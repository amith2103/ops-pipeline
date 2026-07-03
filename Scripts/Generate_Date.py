import pandas as pd 
import random 
from faker import Faker
from datetime import datetime, timedelta 

fake = Faker()
random.seed(42)

NUM_RECORDS = 1000
records = []

service_types = ["Electric", "Gas", "Water", "Billing"]

issue_types = {
    "Electric" : ["Power Outage", "volatge Fluctuation", "Meter Error", "Downed Power Line"],
    "Gas" :["Gas Leak", "No Gas Supply", "Meter Error", "Billing Issue"],
    "Water" :["No water Supply", "Low Pressure", "Water Quality", "Pipe  Burst"],
    "Billing":["Incorrect Charge","Payment Not Reflected", "Refund Request", "Account Error"]
}


Priorities = {
    "Gas Leak" : "Critical",
    "Downed Power Line": "Critical",
    "pipe Burst":"Critical",
    "Power Outage":"High",
    "No Water Supply": "High",
    "No Gas Supply ":"High",
    "default":"Medium"
}

statuses = ["Open", "In Progress", "Resolved","Escalated"]
regions = ["North", "South", "East", "West", "Central"]
reps = [fake.name() for _ in range(10)]

for i in range(NUM_RECORDS):
    service = random.choice(service_types)
    issue = random.choice(issue_types[service])
    priority = Priorities.get(issue, Priorities["default"])
    status = random.choice(statuses)
    created = datetime.now() - timedelta(days=random.randint(1, 365))
    resolved = created + timedelta(days=random.randint(1, 30)) if status == "Resolved" else None

    records.append({
        "request_id": f"REQ-{1000 + i}",
        "customer_name": fake.name(),
        "service_type": service,
        "issue_type": issue,
        "priority": priority,
        "status": status,
        "created_date": created.strftime("%Y-%m-%d"),
        "resolved_date": resolved.strftime("%Y-%m-%d") if resolved else None,
        "assigned_to": random.choice(reps),
        "region": random.choice(regions)
    })
    
    df = pd.DataFrame(records)
    df.to_csv("data/service_requests.csv", index=False)
    print(f"Generated {len(df)} records")
    print(df.head())

print(df["status"].value_counts())
print(df[df["status"] == "Resolved"].head())