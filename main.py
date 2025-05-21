from fastapi import FastAPI, Response
from faker import Faker
import csv
import io
import random

app = FastAPI()
fake = Faker()

@app.get("/get-data")
def get_data():
    headers = ['id', 'name', 'email', 'phone', 'salary', 'join_date']
    data = []

    for i in range(1, 151):
        row = {
            'id': i,
            'name': fake.name(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'salary': round(random.uniform(40000, 120000), 2),
            'join_date': fake.date_between(start_date='-3y', end_date='today')
        }
        data.append(row)

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)

    return Response(content=output.getvalue(), media_type='text/csv')

