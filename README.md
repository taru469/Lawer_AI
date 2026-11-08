# ⚖️ DepositMitra (न्यायमित्र)
### Pre-Litigation AI Paralegal for Indian Renter Security Deposit Recovery
**Submission for Kuku AI Generalist Assignment — Problem 2**

🌐 **Live Deployed Prototype:** [https://deposit-mitra.streamlit.app](https://deposit-mitra.streamlit.app)  
📁 **GitHub Repository:** [https://github.com/taru469/Lawer_AI](https://github.com/taru469/Lawer_AI)

---

## 📌 Executive Summary
In urban India (Bengaluru, Pune, Gurgaon, Mumbai), over **80% of tenants forfeit ₹25,000–₹80,000** in withheld security deposits upon move-out. Landlords routinely invent arbitrary deductions (e.g. flat ₹25k painting charges, ₹10k deep cleaning) or simply ghost the tenant. Hiring a formal advocate costs ₹15,000–₹30,000 upfront, rendering formal litigation economically irrational.

**DepositMitra** is a specialized pre-litigation paralegal that gives tenants actionable legal leverage without expensive litigation. It converts messy Hinglish/English narratives into structured timelines, audits deductions against established Indian **"Normal Wear and Tear"** doctrines, drafts an authentic **15-Day Statutory Legal Demand Notice**, and lets the tenant practice arguing against an evasive landlord before calling them.

---

## 🛡️ Anti-Hallucination & Architecture (What AI does vs. Rules)
To guarantee strict compliance with Kuku's ground rules ("*AI models confidently invent laws, sections, and past cases, so tell us how yours avoids that*"), DepositMitra employs a dual-engine architecture:

1. **Deterministic Guardrails & Statutory Registry (Rules)**:
   - **Grounded Statutory Whitelist**: Hardcoded provisions from the *Indian Contract Act, 1872 (Sec 73 & 74)*, *Model Tenancy Act, 2021 (Sec 11 & 15)*, and the *Limitation Act, 1963 (3-year limit)*.
   - **Anti-Hallucination Citation Filter**: Scans generated drafts using regex. Any fabricated Supreme Court citation (e.g. *"Sharma v. State of Karnataka, 2018 SC"*) is intercepted and stripped or replaced with verified statutory principles.
   - **Safety / Emergency Triage**: Detects physical threats, goons, assault, or forced lockouts, halting civil processing to immediately refer the citizen to emergency helplines (**Dial 112** / DLSA legal aid).

2. **AI Layer (LLM)**:
   - **Conversational Intake**: Parses informal Hinglish narratives (*"Bhaiya landlord ne 35k painting ka kaat liya"*).
   - **Evidence Gap Detection**: Pinpoints missing proof (e.g., lack of GST invoices from landlord, absence of move-in inventory).
   - **Landlord Negotiation Simulator**: Roleplays a stubborn Indian landlord and provides a live **Paralegal Tactical Advice Box** with copy-paste counter-replies.

3. **Unit Economics & Scale**:
   - A full consultation (Intake + Standing + Notice + 3 Roleplay turns) uses **~3,800 tokens**.
   - Cost on Gemini 1.5 Flash is **~$0.0019 USD (< ₹0.16 INR)** per case.

---

## 🚀 Quickstart Guide

### 1. Installation
Clone the repository and install the lightweight requirements:
```bash
git clone <repo_url>
cd KUku
pip install -r requirements.txt
```

### 2. Run Batch Test Suite & Verify Raw Outputs
Run the automated test runner across all 5 realistic Indian dispute cases:
```bash
python3 scripts/run_eval.py
```
This validates all guardrails, executes limitation checks, and outputs unedited logs into `raw_outputs/`.

### 3. Launch Interactive Web App (Streamlit)
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 📁 Repository Structure
```
KUku/
├── app.py                      # Interactive multi-tab Streamlit web application
├── core/
│   ├── tenancy_law.py          # Grounded statutory registry (Contract Act, MTA, Wear & Tear)
│   ├── guardrails.py           # Anti-hallucination filter, limitation audit & safety triage
│   ├── intake_engine.py        # Messy Hinglish/English parser -> structured facts & timeline
│   ├── standing_evaluator.py   # Tenant leverage score (0-100%) & deduction legality audit
│   ├── notice_generator.py     # 15-day statutory legal demand notice generator
│   └── negotiation_coach.py    # Interactive landlord roleplay & tactical coaching arena
├── test_cases/                 # 5 realistic test cases (Bangalore, Pune, Gurgaon, Mumbai, Noida)
├── raw_outputs/                # Unedited raw logs from batch execution
│   ├── run_case_01.txt         # Bengaluru 35k painting scam
│   ├── run_case_02.txt         # Pune ghosting landlord
│   ├── run_case_03.txt         # Gurgaon notice dispute
│   ├── run_case_04.txt         # Mumbai monsoon seepage
│   └── run_case_05.txt         # Adversarial physical threat (emergency triage)
├── scripts/
│   ├── run_eval.py             # Batch evaluation runner
│   └── generate_pdf_doc.py     # Script to compile the 2-page solution PDF
├── docs/
│   ├── solution_doc.md         # Full solution document text (5 evaluation lenses)
│   └── solution_doc.pdf        # Formatted 2-page submission PDF
├── requirements.txt
└── README.md
```

---

## 📊 Evaluation Summary

| Case ID | Scenario | Result | Tenant Leverage |
|---|---|---|---|
| **CASE-01** | Bengaluru: ₹35k deducted for painting without bills | **PASS** | 95 / 100 (Strong) |
| **CASE-02** | Pune: Landlord ghosting after handover (50 days) | **PASS** | 95 / 100 (Strong) |
| **CASE-03** | Gurgaon: Notice dispute (written 1 mo vs oral 2 mo) | **PASS** | 75 / 100 (Moderate) |
| **CASE-04** | Mumbai: Seepage & 8-yr geyser wear blamed on tenant | **PASS** | 95 / 100 (Strong) |
| **CASE-05** | Noida: Landlord sent goons, threatened violence | **PASS (Triage Intercept)** | N/A (Emergency 112) |

---

## 🔍 Honest Failure Modes (Where the tool struggles)
1. **Cash-Only Oral Leases**: Without banking trails or written contracts, legal leverage drops significantly.
2. **Co-Mingled Genuine Damage**: When a tenant causes genuine damage but the landlord inflates the quote 5x, on-site physical inspection is needed to verify true repair quotes.
3. **State Court Specifics**: Regional procedural nuances (e.g. Maharashtra Rent Control vs Karnataka Rent Act) require local advocate filing if summary suits are contested.
