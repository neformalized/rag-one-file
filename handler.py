import vectorizer, index, llm

# Document prepare

with open("C:\\Users\\omni\\desktop\\document.txt", "r", encoding="utf-8") as file:
    
    document = file.read()
#

document_chunks = vectorizer.chunking(document, 500, 100)
document_embedding = vectorizer.vectorize(document_chunks)
document_index = index.build(document_embedding)

# Query prepare

query_origin = "ожидаемые результаты"
query_embedding = vectorizer.vectorize(query_origin)

# Search

results = index.search(document_index, document_chunks, query_embedding, 2)

# Results

tmp = list()

for result in results:
    
    for key in result.keys():
        
        #print(f"{key}:{result[key]}")
        if isinstance(result[key], str): tmp.append(result[key])
    #
#

#

print(llm.generate_answer(query_origin, tmp))