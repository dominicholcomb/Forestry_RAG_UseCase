# Weyerhaeuser Forestry Knowledge Assistant Demo

## Quick Start
1. Open the application: [here](https://holcombforestryragusecase.streamlit.app/) (or paste this link: https://holcombforestryragusecase.streamlit.app/)
 
  **BE SURE TO CLICK "Yes, get this app back up!" IF THE APPLICATION HAS FALLEN ASLEEP**
2. Try asking these sample questions:
   - "What is the minimum required sampling intensity for a timber cruise during the pre-harvest assessment?"
   - "What is the preferred height range for Douglas Fir seedlings?"

## Overview
This demo showcases a Retrieval-Augmented Generation (RAG) system designed for Weyerhaeuser's field operations and forestry management teams. The application allows employees to query forestry-related information using natural language, receiving accurate answers derived from company documentation.

## Problem Statement
Field workers often need access to specific information from company protocols and guidelines while working in remote locations. Traditional document searches can be time-consuming and inefficient, especially when trying to find specific details across multiple documents.

## Solution
This knowledge assistant uses RAG technology to:
1. Index company documents into a vector database
2. Retrieve relevant information based on natural language queries
3. Generate comprehensive, accurate responses using retrieved context
4. Provide source attribution to ensure transparency and trust

## Demo Application
The Streamlit-based demo allows users to:
- Ask questions in natural language about forestry operations
- Receive AI-generated responses based on company documentation
- View which documents and sections were used to create the response
- Explore example questions through the sidebar

## Sample Documents
Find the following sample documents in the Sample_Documents folder of this github repository:
- Douglas Fir Planting Guidelines (Pacific Northwest Region)
- Weyerhaeuser Fire Prevention and Response Plan
- Weyerhaeuser Harvest Planning Checklist

## Testing
A sample set of test queries and expected responses can be found in this [Google Sheet](https://docs.google.com/spreadsheets/d/1TkVRBcPWqG4YY9x1mxdUZwh_Xyt-qlE0Nqw20x5X68U/edit?usp=sharing).

## Technical Implementation

The demo uses:
- **Vector Database**: Pinecone for document embedding storage and retrieval
- **Document Processing**: LangChain for document loading and chunking with source metadata preservation
- **Embedding**: OpenAI's text-embedding-ada-002 model
- **LLM**: Anthropic's Claude 3.7 Sonnet for generating responses
- **UI**: Streamlit for the conversational interface

The application implements a complete RAG workflow:
1. Documents are processed, chunked, and embedded
2. User queries are converted to embeddings and used for semantic search
3. Retrieved context is combined with the original query
4. Claude generates responses with proper source attribution

## Production Implementation
For a production environment, this solution would be enhanced with:
- Cloud-based vector database (like Pinecone) for scalability
- Authentication and role-based access control
- Expanded document corpus covering all relevant company materials
- Regular indexing updates as documents are modified
- Usage analytics to identify common queries and gaps in documentation

## Low-Code/No-Code Implementation
This same functionality could be implemented in a low-code environment using:
- Microsoft Power Platform (Power Apps + Power Automate)
- Azure OpenAI Service
- Azure Cognitive Search for vector database
- SharePoint for document storage and management

## Future Enhancements
- **Expanded Testing**: Develop more comprehensive test examples with edge cases to ensure reliability across diverse forestry queries
- **Model Optimization**: Evaluate different LLM models and parameters to balance performance, cost, and latency for production deployment
- **Security Implementation**: Add authentication, role-based access control, and data encryption to meet enterprise security requirements
- **Responsible AI Framework**: Implement AI ethics guidelines, user feedback mechanisms, and clear disclaimers about potential limitations
- **Performance Monitoring**: Add analytics to track usage patterns, response quality, and identify opportunities for system improvement
- **Mobile Adaptations**: Optimize the interface for field use on mobile devices with limited connectivity
