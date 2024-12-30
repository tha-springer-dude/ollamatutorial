import ollama

response = ollama.list()

res = ollama.chat(
    
        model="llama3.2",
        messages=[{
            
                "role":"user","content": "why is the sky blue?",
            
            }],
    
    )

res = ollama.chat(
    
        model="llama3.2",
        messages=[
            {
             "role":"user",
             "content": "why is the ocean so salty?",
            },            
            ],
            stream=True,
    
    )


for chunk in res:
    print(chunk["message"]["content"],end="",flush=True)