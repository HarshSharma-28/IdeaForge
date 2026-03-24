import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_KEY = os.getenv("GROQ_API_KEY")

def security_scan(analysis, solutions):
    client = Groq(api_key=GROQ_KEY)
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""
You are a world-class security engineer.

Issue Analysis:
{analysis}

Proposed Solutions:
{solutions}

Return in this exact format:

SECURITY RISKS:
1. (risk 1)
2. (risk 2)
3. (risk 3)

VULNERABILITIES DETECTED:
1. (vulnerability 1)
2. (vulnerability 2)

SECURITY RECOMMENDATIONS:
1. (recommendation 1)
2. (recommendation 2)

SAFE TO IMPLEMENT: (Yes/No and why)

SECURITY SCORE: (X/10)
"""
            }
        ]
    )
    return chat_completion.choices[0].message.content

def run_agent4(analysis, solutions):
    print("\n\U0001F512 AGENT 4 — Security Scanner Starting...")
    print("=" * 50)
    security = security_scan(analysis, solutions)
    print(security)
    print("=" * 50)
    return security

if __name__ == "__main__":
    test_analysis = "Login button not working on iOS mobile devices"
    test_solutions = "Fix CSS touch events and update HTML button element"
    run_agent4(test_analysis, test_solutions)
