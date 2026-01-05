# RAG Engine

A minimal, yet production-oriented RAG engine with a clear division of responsibilities.
The project is designed as a skeleton, easily expandable with scripts:
QA, summary, quote search, analysis, hybrid search, etc.

## Quick start

```python
from handler import RAG

with open("path_to_your_document.txt", "r", encoding="utf-8") as file:
    store = RAG(
        document=file.read(),
        chunk_size=500,
        overlap=100
    )

result = store.query(
    query="question about document",
    top_k=3,
    enhance=5
)
```
