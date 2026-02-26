# RAG Engine

A minimal RAG engine with a clear division of responsibilities.
The project is designed as a skeleton, easily expandable with scripts:
QA, summary, quote search, analysis, hybrid search, etc.

## Quick start

Basic query through your document

```python
from rag import RAG

with open("path_to_your_document.txt", "r", encoding="utf-8") as file:
    store = RAG(
        document=file.read(),
        chunk_size=500,
        overlap=100
    )

result = store.query(
    query="question about document", # your query
    top_k=3, # sensevity
    enhance=5 # rewrite your query to queries adopted to RAG mechanism
)
```

Query without response generating

```python
result = store.query(
    query="question about document",
    top_k=3,
    enhance=5,
    strip=True # return only suitable chunks
)
```

Query with original query

```python
result = store.query(
    query="question about document",
    top_k=3,
    enhance=0 # no adopted rewrites
)
```

Query without adopted rewrites and without response generation (no need openai key)

```python
result = store.query(
    query="question about document",
    top_k=3,
    enhance=0,
    strip=True
)
```
