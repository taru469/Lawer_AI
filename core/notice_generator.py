"""
DepositMitra - Formal Legal Demand Notice Generator
Drafts an authentic, professionally structured 15-Day Statutory Legal Demand Notice
governed strictly by verified Indian Contract and Tenancy Law.
"""

from datetime import date
from typing import Dict, Any

class NoticeGenerator:
    @staticmethod
    def generate_notice(case_facts: Dict[str, Any], evaluation: Dict[str, Any]) -> str:
        """
        Builds a formal 15-Day Legal Demand Notice based on facts and evaluation.
        """
        today_str = date.today().strftime("%d %B %Y")
        tenant = case_facts.get("tenant_name", "Tenant")
        landlord = case_facts.get("landlord_name", "Landlord")
        city = case_facts.get("city", "Bengaluru")
        deposit_paid = case_facts.get("deposit_paid", 50000.0)
        withheld_amt = case_facts.get("amount_withheld", 30000.0)
        move_in = case_facts.get("move_in_date", "the commencement date")
        move_out = case_facts.get("move_out_date", "the handover date")
        excuses = ", ".join(case_facts.get("landlord_excuses", ["arbitrary deductions"]))

        notice_text = f"""
================================================================================
                           LEGAL DEMAND NOTICE
               (ISSUED UNDER SECTION 73 OF THE INDIAN CONTRACT ACT, 1872
                  AND PROVISIONS OF THE MODEL TENANCY FRAMEWORK)
================================================================================

DATE: {today_str}

TO:
{landlord} (Property Owner / Lessor)
Premises located at: {city}, India

FROM:
{tenant} (Former Lessee / Tenant)
Contact / Email: [Insert Your Email & Phone Number]

SUBJECT: FORMAL DEMAND NOTICE FOR UNLAWFUL WITHHOLDING OF SECURITY DEPOSIT 
         AMOUNTING TO RS. {withheld_amt:,.2f} IN RESPECT OF RESIDENTIAL LEASE 
         AT {city.upper()}

Sir / Madam,

Under instructions and on behalf of my client/myself, {tenant}, residing formerly at the aforementioned residential premises, I hereby serve upon you this formal Statutory Legal Demand Notice:

1. FACTUAL MATRIX & COMMENCEMENT OF TENANCY:
   That I entered into possession of the residential premises situated at {city} on {move_in}. In accordance with the terms of the tenancy, I duly paid an advance refundable security deposit amounting to Rs. {deposit_paid:,.2f} (Rupees {int(deposit_paid):,} only) via verifiable banking channels, which was acknowledged and received by you.

2. LAWFUL VACATION & VACANT HANDOVER:
   That upon due completion of the tenancy term and after serving requisite notice, I lawfully vacated and handed over vacant, peaceful, and unencumbered physical possession of the said premises to you on {move_out}. At the time of handover, the premises were left in broom-clean, orderly condition with all utilities fully cleared.

3. UNLAWFUL RETENTION & ARBITRARY DEDUCTIONS:
   That despite having resumed full physical possession of the premises, you have failed and neglected to refund the balance refundable security deposit of Rs. {withheld_amt:,.2f}. Instead, you have unilaterally cited deductions under the pretext of "{excuses}". 

4. LEGAL POSITION & NORMAL WEAR AND TEAR:
   (a) Normal Wear & Tear Exception: Under settled Indian tenancy jurisprudence and Section 15 of the Model Tenancy framework, expenses for periodic repainting, minor wall fading, and ordinary weathering constitute 'Normal Wear and Tear', which is the sole capital maintenance obligation of the property owner.
   (b) Absence of Itemized Proof: You have failed to furnish any verified third-party GST tax invoices, pre-existing move-in condition inventories, or legitimate damage assessments to substantiate any deductions.
   (c) Statutory Refund Norms: Under Section 11 of the Model Tenancy Act, a landlord is obligated to refund the security deposit within 30 days of receiving vacant possession. Unjustified detention of client funds constitutes unjust enrichment.
   (d) Breach of Contract: Your arbitrary withholding is a direct breach of contract under Section 73 of the Indian Contract Act, 1872, rendering you liable to pay damages and restitution with interest. Furthermore, any unilateral forfeiture clause is void as an unenforceable penalty under Section 74 of the Indian Contract Act.

5. PEREMPTORY DEMAND (15 DAYS NOTICE):
   I hereby formally call upon you to remit the lawfully due security deposit sum of Rs. {withheld_amt:,.2f} (Rupees {int(withheld_amt):,} only) directly into my designated bank account within FIFTEEN (15) DAYS from the date of receipt of this notice, failing which I shall be constrained to initiate formal legal proceedings against you.

6. CONSEQUENCES OF NON-COMPLIANCE:
   Should you fail to comply with this demand within the stipulated 15-day period:
   (a) I shall institute a Summary Civil Suit under Order 37 of the Code of Civil Procedure, 1908 before the competent Court of Small Causes for recovery of liquidated debt, claiming interest @ 18% per annum from the date of default until realization.
   (b) I shall lodge a formal grievance before the District Consumer Disputes Redressal Commission (via e-Daakhil) and the National Consumer Helpline for deficiency in service and unfair trade practice.
   (c) In such event, you shall be held solely responsible for all litigation costs, advocate fees, and incidental expenses incurred by me.

Please treat this as a final opportunity to resolve this matter amicably without litigation.

Yours faithfully,

_____________________________
{tenant}
Former Lessee / Tenant

DISPATCH INSTRUCTIONS FOR TENANT:
1. Send a physical copy via Registered Post with Acknowledgment Due (RPAD) or Speed Post to create unshakeable court-admissible postal proof.
2. Simultaneously send this PDF copy via WhatsApp and Registered Email to the landlord.
================================================================================
"""
        return notice_text.strip()
