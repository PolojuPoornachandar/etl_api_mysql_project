import pandas as pd

def is_valid_email(email):
    return "@" in email and "." in email

def transform_data():
    df = pd.read_csv("data.csv")
    initial_count = len(df)

    # Basic cleaning
    df = df.dropna()
    df = df[df["email"].apply(is_valid_email)]

    final_count = len(df)
    df.to_csv("cleaned_data.csv", index=False)
    print(f"✅ Transformed data saved to cleaned_data.csv ({final_count}/{initial_count} rows retained)")

if __name__ == "__main__":
    transform_data()

