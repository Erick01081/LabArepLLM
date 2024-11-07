from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/chain/")
print("Invocando remote_chain con parámetros...")
response = remote_chain.invoke({"language": "italian", "text": "hi"})
print("Respuesta recibida:", response)