from sentence_transformers import SentenceTransformer
import numpy

def chunking(text: str, chunk_size: int = 500, overlap: int = 100) -> list[str]:
    
    chunks = list()
    
    current = 0
    over = len(text)
    
    while current < over:
        
        limit = current + chunk_size
        
        if limit > over: break
        
        chunks.append(text[current:min(limit, over)])
        
        current += (chunk_size - overlap)
    #
    
    return chunks
#

def vectorize(texts: list[str], expand: bool = False) -> numpy.ndarray:
    
    model = SentenceTransformer("intfloat/multilingual-e5-base")
    
    embeddings = model.encode(
        texts,
        convert_to_numpy = True,
        normalize_embeddings = True
    )
    
    return numpy.expand_dims(embeddings, 0) if expand else embeddings
#