import vectorizer, index, llm, retriever

class RAG:
    
    def __init__(self, document: str, chunk_size: int = 500, overlap: int = 100):
        
        self.document_chunks = vectorizer.chunking(document, chunk_size, overlap)
        self.document_embedding = vectorizer.vectorize(self.document_chunks)
        self.document_index = index.build(self.document_embedding)
    #
    
    def query(self, query: str, top_k: int = 2, enhance: int = 3) -> str:
        
        queries_embedding = [vectorizer.vectorize(subquery, True) for subquery in llm.generate_search_queries(query, enhance)] if enhance > 0 else vectorizer.vectorize(query, True)
        
        results = retriever.dedup([index.search(self.document_index, self.document_chunks, query_embedding, top_k) for query_embedding in queries_embedding])
        
        response = llm.generate_answer(query, results)
        
        return response
    #
#