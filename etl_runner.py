import pandas as pd
import requests

url = "http://127.0.0.1:5001/get-data"
response = requests.get(url)

# Load CSV into DataFrame
from io import StringIO
df = pd.read_csv(StringIO(response.text))

print(df.head(10))  # 🔍 Check first 10 rows
print(df.shape)     # 🔍 Should be (150, 6) or similar

# Then insert into MySQL

