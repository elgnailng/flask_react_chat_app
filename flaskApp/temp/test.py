import requests
import time



BASE = "http://127.0.0.1:5000/"
timestamp = int(time.time())
response = requests.post(BASE + "video/1", {"name": "hello", "views": timestamp, "likes":0})
print(response)
input()

response = requests.put(BASE + "video/1", {"name": "hello", "views": timestamp, "likes":0})
print(response)
input()

