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
Field workers (i.e. field operations and forestry management employees) often need access to specific information from company protocols and guidelines while working in remote locations. Traditional document searching can be time-consuming and inefficient, and may lead to an inability to find critical information, contributing to less safe and compliant field work.

## Solution
This knowledge assistant uses RAG technology to:
1. Index company documents into a vector database (forestry_ingest.py)
2. Retrieve relevant information based on prompt (forestry_app.py)
3. Generate response using retrieved context (forestry_app.py)
4. Provide citations to ensure transparency and trust (forestry_app.py)

## Demo Application
The Streamlit-based demo allows users to:
- Ask questions in natural language about forestry operations
- Receive AI-generated responses based on company documentation
- View which documents and sections were used to create the response

## Sample Documents
Find the following sample documents in the Sample_Documents folder of this github repository:
- DOUGLAS FIR PLANTING GUIDELINES (PACIFIC NORTHWEST REGION).docx
- WEYERHAEUSER FIRE PREVENTION AND RESPONSE PLAN.docx
- WEYERHAEUSER HARVEST PLANNING CHECKLIST APPLICABLE TO ALL COMPANY-OWNED TIMBERLANDS.docx

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
- Authentication and role-based access control
- Expanded document collection covering more relevant company materials
- Regular indexing updates as documents are modified
- Usage analytics to identify common questions and response preferences

## Low-Code/No-Code Implementation
This same functionality could be implemented in a low-code environment using:
- Microsoft Power Platform (Power Apps + Power Automate)
- Azure OpenAI Service
- Azure Cognitive Search for vector database
- SharePoint for document storage and management

This would likely be easier in a low-code environment... I just can't develop in Power Apps on my personal account!

## Future Enhancements
- **Expanded Testing**: Develop more comprehensive test examples with edge cases to ensure reliability across diverse forestry queries
- **Model Optimization**: Evaluate different LLM models and parameters to balance performance, cost, and latency for production deployment
- **Security Implementation**:Consider adding authentication, role-based access control, and other safety measures to meet enterprise security requirements
- **Responsible AI Framework**: Implement AI ethics guidelines, user feedback mechanisms, and clear disclaimers about potential limitations
- **Performance Monitoring**: Add analytics to track usage patterns, response quality, and identify opportunities for system improvement
- **Mobile Adaptations**: Optimize the interface for field use on mobile devices with limited connectivity
