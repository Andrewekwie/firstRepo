import requests
response = requests.get("https://httpbin.org/get")
print(response.content)
# print(type(response.content))
# print(response.text)

response2 = requests.post("https://httpbin.org/post",data="test data",headers={"h1" : "test Title"})
print(response2.text)