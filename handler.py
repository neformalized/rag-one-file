import vectorizer, index

# Document prepare

with open("C:\\Users\\omni\\desktop\\document.txt", "r", encoding="utf-8") as file:
    
    document = file.read()
#

document_chunks = vectorizer.chunking(document, 500, 100)
document_embedding = vectorizer.vectorize(document_chunks)
document_index = index.build(document_embedding)

# Query prepare

query = vectorizer.vectorize("ожидаемые результаты")

# Search

results = index.search(document_index, document_chunks, query, 2)

# Results



for result in results:
    
    for key in result.keys():
        
        print(f"{key}:{result[key]}")
    #
    
    print("")
#