import faiss, numpy

def build(embeddings: numpy.ndarray) -> faiss.Index:
    
    dim = embeddings.shape[1]
    
    indexes = faiss.IndexFlatIP(dim)
    indexes.add(embeddings)
    
    return indexes
#

def search(store_index: faiss.Index, store_original: list[str], query: numpy.ndarray, top_k: int) -> list[dict]:
    
    scores, indexes = store_index.search(query, top_k)
    
    result = list()
    
    for score, idx in zip(scores[0], indexes[0]):
        
        result.append({
            "idx": idx,
            "score": score,
            "text": store_original[idx]
        })
    #
    
    return result
#