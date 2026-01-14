def dedup(bundle_of_chunks: list[list[dict]]) -> list[dict]:
    
    results, results_sorted = dict(), dict()
    
    #
    
    for chunks in bundle_of_chunks:
        
        for chunk in chunks:
            
            if chunk["idx"] not in results.keys():
                
                results[chunk["idx"]] = chunk["text"]
            #
        #
    #
    
    for key in sorted(results):
        
        results_sorted[key] = results[key]
    #
    
    return results_sorted
#

def strip(raw_chunks: list[dict]) -> list[str]:
    
    return [raw_chunks[key] for key in raw_chunks.keys()]
#