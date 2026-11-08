"""
DepositMitra - Grounded Indian Tenancy & Contract Law Knowledge Registry
Acts as the single source of truth to prevent hallucination of sections, acts, or fake case citations.
"""

from typing import Dict, Any, List

# Verified Statutes & Sections Whitelist
VERIFIED_STATUTES: Dict[str, Dict[str, Any]] = {
    "ICA_SEC_73": {
        "act": "Indian Contract Act, 1872",
        "section": "Section 73",
        "title": "Compensation for loss or damage caused by breach of contract",
        "summary": (
            "When a contract is broken, the party suffering is entitled to receive compensation "
            "for any loss naturally arising in the usual course of things. Unlawfully withholding a "
            "security deposit after vacant possession constitutes breach of contract, entitling the "
            "tenant to restitution plus interest."
        ),
        "interest_rate_precedent": "12% to 18% per annum from the date of wrongful withholding.",
        "verified": True
    },
    "ICA_SEC_74": {
        "act": "Indian Contract Act, 1872",
        "section": "Section 74",
        "title": "Compensation for breach of contract where penalty stipulated for",
        "summary": (
            "Courts disallow arbitrary penalty clauses in rental agreements. Even if an agreement specifies "
            "a flat forfeiture of deposit or automatic multi-month rent penalty without actual proof of "
            "proportional damage, it is deemed an unenforceable penalty."
        ),
        "verified": True
    },
    "MTA_SEC_11": {
        "act": "Model Tenancy Act, 2021",
        "section": "Section 11",
        "title": "Security Deposit Guidelines & Refund Timeline",
        "summary": (
            "Security deposit for residential premises shall not exceed 2 months' rent. The security deposit "
            "must be refunded to the tenant on the date of handing over vacant possession of the premises, "
            "or within a maximum of 30 days after adjusting only agreed arrears of rent and utility bills."
        ),
        "verified": True
    },
    "MTA_SEC_15": {
        "act": "Model Tenancy Act, 2021",
        "section": "Section 15 & Second Schedule",
        "title": "Division of Maintenance Responsibilities & Wear and Tear",
        "summary": (
            "Structural maintenance, periodic whitewashing/repainting, and major plumbing upkeep are "
            "the landlord's responsibility. Tenant is only responsible for routine cleanliness and repair "
            "of damages deliberately or negligently caused by tenant."
        ),
        "verified": True
    },
    "LIMITATION_ACT_ART_19_22": {
        "act": "Limitation Act, 1963",
        "section": "Article 19 & 22",
        "title": "Limitation Period for Recovery of Money / Debt",
        "summary": (
            "The statutory limitation period to initiate a civil suit or summary proceedings for recovery "
            "of an unpaid security deposit is 3 years from the date when the cause of action arose "
            "(i.e., date of vacating the premises or the date on which refund was formally due)."
        ),
        "period_years": 3,
        "verified": True
    },
    "CPA_SEC_35": {
        "act": "Consumer Protection Act, 2019",
        "section": "Section 35",
        "title": "Complaint before District Consumer Disputes Redressal Commission",
        "summary": (
            "Where residential tenancy includes bundled facility management, maintenance charges, or "
            "service agreements (especially in serviced apartments / managed co-living / society rentals), "
            "arbitrary withholding of caution money can be petitioned as 'Deficiency of Service' or "
            "'Unfair Trade Practice' via e-Daakhil without heavy court fees."
        ),
        "verified": True
    }
}

# Established Legal Principles on "Normal Wear and Tear"
WEAR_AND_TEAR_RULES = {
    "painting": {
        "classification": "Landlord Capital Maintenance",
        "legal_status": "UNLAWFUL_DEDUCTION_BY_DEFAULT",
        "explanation": (
            "Repainting due to normal passage of time, sunlight fading, minor scuffs, and ordinary domestic use "
            "falls under 'Normal Wear & Tear'. Under Indian tenancy norms, a landlord cannot unilaterally deduct "
            "a flat ₹20,000-₹50,000 for repainting unless: (1) The tenant deliberately painted walls in bizarre unauthorized "
            "colors, (2) Deep structural gouges exist, or (3) The landlord provides genuine GST invoices of painting costs "
            "and pre-existing move-in condition photos demonstrating tenant-specific damage."
        )
    },
    "deep_cleaning": {
        "classification": "Turnover Operational Expense",
        "legal_status": "CONTESTABLE_WITHOUT_RECEIPTS",
        "explanation": (
            "If the tenant leaves the flat swept and broom-clean, professional deep-cleaning charges for the incoming "
            "tenant are the landlord's turnover costs. Deducting ₹5,000-₹15,000 without sharing an actual service invoice "
            "or prior written agreement is legally contestable."
        )
    },
    "fixtures_and_seepage": {
        "classification": "Structural / Aging Maintenance",
        "legal_status": "LANDLORD_OBLIGATION",
        "explanation": (
            "Internal wall seepage, pre-existing plumbing leaks, aging geyser heating coils, and standard silicon wear "
            "around sanitary ware are structural maintenance obligations of the property owner under Section 15 of MTA "
            "and cannot be charged to a vacating tenant."
        )
    },
    "notice_period_deductions": {
        "classification": "Contractual Rent vs Penalty",
        "legal_status": "CONDITIONAL_ON_CONTRACT",
        "explanation": (
            "If the tenant served the contractually required notice (usually 30 days) via WhatsApp or email, "
            "the landlord has no legal right to withhold deposit citing 'sudden vacancy'. If no notice was given, "
            "the landlord may deduct actual rent for the shortfall period, but cannot forfeit the entire deposit as a penalty."
        )
    }
}

# Grievance Portals and Escalation Avenues
ESCALATION_FORUMS: List[Dict[str, str]] = [
    {
        "channel": "National Consumer Helpline (NCH)",
        "contact": "Toll Free: 1915 or consumerhelpline.gov.in",
        "cost": "Free",
        "relevance": "For co-living operators, managed rentals (e.g. Nestaway, Zolostays), or brokers withholding deposit."
    },
    {
        "channel": "e-Daakhil Portal (Consumer Commission)",
        "contact": "edaakhil.nic.in",
        "cost": "Minimal (₹0 to ₹500 fee depending on claim amount)",
        "relevance": "Online filing of consumer grievance for deficiency of service."
    },
    {
        "channel": "Small Causes Court / Summary Suit (Order 37 CPC)",
        "contact": "Local District Civil Court",
        "cost": "Nominal court fee based on state ad-valorem scale",
        "relevance": "Fast-track recovery of liquidated debt under contract where landlord has no bona fide defense."
    },
    {
        "channel": "District Legal Services Authority (DLSA)",
        "contact": "nalsa.gov.in / District Court Complex",
        "cost": "100% Free Legal Aid & Pre-Litigation Mediation",
        "relevance": "Free mediation where a judge/mediator summons the landlord to settle amicably without lawyer fees."
    }
]
