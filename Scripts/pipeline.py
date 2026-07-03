import pandas as pd
import sqlite3
import os 

# Load the CSV
df = pd.read_csv("data/service_requests.csv")

#clean column names
df.columns = df.columns.str.strip()

# clean string columns - remove extra spaces
df["status"] = df["status"].str.strip()
df["priority"] = df["priority"].str.strip()
df["issue_type"] = df["issue_type"].str.strip()
df["service_type"] = df["service_type"].str.strip()
df["region"] = df["region"].str.strip()

print("shape:", df.shape)
print("Nulls:\n",df.isnull().sum())
print(df.head())


# connect to SQLITE Database (Creates it if it doesn't exist)
conn = sqlite3.connect("data/ops-pipeline.db")

# SAVE DataFrame to database
df.to_sql("service_requests", conn, if_exists="replace", index=False)

print("Data saved to Database successfully!")
print("Total records in DB:", pd.read_sql("SELECT COUNT(*) FROM service_requests", conn).iloc[0,0])

conn.close()