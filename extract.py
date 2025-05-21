import requests

def extract_data():
    url = "http://127.0.0.1:5001/get-data"
    response = requests.get(url)
    
    if response.status_code == 200:
        with open("data.csv", "w") as file:
            file.write(response.text)
        print("✅ Data extracted and saved to data.csv")
    else:
        print("❌ Failed to extract data. Status code:", response.status_code)

if __name__ == "__main__":
    extract_data()

