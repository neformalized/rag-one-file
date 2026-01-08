import vectorizer, index, llm, retriever

class RAG:
    
    def __init__(self, documents: list[], chunk_size: int = 500, overlap: int = 100):
        
        self.documents = list()
        
        #
        
        for document in documents:
            
            chunks = vectorizer.chunking(document, chunk_size, overlap)
            embedding = vectorizer.vectorize(chunks)
            index = index.build(embedding)
            
            self.documents.append({
                "chunks": chunks,
                "index": index
            })
        #
    #
    
    def query(self, query: str, top_k: int = 2, enhance: int = 3) -> str:
        
        queries_embedding = [vectorizer.vectorize(subquery, True) for subquery in llm.generate_search_queries(query, enhance)] if enhance > 0 else vectorizer.vectorize(query, True)
        
        #
        
        results = list()
        
        for document in self.documents:
            
            results = retriever.dedup([index.search(document["index"], document["chunks"], query_embedding, top_k) for query_embedding in queries_embedding])
        #
        
        #
        
        response = llm.generate_answer(query, results)
        
        #
        
        return response
    #
#

r = Rag()