import pandas as pd
import mysql.connector

def load_data():
    # Load the cleaned CSV data
    df = pd.read_csv("cleaned_data.csv")

    df['age'] = 25


    # Print first 5 rows and columns to verify data structure
    print(df.head())
    print(df.columns)

    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="etl_user",
        password="Chandu0009$",
        database="etl_db"
    )
    cursor = conn.cursor()

    # Create the employees table with age column included
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            email VARCHAR(100),
            phone VARCHAR(50),
            salary FLOAT,
            join_date DATE
        )
    """)

    # Insert or update each row from dataframe into the employees table
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO employees (id, name, age, email, phone, salary, join_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                name=VALUES(name),
                age=VALUES(age),
                email=VALUES(email),
                phone=VALUES(phone),
                salary=VALUES(salary),
                join_date=VALUES(join_date)
        """, (row['id'], row['name'], row['age'], row['email'], row['phone'], row['salary'], row['join_date']))

    # Commit transaction and close connection
    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Data loaded into MySQL database")

if __name__ == "__main__":
    load_data()

