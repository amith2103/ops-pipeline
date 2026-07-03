# 🔧 AI-Powered Operations & Stakeholder Reporting Pipeline

> An end-to-end automated data pipeline built for utility sector operations — ingests service request data, cleans and stores it, generates AI-powered executive summaries using Claude API, and auto-produces Excel dashboards and PowerPoint reports ready for stakeholder delivery.

---

## 🚀 Project Overview

This project simulates a real-world **utility company operations reporting workflow**. Instead of analysts spending hours manually compiling reports, this pipeline automates the entire process — from raw data ingestion to polished executive-ready output — in minutes.

Built to demonstrate skills in:
- End-to-end data pipeline development
- AI integration for business intelligence
- Automated stakeholder reporting (Excel + PowerPoint)
- Energy/public sector data analysis

---

## 🏗️ Pipeline Architecture

```
generate_data.py
       │
       ▼
 service_requests.csv  (1,000 realistic utility service records)
       │
       ▼
pipeline.py  ──►  SQLite Database (ops-pipeline.db)
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
   ai_summary.py   excel_report.py  ppt_report.py
          │              │              │
          ▼              ▼              ▼
  AI Executive      Excel Dashboard   PowerPoint
    Summary         (dashboard.xlsx)  Executive Report
  (Claude API)                     (executive_report.pptx)
```

---

## 📁 Project Structure

```
ops-pipeline/
├── scripts/
│   ├── generate_data.py      # Simulates 1,000 realistic utility service requests
│   ├── pipeline.py           # Cleans, validates, and stores data in SQLite
│   ├── ai_summary.py         # Claude AI generates plain-English executive summary
│   ├── excel_report.py       # Auto-generates styled Excel dashboard
│   └── ppt_report.py         # Auto-generates PowerPoint executive report
├── data/                     # Generated outputs (gitignored)
├── main.py                   # Entry point
├── .env                      # API keys (gitignored)
├── .gitignore
└── README.md
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3 |
| Data Processing | Pandas |
| Database | SQLite |
| AI / NLP | Claude API (Anthropic) — `claude-haiku-4-5` |
| Excel Reporting | openpyxl |
| PowerPoint Reporting | python-pptx |
| Fake Data Generation | Faker, random |
| Environment Management | python-dotenv |

---

## 📊 Dataset

The pipeline generates **1,000 realistic utility service requests** with intentional patterns:

| Field | Description |
|-------|------------|
| `request_id` | Unique ID (REQ-1000 to REQ-1999) |
| `customer_name` | Realistic fake customer names |
| `service_type` | Electric, Gas, Water, Billing |
| `issue_type` | Realistic issues per service type |
| `priority` | Critical / High / Medium (rule-based) |
| `status` | Open / In Progress / Resolved / Escalated |
| `created_date` | Random date within last 365 days |
| `resolved_date` | Only populated for Resolved tickets |
| `assigned_to` | Pool of 10 fake technicians/reps |
| `region` | North / South / East / West / Central |

**Realistic patterns built in:**
- Gas Leaks and Downed Power Lines are always `Critical`
- Power Outages and No Water Supply are always `High`
- Resolved tickets always have a `resolved_date`, others don't

---

## 🤖 AI Executive Summary (Sample Output)

```
EXECUTIVE SUMMARY — Utility Service Request Analysis

Current Status:
- 1,000 total requests with 246 open tickets (24.6% backlog)
- 116 critical priority cases requiring immediate attention

Key Risks:
- High open ticket ratio may impact customer satisfaction and SLA compliance
- Billing surge (275 requests, 27.5%) may indicate system issues or rate changes
- West region elevated demand (214 requests) — potential resource reallocation needed

Recommendations:
1. Immediate: Prioritize 116 critical tickets; assess staffing vs resolution timelines
2. Short-term: Investigate billing spike root cause; issue targeted customer communications
3. Ongoing: Establish SLA targets and monitor regional performance monthly
```

---

## 📈 Excel Dashboard (3 Sheets)

- **Summary** — Total requests, open tickets, resolved count, critical count
- **By Region** — Ticket volume breakdown across North, South, East, West, Central
- **By Service Type** — Volume breakdown across Electric, Gas, Water, Billing

---

## 📑 PowerPoint Executive Report (3 Slides)

- **Slide 1** — Title slide with project branding
- **Slide 2** — Key metrics at a glance (large KPI numbers)
- **Slide 3** — Insights and recommendations with business context

---

## 🛠️ How to Run

**1. Clone the repo:**
```bash
git clone https://github.com/amith2103/ops-pipeline.git
cd ops-pipeline
```

**2. Install dependencies:**
```bash
pip install pandas faker anthropic openpyxl python-pptx python-dotenv
```

**3. Set up your API key:**

Create a `.env` file in the root folder:
```
ANTHROPIC_API_KEY=your-api-key-here
```

**4. Run the pipeline in order:**
```bash
python scripts/generate_data.py   # Generate data
python scripts/pipeline.py        # Clean and store
python scripts/ai_summary.py      # AI summary
python scripts/excel_report.py    # Excel dashboard
python scripts/ppt_report.py      # PowerPoint report
```

---

## 💡 Key Learnings & Skills Demonstrated

- Designed and built a **multi-script data pipeline** from scratch
- Applied **realistic data modeling** with business-logic-based patterns
- Integrated **Claude AI API** for automated natural language reporting
- Generated **production-style Excel and PowerPoint reports** programmatically
- Practiced **secure credential management** with `.env` and `.gitignore`
- Used **SQLite** as a lightweight operational database

---

## 👤 Author

**Amith** — Aspiring Data Analyst | Austin, TX  
[GitHub](https://github.com/amith2103)

---

> *Built as a portfolio project targeting Data Analyst roles in the energy and public sector space.*
