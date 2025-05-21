import requests

url = "http://127.0.0.1:5001/get-data"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Response Preview:\n", response.text[:500])  # print first 500 chars

