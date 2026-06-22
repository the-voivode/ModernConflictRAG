# ModernConflictRAG

A Hybrid Retrieval-Augmented Generation (RAG) system for geopolitical and modern historical documents using PGVector, PostgreSQL Full-Text Search, Reciprocal Rank Fusion (RRF), and Cross-Encoder Reranking.

---

## Overview

ModernConflictRAG is an end-to-end RAG pipeline designed for collections of modern historical and geopolitical conflict texts. The system combines semantic vector search with lexical retrieval to improve recall and uses a cross-encoder reranker to maximize relevance before passing context to an LLM.

The project focuses on retrieval quality and transparency rather than building a complex interface.

---

## Features

- PGVector-backed vector database
- PostgreSQL Full-Text Search (BM25-like lexical retrieval)
- Dense semantic retrieval with BGE embeddings
- Hybrid retrieval (dense + lexical)
- Reciprocal Rank Fusion (RRF)
- Cross-encoder reranking
- Source-aware context construction
- Grounded answer generation
- Streamlit interface
- Modular ingestion and benchmarking pipeline

---

## Architecture

```text
Question
    │
    ▼
Dense Retrieval (BGE + PGVector)
    │
    ├──────────────┐
    │              │
    ▼              ▼
Semantic Search    Lexical Search
                   (PostgreSQL FTS)
    │              │
    └──────┬───────┘
           ▼
      RRF Fusion
           ▼
     Top Candidates
           ▼
Cross-Encoder Reranker
(BAAI/bge-reranker-base)
           ▼
     Top Contexts
           ▼
      Prompt Builder
           ▼
          LLM
           ▼
         Answer
```

---

## Technology Stack

| Component | Technology |
|------------|------------|
| Vector Database | PGVector |
| Database | PostgreSQL |
| Embeddings | BAAI/bge-large-en |
| Lexical Search | PostgreSQL Full-Text Search |
| Fusion | Reciprocal Rank Fusion (RRF) |
| Reranker | BAAI/bge-reranker-base |
| LLM Provider | OpenRouter |
| LLM Models | nvidia/nemotron-3-super-120b |
| Interface | Streamlit |
| Frameworks | LangChain, SentenceTransformers |
| ORM | SQLAlchemy |

---

## Repository Structure

```text
.
├── loader.py
├── chunker.py
├── embed_chunks_to_pg.py
├── test_retrieval.py
├── rag_qa.py
├── app.py
├── config.py
├── artifacts/
├── metadata/
├── screenshots/
├── architecture/
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/the-voivode/ModernConflictRAG.git
cd ModernConflictRAG
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Ensure `.env` is included in `.gitignore`.

---

## PostgreSQL + PGVector Setup

Enable the vector extension:

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

Example connection string:

```python
postgresql+psycopg://USER:PASSWORD@localhost:5432/ModernConflictRAG
```

---

## Quick Start

### 1. Configure

Set:

- Connection string
- Collection name
- Embedding model
- Retrieval parameters
- Reranker settings

inside `config.py`.

---

### 2. Load Documents

```bash
python loader.py
```

---

### 3. Chunk Documents

```bash
python chunker.py
```

---

### 4. Embed and Store in PGVector

```bash
python embed_chunks_to_pg.py
```

---

### 5. Benchmark Retrieval

```bash
python test_retrieval.py
```

Supported retrieval modes:

- Dense retrieval
- Lexical retrieval
- Hybrid retrieval
- Cross-encoder reranking

---

### 6. Run Question Answering

```bash
python rag_qa.py
```

---

### 7. Launch the Streamlit Interface

```bash
streamlit run app.py
```

---

## Retrieval Pipeline

### Dense Retrieval

Semantic search is performed using:

- BAAI/bge-large-en
- PGVector
- Cosine similarity

---

### Lexical Retrieval

Lexical matching is performed using PostgreSQL Full-Text Search.

---

### Hybrid Retrieval

Dense and lexical results are combined using:

- Reciprocal Rank Fusion (RRF)

---

### Cross-Encoder Reranking

Candidate passages are reranked using:

- BAAI/bge-reranker-base

Only the highest-ranked chunks are passed to the language model.

---

## Example Query

### Question

> What caused the French Revolution?

### Retrieved Context

- Economic crises
- Social inequality
- Enlightenment ideas

### Generated Answer

> According to the retrieved sources, the French Revolution resulted from financial instability, social inequality, and Enlightenment thought.

---

## Project Goals

- Improve retrieval quality through hybrid search
- Reduce hallucinations via grounded context
- Provide transparent source-aware answers
- Explore retrieval optimization techniques
- Benchmark semantic and lexical retrieval strategies

---

## Future Work

- Query expansion
- Metadata filtering
- RAGAS evaluation
- Knowledge graph integration
- GraphRAG
- Agentic RAG
- Multi-query retrieval
- Parent-child retrieval
- Multilingual support
- Fine-tuned embedding models

---

## Screenshots

### Streamlit Interface, Generated Answer and Retrieved Sources

![App Screenshot](Screenshots/Screenshot2.png)
![App Screenshot](Screenshots/Screenshot1.png)

---

## Built With

- LangChain
- SentenceTransformers
- PGVector
- PostgreSQL
- SQLAlchemy
- HuggingFace
- Streamlit
- OpenRouter

---

## License


---

## Citation

```bibtex
@software{ModernConflictRAG,
  title = {ModernConflictRAG},
  author = {the-voivode},
  year = {2026},
  description = {A Hybrid Retrieval-Augmented Generation System for Geopolitical and Modern Historical Conflict Documents using PGVector, PostgreSQL Full-Text Search, Reciprocal Rank Fusion, and Cross-Encoder Reranking.}
}
```
