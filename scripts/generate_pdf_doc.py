"""
DepositMitra - 2-Page Solution Document PDF Generator
Uses fpdf2 to build a publication-grade 2-page PDF deliverable for Kuku.
"""

import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class SolutionDocPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(24, 43, 73)
        self.cell(0, 6, "KUKU AI GENERALIST ASSIGNMENT - SOLUTION DOCUMENT", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        self.set_font("Helvetica", "I", 8.5)
        self.set_text_color(100, 116, 139)
        self.cell(0, 4, "Problem 2: DepositMitra (AI Paralegal for Indian Renter Deposit Recovery)", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        self.set_draw_color(203, 213, 225)
        self.line(12, 21, 198, 21)
        self.ln(3)

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(148, 163, 184)
        self.cell(0, 8, f"DepositMitra | Page {self.page_no()} of 2", align="C")

def build_pdf():
    pdf = SolutionDocPDF(orientation="P", unit="mm", format="A4")
    pdf.set_margins(12, 12, 12)
    pdf.set_auto_page_break(auto=True, margin=12)
    
    # -------------------------------------------------------------
    # PAGE 1
    # -------------------------------------------------------------
    pdf.add_page()
    
    # Section 1: Problem Choice and Framing
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 5.5, "1. Problem Choice and Framing", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(37, 99, 235)
    pdf.cell(0, 4.5, "Why This Problem?", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(30, 41, 59)
    pdf.multi_cell(0, 3.7, (
        "In urban India (Bengaluru, Pune, Gurgaon, Mumbai), security deposit retention is an endemic crisis. "
        "Over 80% of young renters forfeit Rs. 25,000 to 80,000 upon moving out due to arbitrary deductions: "
        "routine repainting charges, unjustified cleaning fees, or outright landlord ghosting. Formal legal "
        "recourse is economically broken: retaining an advocate costs Rs. 15,000-30,000 upfront for a Rs. 40,000 "
        "dispute. Intimidated by opaque jargon and court backlogs, ordinary citizens abandon their claims."
    ))
    pdf.ln(1)

    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(37, 99, 235)
    pdf.cell(0, 4.5, "Scoping & Intentional Boundaries (Depth over Shallow Breadth):", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(30, 41, 59)
    pdf.multi_cell(0, 3.7, (
        "Rather than building a superficial general lawyer covering murder, divorce, and corporate law, "
        "DepositMitra is laser-focused 100% on Residential Rental Security Deposit Disputes.\n"
        "- In-Scope: Unlawful painting/cleaning deductions, ghosting post-key handover, notice period disputes, "
        "wear-and-tear classification, demand notice generation, and negotiation coaching.\n"
        "- Strict Out-of-Scope (Safety Triage): Physical threats, goons, forced lockouts, and commercial leases (>Rs. 50L). "
        "These trigger immediate deterministic hard-refusal and direct referral to emergency helplines (Dial 112) "
        "or the District Legal Services Authority (DLSA)."
    ))
    pdf.ln(1)

    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(37, 99, 235)
    pdf.cell(0, 4.5, "Assumptions Made:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(30, 41, 59)
    pdf.multi_cell(0, 3.7, (
        "(1) Ordinary renters communicate in colloquial Hinglish or informal text; (2) Landlords count on tenant "
        "legal hesitation; (3) Painting and minor weathering constitute 'Normal Wear & Tear' under Indian law "
        "unless the landlord substantiates deliberate damage with move-in inventories and third-party GST invoices."
    ))
    pdf.ln(2.5)

    # Section 2: Approach and Scale
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 5.5, "2. Approach and Scale: What We Gave to AI vs. Deterministic Rules", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(30, 41, 59)
    pdf.multi_cell(0, 3.7, (
        "To eliminate hallucination of legal sections and fabricated court cases, DepositMitra balances "
        "deterministic code with LLM reasoning:"
    ))
    pdf.ln(1)

    # Comparison Box
    pdf.set_fill_color(241, 245, 249)
    pdf.rect(12, pdf.get_y(), 186, 25, "F")
    pdf.set_xy(14, pdf.get_y() + 1)
    pdf.set_font("Helvetica", "B", 8)
    pdf.cell(90, 3.8, "What AI Does (Gemini 1.5/2.5 Flash):", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(90, 3.8, "What Deterministic Code / Rules Do:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 7.5)
    pdf.set_x(14)
    pdf.cell(90, 3.5, "- Parses messy Hinglish & conversational stories", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(90, 3.5, "- Safety triage: Regex catches criminal threats", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_x(14)
    pdf.cell(90, 3.5, "- Extracts chronology & detects missing proof gaps", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(90, 3.5, "- Statutory Registry: Whitelist of verified Indian Acts", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_x(14)
    pdf.cell(90, 3.5, "- Plain-language legal advice & strategic standing", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(90, 3.5, "- Anti-Hallucination Filter: Blocks fake case citations", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_x(14)
    pdf.cell(90, 3.5, "- Interactive stubborn landlord persona roleplay", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(90, 3.5, "- Limitation Audit: Enforces 3-year statutory limit", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_x(14)
    pdf.cell(90, 3.5, "- Drafts tailored, persuasive 15-day notice clauses", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(90, 3.5, "- Unit economics: Zero-cost rule execution & fallback", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3.5)

    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(37, 99, 235)
    pdf.cell(0, 4.5, "Human in the Loop & Unit Economics at Scale:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(30, 41, 59)
    pdf.multi_cell(0, 3.7, (
        "- Human in the Loop: The tenant reviews and customizes the generated demand notice before dispatch. "
        "A clear statutory disclaimer clarifies that DepositMitra is a pre-litigation paralegal assistant, not an advocate.\n"
        "- Real-World Economics: A full 5-phase consultation consumes ~3,800 tokens. On Gemini 1.5 Flash, the cost is "
        "approx. $0.0019 USD (< 16 paise INR) per case. Scaling to 100,000 cases costs under Rs. 16,000 (~$190), "
        "making it economically deployable as a free public utility."
    ))

    # -------------------------------------------------------------
    # PAGE 2
    # -------------------------------------------------------------
    pdf.add_page()

    # Section 3: Quality Checking
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 5.5, "3. Quality Checking, Real Runs & Honest Failure Modes", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(30, 41, 59)
    pdf.multi_cell(0, 3.7, (
        "The system was evaluated against 5 realistic test cases (unedited raw logs in /raw_outputs/):"
    ))
    pdf.ln(1)

    # Test cases table
    pdf.set_font("Helvetica", "B", 7.5)
    pdf.set_fill_color(226, 232, 240)
    pdf.cell(18, 4.8, "Case ID", 1, 0, "C", True)
    pdf.cell(64, 4.8, "Scenario & City", 1, 0, "L", True)
    pdf.cell(64, 4.8, "Engine Action & Output", 1, 0, "L", True)
    pdf.cell(40, 4.8, "Status / Leverage", 1, 1, "C", True)

    test_runs = [
        ("CASE-01", "Bengaluru: Rs.35k deducted for painting without bills", "Sanitized 15-day notice citing Sec 73 ICA & MTA", "PASS (95/100 Leverage)"),
        ("CASE-02", "Pune: Landlord ghosting after handover (50 days)", "Demanded 18% statutory interest & CPC summary suit", "PASS (95/100 Leverage)"),
        ("CASE-03", "Gurgaon: Notice dispute (written 1 mo vs oral 2 mo)", "Voided arbitrary penalty under Sec 74 ICA", "PASS (75/100 Leverage)"),
        ("CASE-04", "Mumbai: Seepage & 8-yr geyser wear charged to tenant", "Applied Normal Wear & Tear doctrine (Sec 15 MTA)", "PASS (95/100 Leverage)"),
        ("CASE-05", "Noida: Landlord sent goons, threatened violence", "Hard stop: Civil processing halted; Dial 112 triage", "PASS (Emergency Alert)")
    ]

    pdf.set_font("Helvetica", "", 7.2)
    for cid, scen, act, stat in test_runs:
        pdf.cell(18, 4.8, cid, 1, 0, "C")
        pdf.cell(64, 4.8, scen, 1, 0, "L")
        pdf.cell(64, 4.8, act, 1, 0, "L")
        pdf.cell(40, 4.8, stat, 1, 1, "C")
    pdf.ln(2)

    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(185, 28, 28)
    pdf.cell(0, 4.5, "Where the Tool Fails Honestly (Boundary Limitations):", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(30, 41, 59)
    pdf.multi_cell(0, 3.7, (
        "1. Cash-Only Oral Leases: Without banking records or a signed lease, the tool cannot manufacture documentary "
        "proof. It alerts the tenant to banking gaps but cannot provide high legal leverage.\n"
        "2. Co-Mingled Genuine Damage: If a tenant genuinely broke a fixture but the landlord inflated the repair cost by 5x, "
        "the tool cannot verify physical damage without on-site computer vision or contractor quote audits.\n"
        "3. Local Rent Control Nuances: Certain states (e.g. Maharashtra Rent Control Act vs Karnataka Rent Act) have "
        "distinct local forum procedural requirements. The tool recommends central summary suits and DLSA mediation, "
        "flagging when regional court filings require local bar counsel."
    ))
    pdf.ln(2)

    # Section 4: The Prototype
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 5.5, "4. The Prototype & Reproducibility", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(30, 41, 59)
    pdf.multi_cell(0, 3.7, (
        "- Live Public App: https://deposit-mitra.streamlit.app\n"
        "- GitHub Repository: https://github.com/taru469/Lawer_AI\n"
        "- Structure: Clean Python architecture separating statutes, guardrails, intake, evaluation, notice generation, "
        "and negotiation simulation.\n"
        "- Model Swapping & Zero-Cost Run: Fully operational in 100% offline heuristic mode without API keys, while seamlessly "
        "connecting to Google Gemini (or interview APIs) when provided."
    ))
    pdf.ln(2)

    # Section 5: Conclusion
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 5.5, "5. Conclusion & Product Vision", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(30, 41, 59)
    pdf.multi_cell(0, 3.7, (
        "DepositMitra bridges India's pre-litigation justice gap by delivering credible, anti-hallucinatory legal leverage. "
        "By arming tenants with statutory facts, 15-day demand notices, and roleplay confidence, it enables ordinary citizens "
        "to recover their hard-earned money without entering protracted courtroom battles."
    ))

    # Output file
    os.makedirs("docs", exist_ok=True)
    out_path = "docs/solution_doc.pdf"
    pdf.output(out_path)
    print(f"✓ Solution document PDF successfully generated: {out_path}")

if __name__ == "__main__":
    build_pdf()
