AskCarlos: Your Sassy AI Stylist, Strategist, and Spanish F1 Legend

AskCarlos is a local Retrieval-Augmented Generation (RAG) chatbot inspired by none other than Carlos Sainz Jr.—with flair, charm, and a little sass. It answers your questions using uploaded PDFs as context, with the wit and warmth of a Spanish F1 driver who moonlights as your personal assistant.

💪 What Can AskCarlos Do?

Load and understand unstructured PDF content

Split it into digestible chunks for fast search

Embed it locally using nomic-embed-text

Store it in a Chroma vector database

Generate multiple query variants for better RAG retrieval

Respond with charming, context-specific answers using a custom Carlos Sainz persona

All of this, completely offline using Ollama, with no cloud APIs or external dependencies.

🛠️ Tech Stack

Language Model: Ollama (carlos:latest)

Embeddings: Ollama (nomic-embed-text)

Document Loader: UnstructuredPDFLoader

Vector DB: Chroma

LangChain: Chains, Retrievers, PromptTemplates, Runnables

Logging: Python logging for runtime feedback

🔧 How It Works

1. Load PDF
2. Chunk PDF content
3. Create local embeddings with Ollama
4. Store chunks in Chroma vector DB
5. Use multi-query retriever to reformulate questions
6. Answer questions ONLY using vector search context
7. Respond with a Carlos-style comment

🚀 Example Use Case

You upload a PDF (technique.pdf) and ask:

"What is Floor fences and why do we need them?"

Carlos responds:

"Ahh, floor fences! Not just a fashion statement for the underbody, mi carino. They help with sealing the airflow, giving more downforce. Essential for precision in those tight corners."

🧡 Why I Built This

Inspired by the confident, tactical personality of Carlos Sainz Jr., I built AskCarlos as a playful yet technically sound AI assistant that could explain engineering concepts with charm and clarity. What started as a fun exploration became a solid RAG application.

🔹 Run It Yourself

Clone the repo

Place your .pdf file in ./data/

Update DOC_PATH if needed

Run python askcarlos.py

💪 Future Improvements

Streamlit UI with Carlos Sainz theme

Add voice (Spanish-accented TTS)

Accept user PDFs via drag-and-drop

📅 Status

Project: Complete (Core working, charming, and informative)

Stage: Personal Portfolio

Next Up: Adding voice and visuals. Because Carlos deserves it.

Made with love, Python, and just the right amount of flair. Viva Carlos 🇪🇸
