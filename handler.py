import vectorizer, index, llm, retriever

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

results = retriever.dedup_multiquery([index.search(document_index, document_chunks, query_embedding, 2) for query_embedding in subquery_embedding])

# Join results

print(llm.generate_answer(query_origin, results))