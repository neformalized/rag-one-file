from openai import OpenAI
import json
from importlib.resources import files

#

client = OpenAI()

def request_to_openai(context: list[dict]) -> str:
    
    request = client.responses.create(
        model="gpt-4.1",
        input=context
    )
    
    #
    
    return request.output_text
#

def prompt_load(name: str) -> str:
    
    return files("rag.engine.prompts").joinpath(name).read_text(encoding="utf-8")
#

def generate_search_queries(user_query: str, max_queries: int = 3, prompt: str) -> list[str]:
    
    context = list()
    
    if prompt: context.append({"role": "system", "content": prompt.format(max_queries=max_queries)})
    else: context.append({"role": "system", "content": prompt_load("search_queries.txt").format(max_queries=max_queries)})
    
    context.append({"role": "user", "content": user_query})
    
    return json.loads(request_to_openai(context))
#

def generate_answer(user_query: str, content: list[str], prompt: str) -> str:
    
    context = list()
    
    if prompt: context.append({"role": "system", "content": prompt.format(user_query=user_query)})
    else: context.append({"role": "system", "content": prompt_load("answer_synth.txt").format(user_query=user_query)})
    
    context.append({"role": "user", "content": "".join(content)})
    
    return request_to_openai(context)
#