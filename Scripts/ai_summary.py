import anthropic
import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("ANTHROPIC_API_KEY")
print("KEY FOUND:", api_key is not None)


# Connect to database
conn = sqlite3.connect("data/ops-pipeline.db")

# Pull key stats
df = pd.read_sql("SELECT * FROM service_requests", conn)

total = len(df)
open_tickets = len(df[df["status"] == "Open"])
critical = len(df[df["priority"] == "Critical"])
by_region = df["region"].value_counts().to_string()
by_service = df["service_type"].value_counts().to_string()

conn.close()

print("Data loaded:", total, "records")


# Build the prompt
prompt = f"""
You are a data analyst for a utility company.
Here is a summary of current service requests:

Total Requests: {total}
Open Tickets: {open_tickets}
Critical Priority: {critical}

By Region:
{by_region}

By Service Type:
{by_service}

Write a short executive summary highlighting key trends, risks, and recommendations.
"""

# Send to Claude API
client = anthropic.Anthropic(api_key=api_key)

message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("\n=== AI EXECUTIVE SUMMARY ===")
print(message.content[0].text)