"""
DepositMitra - Landlord Negotiation Simulator & Coaching Arena
Enables tenants to practice confronting the opposing landlord before real-world interaction.
Features:
- Realistic Indian landlord persona (evasion, intimidation, fake excuses)
- Tactical coaching tips after each turn (leverage analysis, counter-response suggestions)
Works both offline (scripted branching) and online (dynamic LLM).
"""

import os
from typing import Dict, Any, List

OFFLINE_LANDLORD_PERSONAS = [
    {
        "trigger": ["paint", "painting", "colour", "wall"],
        "landlord_reply": (
            "Look, the flat was given fresh. When you left, walls had marks. "
            "In Bangalore/Pune, standard deduction for 2BHK repainting is 25,000 to 30,000. "
            "It is written in our rental agreement that 1 month rent or painting charges will be deducted. "
            "I cannot refund this."
        ),
        "tactic_analysis": "Landlord is relying on a standard boiler-plate clause to charge turnover maintenance as tenant damage.",
        "recommended_counter": (
            "\"Under Section 74 of the Indian Contract Act and Model Tenancy guidelines, arbitrary penalty clauses "
            "are legally invalid without proof of actual structural damage. Sunlight fading and minor scuffs are 'Normal Wear & Tear'. "
            "Please share the contractor's GST invoice and move-in comparison photos within 48 hours, or refund the full amount.\""
        )
    },
    {
        "trigger": ["notice", "1 month", "shortfall", "vacate"],
        "landlord_reply": (
            "You gave notice very late. I couldn't find a new tenant and lost rent for this month. "
            "Therefore I am adjusting the deposit against my vacancy loss. You can't just leave whenever you want."
        ),
        "tactic_analysis": "Landlord is shifting vacancy risk onto you despite lawful notice being served.",
        "recommended_counter": (
            "\"I have timestamped WhatsApp and email records showing I served the contractually required notice on [Date]. "
            "Once valid notice is completed and keys are handed over, you cannot hold deposit for your failure to find a new tenant. "
            "Please transfer the balance immediately.\""
        )
    },
    {
        "trigger": ["court", "police", "legal", "lawyer", "notice"],
        "landlord_reply": (
            "You want to send legal notice? Go ahead, do whatever you want! "
            "Do you know how long Indian courts take? 5 years! You will spend 40,000 on advocate fees to recover 30,000. "
            "Be practical and take 5,000 as final settlement."
        ),
        "tactic_analysis": "Classic intimidation tactic. Landlords count on tenants assuming civil courts are slow and expensive.",
        "recommended_counter": (
            "\"I do not need expensive litigation. A Summary Suit under Order 37 CPC in Small Causes Court is fast-tracked "
            "for undisputed debt, where the judge decrees full amount plus 18% interest and makes the losing party bear "
            "all court fees. Furthermore, filing on e-Daakhil / National Consumer Helpline costs zero rupees. Let us avoid this.\""
        )
    },
    {
        "trigger": ["money", "funds", "next month", "delay", "wait"],
        "landlord_reply": (
            "Right now I am having financial trouble. My daughter's college fees and medical expenses came up. "
            "Wait until the new tenant gives me deposit next month, then I will see."
        ),
        "tactic_analysis": "Landlord spent your deposit as personal income instead of maintaining it as an escrow caution deposit.",
        "recommended_counter": (
            "\"A security deposit is trust money held in custody, not a personal loan. Under Section 11 of the Model Tenancy Act, "
            "refund is mandatory upon handing over vacant possession. Delaying payment incurs statutory interest @ 18% p.a. "
            "Please arrange the transfer by this Friday.\""
        )
    }
]

class NegotiationCoach:
    @staticmethod
    def simulate_turn(tenant_message: str, history: List[Dict[str, str]], api_key: str = None) -> Dict[str, Any]:
        """
        Generates landlord reply and tactical tenant coaching.
        """
        gemini_key = api_key or os.environ.get("GEMINI_API_KEY")
        if gemini_key:
            try:
                return NegotiationCoach._simulate_via_llm(tenant_message, history, gemini_key)
            except Exception:
                pass

        return NegotiationCoach._simulate_rule_based(tenant_message)

    @staticmethod
    def _simulate_via_llm(tenant_message: str, history: List[Dict[str, str]], api_key: str) -> Dict[str, Any]:
        import google.generativeai as genai
        import json
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        history_context = "\n".join([f"{h['role']}: {h['content']}" for h in history[-4:]])
        
        prompt = f"""
        You are a simulator for tenant-landlord disputes in urban India (Bangalore/Pune/Delhi/Gurgaon).
        Current conversation history:
        {history_context}
        
        Tenant says: "{tenant_message}"
        
        Generate a JSON response with:
        1. "landlord_reply": A realistic response from an Indian landlord who is defensive, reluctant to return money, makes excuses (painting costs, deep cleaning, vacancy loss, or court delays).
        2. "tactic_analysis": 1-2 lines explaining what psychological or legal bluff the landlord is using.
        3. "recommended_counter": A crisp, polite, legally assertive reply the tenant can use citing Indian law (Section 73 Contract Act, Normal wear & tear, Order 37 CPC summary suit, or 18% interest).
        
        Return STRICTLY raw JSON.
        """
        response = model.generate_content(prompt)
        text = response.text.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        return json.loads(text.strip())

    @staticmethod
    def _simulate_rule_based(tenant_message: str) -> Dict[str, Any]:
        lowered = tenant_message.lower()
        for persona in OFFLINE_LANDLORD_PERSONAS:
            if any(t in lowered for t in persona["trigger"]):
                return {
                    "landlord_reply": persona["landlord_reply"],
                    "tactic_analysis": persona["tactic_analysis"],
                    "recommended_counter": persona["recommended_counter"]
                }
        
        # Default fallback
        return {
            "landlord_reply": (
                "Look, you stayed there for over a year. There are cleaning expenses and minor maintenance. "
                "I am already adjusting very reasonably. If I give everything back, who will pay the painter?"
            ),
            "tactic_analysis": "Landlord is conflating routine post-tenancy preparation with tenant-caused damage.",
            "recommended_counter": (
                "\"Repainting and routine turnover cleaning are the landlord's operational expenses under Section 15 of MTA. "
                "Unless there is deliberate structural breakage substantiated by GST bills and move-in photos, "
                "deductions are legally unviable. Please send the itemized bills or refund the balance within 3 days.\""
            )
        }
