import streamlit as st
import anthropic
import os
from pinecone import Pinecone
from dotenv import load_dotenv
from openai import OpenAI

# Load the keys!
ant_api = st.secrets["ANTHROPIC_API_KEY"] if "ANTHROPIC_API_KEY" in st.secrets else None
pc_api = st.secrets["PINECONE_API_KEY"] if "PINECONE_API_KEY" in st.secrets else None
oai_api = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else None


if not all([ant_api, pc_api, oai_api]):
    load_dotenv()
    ant_api = os.getenv("ANTHROPIC_API_KEY")
    pc_api = os.getenv("PINECONE_API_KEY")
    oai_api = os.getenv("OPENAI_API_KEY")

# Initialize clients
pc = Pinecone(api_key=pc_api)
index_name = "forestryindex"
index = pc.Index(index_name)

client_ant = anthropic.Anthropic(api_key=ant_api)
client_open = OpenAI(api_key=oai_api)

# Create the vector embedding
def get_embedding(text):
    response = client_open.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding

# Call our LLM, I chose Claude as I have an existing personal account!
def query_claude(prompt, model="claude-3-7-sonnet-20250219", max_tokens=400):
    try:
        response = client_ant.messages.create(
            model=model,
            max_tokens=max_tokens,
            temperature=0.4,
            system="You are a helpful assistant trained on forestry best practices, planting guidelines, harvest planning, and fire prevention. "
                   "Answer concisely and clearly. Cite context providing the exact name of the document in quotations whenever referenced in your response.",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    except Exception as e:
        print(f"Error calling Claude API: {e}")
        return "An error occurred when querying Claude."

# Find the closest "chunks" to the question asked
def search_pinecone(query, top_k=5):
    query_embedding = get_embedding(query)
    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )
    return results.get("matches", [])

# Put context together into prompt and pass to LLm
def generate_response_from_pinecone(query):
    """Search Pinecone, format context, and query Claude."""
    retrieved_chunks = search_pinecone(query)

    if not retrieved_chunks:
        return "I couldn't find any relevant information in the forestry documents."

    # Format retrieved chunks into context
    context = "\n\n".join(
        f"### Source: {match['metadata'].get('source', 'Unknown')}\n"
        f"{match['metadata'].get('text', '[No text available]')}"
        for match in retrieved_chunks
    )


    # Construct the prompt
    prompt = f"""
Use the following retrieved context to answer the user's question.

Context:
{context}

Question: {query}
Answer:
    """

    return query_claude(prompt)


# Webpage UI
st.set_page_config(page_title="Forestry Doc Assistant", page_icon="🌲")
st.title("Forestry Document Chatbot Demo")
st.write("Ask a question based on the forestry guidelines, fire prevention plans, and harvest planning documents found in the GitHub folder ([here](https://github.com/dominicholcomb/Forestry_RAG_UseCase/tree/main/sample_documents)).")
# Add a sidebar with a disclaimer and sample questions
with st.sidebar:
    st.markdown("### ℹ️ Disclaimer")
    st.markdown(
        """
        This use case demonstrates effective document retrieval and summarization 
        for field operations and forestry management employees using **fabricated/test documentation**.  
        
        **Note:** The content of this demo is entirely fictional and does **not** represent official Weyerhaeuser policy.

        ### Sample Questions:
        * What is the minimum required sampling intensity for a timber cruise during the pre-harvest assessment?
        * What is the preferred height range for Douglas Fir seedlings?
        * I planted seedlings. Now what?
        * What percentage of the harvest area must be marked as wildlife retention?
        * What document will provide more information to me on fire prevention protocol?
        """
    )



if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
query = st.chat_input("Ask me anything about forestry...")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    response = generate_response_from_pinecone(query)

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
