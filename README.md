# LangChain Learning Repository

This repository contains notebooks and small examples focused on learning and experimenting with **LangChain** and related AI workflows.

## Project Overview

The workspace includes:
- **LangChain notebooks** for prompts, embeddings, document loading, vector stores, and agents.
- **LangGraph** examples for graph-based workflows.
- Small demo applications for running AI models with local or cloud providers.

## Folder Structure

- `langchain/` - Main LangChain practice materials
  - `data ingestion/` - Document loading examples
  - `embeddings/` - Embedding examples
  - `simpleGENAIapp/` - Small GenAI demo apps
  - `text_splitting/` - Text splitter examples
  - `vectorstore/` - Vector database examples (Chroma, FAISS)
  - `lcel/` - LCEL / Runnable examples
  - `langchain_latest/` - Updated LangChain examples
- `langgraph/` - LangGraph notebook examples

## Requirements

The main Python dependencies for the LangChain examples are listed in:
- [langchain/requirements.txt](langchain/requirements.txt)

You may also want to check the additional requirements files under:
- [langchain/langchain_latest/requirements.txt](langchain/langchain_latest/requirements.txt)
- [langchain/langchain_latest/requirements2.txt](langchain/langchain_latest/requirements2.txt)
- [langchain/lcel/requirements.txt](langchain/lcel/requirements.txt)

## Setup

1. Create a virtual environment (recommended)
2. Install the required packages:
   ```bash
   pip install -r langchain/requirements.txt
   ```
3. Install any additional requirements if needed for specific folders.
4. Make sure your API keys or model endpoints are configured before running notebooks.

## How to Use

- Open the `.ipynb` notebooks in Jupyter or VS Code.
- Run the examples in order for learning flow.
- Use the Python scripts in the demo folders as reference implementations.

## Notes

- Some notebooks may require external services such as OpenAI, Ollama, or Hugging Face.
- If a notebook fails because of missing credentials or a package, check the corresponding requirements file and environment setup.

## Learning Topics Covered

- Prompt engineering
- Document loading
- Text splitting
- Embeddings
- Vector stores
- Retrieval-based workflows
- Agents and chains
- LangGraph basics
