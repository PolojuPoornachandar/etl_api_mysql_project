from fastapi import FastAPI
from faker import Faker
import random
import csv
from fastapi.responses import PlainTextResponse

app = FastAPI()
fake = Faker()

@app.get("/get-data", response_class=PlainTextResponse)
def get_data():
    rows = []
    header = "id,name,email,phone,salary,join_date"
    rows.append(header)
    for i in range(1, 151):  # 150 rows
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        salary = round(random.uniform(40000, 120000), 2)
        join_date = fake.date_between(start_date="-3y", end_date="today").isoformat()
        row = f"{i},{name},{email},{phone},{salary},{join_date}"
        rows.append(row)
    return "\n".join(rows)

