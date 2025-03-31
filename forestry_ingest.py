
import os
from langchain.document_loaders import Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone as PineconeVectorStore
import pinecone
from pinecone import Pinecone
from uuid import uuid4




# Get my keys and set environment
openai_api_key = os.getenv("OPENAI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_env="us-west2"

# Initialize Pinecone
pc = Pinecone(api_key=pinecone_api_key)

index_name = "forestryindex"
index = pc.Index(index_name)



# Make compatible for .docx files. Simple to add functionality for more document types like .pdf, .txt, and even images if using chatgpt, claude or others!
def load_documents(file_paths):
    documents = []
    for file_path in file_paths:
        if file_path.endswith(".docx"):
            loader = Docx2txtLoader(file_path)
            docs = loader.load()

            short_name = os.path.splitext(os.path.basename(file_path))[0]  # remove .docx
            for doc in docs:
                doc.metadata["source"] = short_name

            documents.extend(docs)
            print(f"✅ Loaded: {short_name}")
    return documents

# Chunking
def process_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks")
    return chunks

# Pinecone indexing classic

def index_documents(chunks):
    embeddings_model = OpenAIEmbeddings()
    
    # Extract the texts and metadata from the langchain documents
    texts = [doc.page_content for doc in chunks]
    metadatas = [doc.metadata for doc in chunks]
    
    # Generate embeddings
    print("Generating embeddings...")
    vectors = embeddings_model.embed_documents(texts)

    # Prepare data for Pinecone upsert
    pinecone_vectors = []
    for i, (vector, metadata) in enumerate(zip(vectors, metadatas)):
        pinecone_vectors.append({
            "id": str(uuid4()),
            "values": vector,
            "metadata": {
                "text": texts[i], 
                **metadata    
            }
        })


    index.upsert(vectors=pinecone_vectors)
    print("Documents successfully indexed in Pinecone.")


# Execute
if __name__ == "__main__":
    desktop_path = os.path.expanduser("~/Desktop") #I just kept these on my desktop for simplicity haha. I have done this from AWS though and it is not too much more involved!
    docs_folder = os.path.join(desktop_path, "sample_documents")
    index.delete(delete_all=True) # this deletes all the files and reuploads. Make sure if I keep this line in that I'm uploading all documents.


    file_paths = [
        os.path.join(docs_folder, "DOUGLAS FIR PLANTING GUIDELINES (PACIFIC NORTHWEST REGION).docx"),
        os.path.join(docs_folder, "WEYERHAEUSER FIRE PREVENTION AND RESPONSE PLAN.docx"),
        os.path.join(docs_folder, "WEYERHAEUSER HARVEST PLANNING CHECKLIST  APPLICABLE TO ALL COMPANY-OWNED TIMBERLANDS.docx")
    ]

    documents = load_documents(file_paths)
    chunks = process_documents(documents)
    index_documents(chunks)