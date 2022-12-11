import requests
import time
BASE = "http://127.0.0.1:5000/"

timestamp = int(time.time())
response = requests.get(BASE + "messages")
print(response.json())
input()
response = requests.put(BASE + "messages", {"text": "hello", "createdAt": timestamp, "uid":0, "photoURL":"http://api.adorable.io/avatars/285/abott@adorable.png"})

response = requests.put(BASE + "messages", {"text": "hello", "createdAt": timestamp, "uid":1, "photoURL":"http://api.adorable.io/avatars/285/abott@adorable.png"})

response = requests.put(BASE + "messages", {"text": "hello", "createdAt": timestamp, "uid":2, "photoURL":"http://api.adorable.io/avatars/285/abott@adorable.png"})

response = requests.put(BASE + "messages", {"text": "hello", "createdAt": timestamp, "uid":3, "photoURL":"http://api.adorable.io/avatars/285/abott@adorable.png"})
response = requests.put(BASE + "messages", {"text": "hello", "createdAt": timestamp, "uid":4, "photoURL":"http://api.adorable.io/avatars/285/abott@adorable.png"})
print(response.json())
input()
response = requests.get(BASE + "messages")
print(response.json())