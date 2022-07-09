import requests

# print("# All Employe Info")
# URL = "http://127.0.0.1:8000/empinfo"

# print("# Single Project Info")
# URL = "http://127.0.0.1:8000/projectinfo/1"

print("# ALL Project Info")
URL = "http://127.0.0.1:8000/projectinfo/1"

r = requests.get(url= URL)

data = r.json()
print(data)