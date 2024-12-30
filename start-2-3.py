import ollama

# Create a new model with modelfile
modelfile = """
FROM llama3.2
SYSTEM You are very smart and know everything about oceans. You are very succinct and informative.
PARAMETER temperature 0.1
"""

# Create the model
ollama.create(model="mynerd", modelfile=modelfile)

# Generate a response
res = ollama.generate(model="mynerd", prompt="why is the ocean salty?")


# If the response contains the "response" key, you can access it like this:
print(res["response"])


# delete model
#ollama.delete("mynerd")