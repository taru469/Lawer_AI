"""
DepositMitra - Legal Standing & Leverage Evaluator
Calculates tenant leverage score (0-100%), audits deduction legality,
and provides plain-language strategic guidance.
"""

from typing import Dict, Any, List
from core.tenancy_law import VERIFIED_STATUTES, WEAR_AND_TEAR_RULES

class StandingEvaluator:
    @staticmethod
    def evaluate(case_facts: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evaluates the tenant's legal position based on structured facts.
        """
        score = 50  # Baseline

        # Scoring adjustments
        positives = []
        negatives = []

        if case_facts.get("rental_agreement_present", True):
            score += 15
            positives.append("Written rental agreement exists, establishing clear contractual obligations.")
        else:
            score -= 20
            negatives.append("No written rental agreement; reliant on banking records and WhatsApp chat proof.")

        evidence = case_facts.get("evidence_present", [])
        if any("bank" in e.lower() or "upi" in e.lower() for e in evidence):
            score += 15
            positives.append("Clear digital banking trail for initial security deposit payment.")

        if case_facts.get("notice_period_served", False):
            score += 15
            positives.append("Notice period was duly communicated, eliminating sudden vacancy penalty.")
        
        # Deduction analysis
        excuses = case_facts.get("landlord_excuses", [])
        deduction_audit = []

        for excuse in excuses:
            excuse_lower = excuse.lower()
            if "paint" in excuse_lower:
                score += 10  # High tenant leverage because painting is normal wear & tear
                deduction_audit.append({
                    "item": excuse,
                    "status": "UNLAWFUL DEDUCTION",
                    "reasoning": (
                        "Repainting falls under 'Normal Wear and Tear'. Under Indian tenancy jurisprudence, "
                        "landlords cannot charge a departing tenant for periodic repainting unless gross intentional damage "
                        "is documented with pre-existing move-in inspection proof and valid GST invoices."
                    ),
                    "governing_law": "Model Tenancy Act 2021 (Sec 15) & Indian Contract Act (Sec 73)"
                })
            elif "clean" in excuse_lower:
                score += 5
                deduction_audit.append({
                    "item": excuse,
                    "status": "HIGHLY CONTESTABLE",
                    "reasoning": (
                        "Standard deep-cleaning is a turnover expense. If the apartment was handed over broom-clean, "
                        "the landlord cannot unilaterally deduct funds without an agreed clause and actual tax receipt."
                    ),
                    "governing_law": "Principles of Restitution & Section 73 ICA"
                })
            elif "ghost" in excuse_lower:
                score += 10
                deduction_audit.append({
                    "item": excuse,
                    "status": "ILLEGAL RETENTION",
                    "reasoning": (
                        "Ceasing communication after receiving keys constitutes willful withholding of client funds. "
                        "The tenant is entitled to claim 18% annual interest on delayed sums."
                    ),
                    "governing_law": "Section 11 Model Tenancy Act & Section 73 Indian Contract Act"
                })
            elif "notice" in excuse_lower or "lock" in excuse_lower:
                score -= 5
                deduction_audit.append({
                    "item": excuse,
                    "status": "SCRUTINY REQUIRED",
                    "reasoning": (
                        "If notice period was disputed, landlord can only offset actual days of notice shortfall, "
                        "not forfeit the entire security deposit. Penalty clauses without actual damages are void under Sec 74 ICA."
                    ),
                    "governing_law": "Section 74 Indian Contract Act (Penalty clauses unenforceable)"
                })
            else:
                deduction_audit.append({
                    "item": excuse,
                    "status": "CONTESTABLE",
                    "reasoning": "Unsubstantiated withholding requires itemized proof and receipts from the landlord.",
                    "governing_law": "Section 73 Indian Contract Act"
                })

        score = max(10, min(95, score))

        # Plain language summary
        if score >= 75:
            verdict = "STRONG LEGAL LEVERAGE (HIGH)"
            summary = (
                "You have strong legal standing. The landlord's deductions appear to violate standard "
                "wear-and-tear principles and statutory deposit return norms. A formal 15-day Legal Demand Notice "
                "places severe legal and financial pressure on them to settle."
            )
        elif score >= 50:
            verdict = "MODERATE TO GOOD LEVERAGE"
            summary = (
                "You have a solid case to recover the majority of your withheld deposit. While there may be minor "
                "points of contention (such as utility adjustments or notice clarification), the landlord cannot "
                "legally retain your funds without verified GST receipts."
            )
        else:
            verdict = "DOCUMENTATION DEFICIENT"
            summary = (
                "Your case requires additional substantiation (e.g. locating UPI receipts, chat backups, or handover photos). "
                "Even without an agreement, banking records can prove the deposit was non-gratuitous."
            )

        # Strategic roadmap
        action_plan = [
            {
                "step": 1,
                "title": "Serve Formal 15-Day Statutory Legal Demand Notice",
                "description": "Send a formal notice via Registered Post AD and WhatsApp citing Section 73 ICA and 18% p.a. interest."
            },
            {
                "step": 2,
                "title": "Pre-Litigation Mediation via DLSA / NCH",
                "description": "If unresolved after 15 days, lodge a free grievance on the National Consumer Helpline (1915) or approach the District Legal Services Authority (DLSA) for free summons-based mediation."
            },
            {
                "step": 3,
                "title": "Summary Suit under Order 37 CPC / Rent Tribunal",
                "description": "File a fast-track summary suit in Small Causes Court for recovery of liquidated debt. The landlord will bear full legal costs upon losing."
            }
        ]

        return {
            "leverage_score": score,
            "verdict": verdict,
            "summary": summary,
            "positives": positives,
            "negatives": negatives,
            "deduction_audit": deduction_audit,
            "action_plan": action_plan
        }
