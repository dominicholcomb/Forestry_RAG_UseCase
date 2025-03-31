# Weyerhaeuser Forestry Knowledge Assistant

## Quick Start
1. Launch the application: [here](https://holcombforestryragusecase.streamlit.app/) (or paste this link: https://holcombforestryragusecase.streamlit.app/)
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
This demo uses the following company documents:
- Douglas Fir Planting Guidelines (Pacific Northwest Region)
- Weyerhaeuser Fire Prevention and Response Plan
- Weyerhaeuser Harvest Planning Checklist

## Testing
A sample set of test queries and expected responses can be found in this [Google Sheet](https://docs.google.com/spreadsheets/d/1TkVRBcPWqG4YY9x1mxdUZwh_Xyt-qlE0Nqw20x5X68U/edit?usp=sharing).

## Technical Implementation
The demo uses:
- LangChain for document processing and RAG implementation
- PineCone for vector storage and similarity search
- OpenAI's embedding model for document vectorization
- OpenAI's language model for response generation
- Streamlit for the user interface

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

## Setup and Installation
1. Clone this repository
2. Install requirements: `pip install -r requirements.txt`
3. Add your OpenAI API key to the `.env` file
4. Run the document indexing: `python ingest.py`
5. Launch the app: `streamlit run app.py`

## Future Enhancements
- Mobile application for field use
- Offline mode for areas with limited connectivity
- Voice interface for hands-free operation
- Integration with GIS data for location-specific information
- Expansion to other business units and document types
