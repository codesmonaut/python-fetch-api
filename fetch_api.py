import requests

res = requests.get("http://localhost:3030/shoes")
data = res.json()

for item in data:
    print(f"Brend patike je {item['brand']} a model je {item['model']}.")