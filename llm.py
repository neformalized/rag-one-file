from openai import OpenAI
import json

#

client = OpenAI()

#

def request_to_openai(context: list[dict]) -> str:
    
    request = client.responses.create(
        model="gpt-4.1",
        input=context
    )
    
    #
    
    return request.output_text
#

def generate_search_queries(user_query: str, max_queries: int = 3) -> list[str]:
    
    context = list()
    
    with open("prompts/search.txt", "r", encoding = "utf-8") as file:
        
        context.append({"role": "system", "content": file.read().format(max_queries=max_queries)})
    #
    
    context.append({"role": "user", "content": user_query})
    
    #
    
    return json.loads(request_to_openai(context))
#

def generate_answer(user_query: str, content: list[str]) -> str:
    
    context = list()
    
    with open("prompts/answer_synth.txt", "r", encoding = "utf-8") as file:
        
        context.append({"role": "system", "content": file.read().format(user_query=user_query)})
    #
    
    context.append({"role": "user", "content": "".join(content)})
    
    #
    
    return request_to_openai(context)
#