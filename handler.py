import vectorizer, index, llm, retriever

class RAG:
    
    def __init__(self, document: str, chunk_size: int = 300, overlap: int = 50):
        
        self.chunks = vectorizer.chunking(document, chunk_size, overlap)
        self.embedding = vectorizer.vectorize(self.chunks)
        self.index = index.build(self.embedding)
        
        #
    #
    
    def query(self, query: str, top_k: int = 2, enhance: int = 3, strip: bool = False) -> str:
        
        queries_embedding = [vectorizer.vectorize(subquery, True) for subquery in llm.generate_search_queries(query, enhance)] if enhance > 0 else vectorizer.vectorize(query, True)
        
        #
        
        results = retriever.dedup([index.search(self.index, self.chunks, query_embedding, top_k) for query_embedding in queries_embedding])
        
        #
        
        if strip: return "\n".join(result)
        
        #
        
        return llm.generate_answer(query, results)
        
    #
#