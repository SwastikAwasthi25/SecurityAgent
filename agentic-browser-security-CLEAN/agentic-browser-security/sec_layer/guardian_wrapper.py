from models.guardian_llm import GuardianLLM


class GuardianWrapper:
    def __init__(self):
        self.model = GuardianLLM()

    def analyze(self, content: str):
        structured_prompt = f"""
You are a browser security model.

Analyze the following content.

Respond ONLY in this exact format:

VERDICT: MALICIOUS or BENIGN
REASON: one short sentence

Do not repeat the input.
Do not add anything else.

Content:
{content}
"""

        response = self.model.generate(structured_prompt)

        verdict = "UNKNOWN"
        response_upper = response.upper()

        if "VERDICT: MALICIOUS" in response_upper:
            verdict = "MALICIOUS"
        elif "VERDICT: BENIGN" in response_upper:
            verdict = "BENIGN"

        return {
            "verdict": verdict,
            "raw_output": response.strip()
        }
