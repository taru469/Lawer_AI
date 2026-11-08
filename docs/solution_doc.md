# DepositMitra: Pre-Litigation AI Paralegal for Indian Renter Security Deposit Recovery
**Candidate Solution Document | Kuku AI Generalist Assignment (Problem 2)**

---

### 1. Problem Choice and Framing
**Why This Problem?**  
In urban India (Bengaluru, Pune, Gurgaon, Mumbai, Hyderabad), security deposit retention is an endemic friction point. Over 80% of young working professionals and students forfeit ₹25,000–₹80,000 upon moving out due to arbitrary deductions: flat 1-month painting charges, unjustified "deep cleaning" fees, or outright landlord ghosting. Formal legal recourse is practically blocked: hiring an advocate requires ₹15,000–₹30,000 upfront, which is economically irrational for a ₹40,000 dispute. Intimidated by legal jargon and court delays, ordinary tenants give up.

**Scoping & Intentional Boundaries:**  
We chose depth over shallow breadth. Rather than building a generic "lawyer for all of India" that produces vague summaries across criminal, corporate, and family law, DepositMitra acts as a specialized **Pre-Litigation Citizen Paralegal** focused 100% on **Rental Security Deposit Disputes**.
- **In-Scope:** Unlawful painting/cleaning deductions, ghosting post-key handover, notice period disputes, wear-and-tear classification, demand notice generation, and negotiation coaching.
- **Strict Out-of-Scope (Automatic Safety Triage):** Physical violence, lockouts with force, criminal intimidation, and commercial property disputes (>₹50L). These trigger immediate hard-refusal and direct referral to emergency services (Dial 112) or the District Legal Services Authority (DLSA).

**Assumptions Made:**  
Where the brief was silent, we assumed: (1) Ordinary citizens communicate in colloquial Hinglish or fragmented English; (2) Landlords count on tenant legal ignorance; (3) Painting and minor weathering constitute "Normal Wear & Tear" under Indian jurisprudence unless the landlord proves deliberate damage with pre-existing move-in condition inventories and GST invoices.

---

### 2. Approach and Scale: AI vs. Deterministic Rules
To prevent unpredictable model failures, DepositMitra uses a dual-engine architecture balancing deterministic certainty with LLM flexibility:

```
[Messy User Story (Hinglish/English)] 
       │
       ▼
[Deterministic Guardrail] ──── (Threat / Out-of-Scope?) ────► [Emergency Refusal & Dial 112]
       │ (Safe)
       ▼
[AI Extraction Layer] ────────► Structured Facts, Timeline & Missing Evidence Gap Detector
       │
       ▼
[Statutory Knowledge Base] ───► Deterministic Whitelist (Contract Act Sec 73/74, MTA Sec 11/15)
       │
       ├──────────────────────► [Plain-Language Leverage Score (0-100%)]
       ├──────────────────────► [15-Day Statutory Legal Demand Notice + Sanitizer]
       └──────────────────────► [Opposing Party Roleplay Arena + Tactical Coaching]
```

- **What We Gave to AI:** Unstructured text understanding (deciphering Hinglish narratives like *"Bangalore landlord 35k cut kar liya"*), chronological fact extraction, dynamic demand notice personalization, and realistic landlord roleplay simulation.
- **What We Kept as Code & Deterministic Rules:**
  - *Safety Guardrail:* Regex pattern matcher for criminal intimidation and violence.
  - *Statutory Knowledge Registry:* Strict whitelist of verified Indian statutes (Sec 73 & 74 Indian Contract Act 1872; Sec 11 & 15 Model Tenancy Act; Limitation Act 1963).
  - *Anti-Hallucination Citation Filter:* Regex sanitizer that flags or strips any hallucinated Supreme Court citations or non-existent sections before displaying to the user.
  - *Limitation Period Calculator:* Mathematical date check enforcing the 3-year statutory limit under Article 19 & 22 of the Limitation Act, 1963.
- **Human in the Loop:** The tenant reviews, verifies, and edits the generated notice before dispatch. Clear disclaimers ensure users understand the tool provides pre-litigation paralegal assistance, not advocate representation.
- **Unit Economics & Scale:** A full 5-step consultation consumes ~3,800 tokens. On Gemini 1.5/2.5 Flash, cost is **~$0.0019 USD (< ₹0.16 INR)** per case, allowing nationwide deployment for less than the cost of a single postal stamp.

---

### 3. Quality Checking, Evaluation & Honest Failure Modes
We evaluated DepositMitra across 5 diverse test scenarios (logged unedited in `raw_outputs/`):

| Test Case | Scenario Description | Engine Result | Tenant Leverage |
|---|---|---|---|
| **CASE-01** | Bengaluru: ₹35k deducted for painting without GST bills | PASS (Sanitized Notice Generated) | 95 / 100 (Strong) |
| **CASE-02** | Pune: Landlord ghosting after key handover (50 days) | PASS (Statutory Interest Demanded) | 95 / 100 (Strong) |
| **CASE-03** | Gurgaon: Disputed notice period (written 1 mo vs oral 2 mo) | PASS (Penalty Clause Disallowed) | 75 / 100 (Moderate) |
| **CASE-04** | Mumbai: Monsoon wall seepage charged to tenant | PASS (Wear & Tear Doctrine Applied) | 95 / 100 (Strong) |
| **CASE-05** | Noida: Landlord sent goons, threatened violence | PASS (Civil Action Blocked; Emergency 112 Triage) | N/A (Emergency) |

**Where the Tool Struggles & Fails (Honest Limitations):**
1. **Cash-Only Oral Leases:** When a tenant has no written agreement and paid deposit in cash without UPI/bank records, the tool cannot create documentary leverage. It flags the deficiency but cannot manufacture proof.
2. **Co-Mingled Genuine Damage:** If the tenant genuinely cracked a marble slab or damaged an appliance, but the landlord overcharged 5x for the whole flat, the tool currently relies on self-reported facts. Without physical image inspection, it cannot audit true contractor repair quotes.
3. **Regional Tenancy Variations:** While grounded in central acts (Contract Act 1872 and Model Tenancy Act), local municipal rent control practices (e.g., West Bengal Premises Tenancy Act or legacy Mumbai Pagdi systems) have idiosyncratic procedural quirks that require certified local advocate intervention.

---

### 4. The Prototype
- **Tech Stack:** Python 3.12, Streamlit 1.40+, Google Gemini API (with 100% offline fallback), `fpdf2`.
- **How to Run:**
  ```bash
  git clone <repo_url> && cd KUku
  pip install -r requirements.txt
  streamlit run app.py
  ```
- **Live Capabilities:** Interactive case intake with quick presets, visual leverage meter, editable 15-day statutory notice with download, live landlord confrontation simulator with paralegal tactical counter-replies, and real-time guardrail verification inspector.
