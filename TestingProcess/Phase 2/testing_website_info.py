import requests
import json

t = requests.get("https://www.wordreference.com/es/translation.asp?tranword=hello")

print(json.loads(t.content))
print(t.status_code)