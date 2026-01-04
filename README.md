LangChain with Python – Complete Learning Repository

This repository is a hands-on, structured learning project for mastering LangChain using Python.
It covers everything from LLMs, prompts, chains, retrievers, vector databases, tools, output parsers, and runnables with practical examples.

Perfect for:

Python developers learning Generative AI

Beginners exploring LangChain

Backend developers building LLM-powered applications

🧰 Tech Stack

Python 3.11+

LangChain

OpenAI / Google Gemini / Hugging Face

Chroma / FAISS (Vector Databases)

Pydantic

Jupyter Notebook

⚙️ Python Environment Setup (Start Here)
1️⃣ Clone the Repository
git clone https://github.com/Sushildevelop/Langchain-models.git
cd langchain-project

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Virtual Environment

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Environment Variables Setup

Create a .env file using the example:

cp .env.example .env


Add your API keys:

OPENAI_API_KEY=your_api_key
GOOGLE_API_KEY=your_api_key

📁 Project Structure Explained
🔗 Chains/

Contains examples of LangChain chains showing how multiple components (prompt → model → output) work together.

💬 ChatModels/

Demonstrates usage of different chat-based LLMs such as:

OpenAI Chat Models

Google Gemini

Hugging Face models

🧠 LLMs/

Covers base LLM usage without chat history, focusing on:

Text generation

Prompt → response flow

📝 Prompts/

Examples of:

Prompt templates

Dynamic prompts

Structured prompts

📦 Pydantic/

Uses Pydantic models to:

Validate LLM responses

Enforce structured output

Ensure type safety

🔍 Retrievers/

Implements different retrieval strategies used in:

RAG (Retrieval Augmented Generation)

Semantic search

🏃 Runnables/

Shows LangChain Runnable interfaces, including:

RunnableSequence

RunnableParallel

RunnableLambda

🛠️ Tools/

Custom and built-in LangChain tools, enabling:

Tool calling

Function execution by LLMs

📑 Typeddict/

Uses TypedDict for structured output:

Lightweight alternative to Pydantic

Useful for simple schema enforcement

🤖 chatbot/

Simple chatbot implementation using:

LangChain

Memory

Prompt + LLM pipeline

📂 document_loader/

Demonstrates different document loaders, such as:

Text files

PDFs

Web pages

📤 output_parser/

Shows how to:

Parse LLM responses

Convert text into structured data

✂️ text_splitters/

Implements:

Character-based splitters

Recursive splitters

Semantic text splitting

🧮 vector_database/

Vector DB implementations using:

Chroma

FAISS

Embeddings storage and similarity search

Pincone

🔐 .env.example

Template file for storing environment variables safely.

📌 Key Concepts Covered

LangChain Architecture

Prompt Engineering

RAG (Retrieval Augmented Generation)

LLM Tool Calling

Vector Databases

Structured Output Parsing

Runnable-based Pipelines

🎯 Who Should Use This Repo?

✔ Python Beginners entering AI
✔ Backend Developers exploring LLMs
✔ AI Enthusiasts learning LangChain
✔ Students & Self-learners

📈 Future Enhancements

Agentic RAG

Multi-agent systems

LangGraph integration

Streaming responses

Production-ready APIs

⭐ Support & Contribution

If you find this repository helpful: 

⭐ Star the repo

🍴 Fork it

🧠 Learn & Experiment

👨‍💻 Maintained by

Sushil Chaubey
Backend Developer | Python | LangChain | Generative AI

.venv\Scripts\activate 

! pip install langchain langchain-core langchain-community pydantic ddgs langchain_experimental


pip install -U ddgs duckduckgo-search langchain-community


