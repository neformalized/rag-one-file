import vectorizer, index, llm, retriever

class RAG:
    
    def __init__(self, document: str, chunk_size: int = 500, overlap: int = 100):
        
        self.document_chunks = vectorizer.chunking(document, chunk_size, overlap)
        self.document_embedding = vectorizer.vectorize(self.document_chunks)
        self.document_index = index.build(self.document_embedding)
    #
    
    def query(self, query: str, top_k: int = 2, enhance: int = 5) -> str:
        
        queries_embedding = [vectorizer.vectorize(subquery, True) for subquery in llm.generate_search_queries(query, enhance)] if enhance > 0 else vectorizer.vectorize(query, True)
        
        results = retriever.dedup([index.search(self.document_index, self.document_chunks, query_embedding, top_k) for query_embedding in queries_embedding])
        
        response = llm.generate_answer(query, results)
        
        return response
    #
#


"""

# Document prepare

with open("C:\\Users\\omni\\desktop\\document.txt", "r", encoding="utf-8") as file:
    
    document = file.read()
#

document_chunks = vectorizer.chunking(document, 500, 100)
document_embedding = vectorizer.vectorize(document_chunks)
document_index = index.build(document_embedding)

# Query prepare

query_origin = "ожидаемые результаты"
#query_embedding = vectorizer.vectorize(query_origin, True)

subquery_embedding = [vectorizer.vectorize(subquery, True) for subquery in llm.generate_search_queries(query_origin)]

# Search

#results = index.search(document_index, document_chunks, query_embedding, 2)

results = retriever.dedup([index.search(document_index, document_chunks, query_embedding, 2) for query_embedding in subquery_embedding])

# Join results

print(llm.generate_answer(query_origin, results))

"""