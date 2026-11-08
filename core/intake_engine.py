"""
DepositMitra - Case Intake Engine
Ingests colloquial Hinglish/English tenant complaints and extracts:
- Structured dispute metrics (deposit paid, amount withheld, monthly rent)
- Dates (move-in, move-out, notice served)
- Landlord deduction excuses
- Evidence checklist & missing critical proof
Supports both rule-based robust extraction and Gemini API LLM extraction.
"""

import re
import json
import os
from typing import Dict, Any, List

class IntakeEngine:
    @staticmethod
    def extract_case_facts(user_story: str, api_key: str = None) -> Dict[str, Any]:
        """
        Parses messy story into structured case facts.
        Attempts LLM extraction if API key is provided/available, else uses deterministic parser.
        """
        # If Gemini key is available, attempt intelligent LLM extraction
        gemini_key = api_key or os.environ.get("GEMINI_API_KEY")
        if gemini_key:
            try:
                extracted = IntakeEngine._extract_via_llm(user_story, gemini_key)
                if extracted:
                    return extracted
            except Exception as e:
                # Silently fallback to rule-based engine
                pass

        return IntakeEngine._extract_rule_based(user_story)

    @staticmethod
    def _extract_via_llm(user_story: str, api_key: str) -> Dict[str, Any]:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        
        # Try preferred fast models
        model_name = "gemini-1.5-flash"
        model = genai.GenerativeModel(model_name)
        
        prompt = f"""
        You are an expert Indian tenancy paralegal intake assistant.
        Analyze this tenant grievance story (which may be in English or Hinglish):
        \"\"\"{user_story}\"\"\"

        Extract and return STRICTLY a JSON object with this exact structure:
        {{
            "tenant_name": "Tenant Name if mentioned, else 'Tenant'",
            "landlord_name": "Landlord Name if mentioned, else 'Landlord'",
            "city": "City name (e.g. Bengaluru, Pune, Gurgaon, Mumbai) or 'India'",
            "monthly_rent": 0 (integer/float in INR, estimate from context or 0),
            "deposit_paid": 0 (integer/float total security deposit in INR),
            "amount_withheld": 0 (integer/float amount landlord refused to refund in INR),
            "move_in_date": "YYYY-MM-DD or DD/MM/YYYY or approximate",
            "move_out_date": "YYYY-MM-DD or DD/MM/YYYY or approximate",
            "rental_agreement_present": true/false,
            "notice_period_served": true/false,
            "move_out_inspection_done": true/false,
            "landlord_excuses": ["painting", "cleaning", "ghosting", etc.],
            "evidence_present": ["WhatsApp chats", "Bank statement", etc.],
            "missing_evidence": ["Move-in photos", "Written handover acknowledgment", etc.],
            "narrative_summary": "2-line clear summary of the core grievance"
        }}
        Do not output markdown ticks or explanation. Return ONLY the raw JSON string.
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
    def _extract_rule_based(text: str) -> Dict[str, Any]:
        """
        Deterministic regex and NLP-rule extraction for zero-dependency, 100% offline reliability.
        """
        lowered = text.lower()

        # Remove dates/years (e.g., 2020 to 2035) so calendar years are not confused with currency
        # Clean phrases like "october 2026", "in 2026", "year 2026", "2024", "2025", "2026"
        cleaned_for_amounts = re.sub(r"\b(19\d\d|20[2-3]\d)\b", "", lowered)

        # Context-aware extraction for specific keywords
        # 1. Deposit Paid
        dep_match = re.search(r"(?:deposit|advance|security)(?:\s+paid|\s+amount|\s+was|\s+of)?(?:\s+is|\s*:|\s*-)?\s*(?:rs\.?|inr|₹)?\s*(\d+(?:,\d+)*(?:\.\d+)?)\s*(k|thousand|lakh|lac)?", cleaned_for_amounts)
        # 2. Amount Withheld / Deducted
        withheld_match = re.search(r"(?:deducted|deduct|withheld|cut|kept|refused to return|holding)(?:\s+amount|\s+only)?(?:\s+is|\s*:|\s*-)?\s*(?:rs\.?|inr|₹)?\s*(\d+(?:,\d+)*(?:\.\d+)?)\s*(k|thousand|lakh|lac)?", cleaned_for_amounts)
        # 3. Monthly Rent
        rent_match = re.search(r"(?:rent)(?:\s+was|\s+is|\s+of)?(?:\s*:|\s*-)?\s*(?:rs\.?|inr|₹)?\s*(\d+(?:,\d+)*(?:\.\d+)?)\s*(k|thousand|lakh|lac)?", cleaned_for_amounts)

        def parse_val(m):
            if not m:
                return None
            val_clean = m.group(1).replace(",", "")
            try:
                num = float(val_clean)
                unit = m.group(2)
                if unit in ["k", "thousand"]:
                    num *= 1000
                elif unit in ["lakh", "lac"]:
                    num *= 100000
                return num
            except ValueError:
                return None

        ctx_dep = parse_val(dep_match)
        ctx_withheld = parse_val(withheld_match)
        ctx_rent = parse_val(rent_match)

        # Fallback regex for all amounts
        amount_matches = re.findall(r"(?:rs\.?|inr|₹)?\s*(\d+(?:,\d+)*(?:\.\d+)?)\s*(k|thousand|lakh|lac)?", cleaned_for_amounts)
        extracted_nums = []
        for val_str, unit in amount_matches:
            val_clean = val_str.replace(",", "")
            try:
                num = float(val_clean)
                if unit == "k" or unit == "thousand":
                    num *= 1000
                elif unit in ["lakh", "lac"]:
                    num *= 100000
                # Filter out small integers like day of month (e.g. 1st, 14, 31)
                if num >= 1000:
                    extracted_nums.append(num)
            except ValueError:
                continue

        deposit_paid = ctx_dep or (max(extracted_nums) if extracted_nums else 50000.0)
        
        if ctx_withheld:
            amount_withheld = ctx_withheld
        elif len(extracted_nums) >= 2:
            # Pick the second largest or the remainder
            remaining = [n for n in extracted_nums if n < deposit_paid]
            amount_withheld = max(remaining) if remaining else min(extracted_nums)
        else:
            amount_withheld = deposit_paid

        monthly_rent = ctx_rent or 25000.0

        # Extract City
        city = "Bengaluru"
        cities = ["bengaluru", "bangalore", "pune", "gurgaon", "gurugram", "noida", "delhi", "mumbai", "hyderabad", "chennai", "kolkata"]
        for c in cities:
            if c in lowered:
                city = c.capitalize()
                if city == "Bangalore":
                    city = "Bengaluru"
                break

        # Detect excuses
        excuses = []
        if any(w in lowered for w in ["paint", "painting", "whitewash", "colour"]):
            excuses.append("Painting Charges")
        if any(w in lowered for w in ["deep clean", "deep cleaning", "cleaning charges", "cleaning cost"]):
            excuses.append("Deep Cleaning Charges")
        if any(w in lowered for w in ["ghost", "not pick", "not answering", "blocked", "call cut", "phone off", "not responding"]):
            excuses.append("Landlord Unresponsive / Ghosting")
        if any(w in lowered for w in ["shortfall", "sudden vacancy", "lockin", "lock-in", "no notice", "without notice"]):
            excuses.append("Notice Period Shortfall / Lock-in Dispute")
        if any(w in lowered for w in ["tap", "geyser", "seepage", "repair", "broken", "damage", "fixtures"]):
            excuses.append("Property Damage / Fixture Repair")
        if not excuses:
            excuses.append("Unexplained Withholding")

        # Detect Agreement & Notice
        has_agreement = not any(w in lowered for w in ["no agreement", "bina agreement", "without agreement", "oral lease"])
        notice_served = any(w in lowered for w in ["gave notice", "served notice", "1 month notice", "informed earlier", "notified"])

        # Detect Evidence
        evidence = []
        if any(w in lowered for w in ["whatsapp", "chat", "message", "msg"]):
            evidence.append("WhatsApp Chat History")
        if any(w in lowered for w in ["upi", "bank", "statement", "gpay", "neft", "transfer"]):
            evidence.append("Bank Transfer / UPI Payment Proof")
        if any(w in lowered for w in ["photo", "photos", "video", "pic", "pics"]):
            evidence.append("Move-out Handover Photos/Videos")
        if not evidence:
            evidence.append("Bank Transfer Record of Initial Deposit")

        # Missing critical evidence
        missing = []
        if "Move-out Handover Photos/Videos" not in evidence:
            missing.append("Date-stamped photos/videos of flat condition at time of key handover")
        if not has_agreement:
            missing.append("Formal signed rental agreement (oral lease is harder to substantiate)")
        missing.append("Itemized GST tax invoices from landlord justifying repair/painting costs")
        missing.append("Written move-in condition inventory signed by both parties")

        # Extract names if present
        landlord_name = "Landlord"
        tenant_name = "Tenant"

        # Look for phrases like "landlord Venkat Rao", "owner Suresh", "Mr. Sharma"
        landlord_match = re.search(r"(?:landlord|owner|lessor)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)", text)
        if landlord_match:
            landlord_name = landlord_match.group(1).strip()

        # Look for move out dates like "31st October 2026", "15th August"
        date_match = re.search(r"(\d{1,2}(?:st|nd|rd|th)?\s+(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)(?:\s+\d{4})?)", text, re.IGNORECASE)
        move_out_date = date_match.group(1) if date_match else "30 days ago"

        return {
            "tenant_name": tenant_name,
            "landlord_name": landlord_name,
            "city": city,
            "monthly_rent": monthly_rent,
            "deposit_paid": deposit_paid,
            "amount_withheld": amount_withheld,
            "move_in_date": "1 year ago",
            "move_out_date": move_out_date,
            "rental_agreement_present": has_agreement,
            "notice_period_served": notice_served,
            "move_out_inspection_done": True,
            "landlord_excuses": excuses,
            "evidence_present": evidence,
            "missing_evidence": missing,
            "narrative_summary": f"Landlord {landlord_name} in {city} is unlawfully withholding ₹{amount_withheld:,.0f} out of ₹{deposit_paid:,.0f} deposit citing {', '.join(excuses)}."
        }
