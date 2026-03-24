import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_KEY = os.getenv("GROQ_API_KEY")

def generate_solutions(analysis, expansion):
    client = Groq(api_key=GROQ_KEY)
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""
You are a world-class software engineer and startup founder.

Issue Analysis:
{analysis}

Problem Expansion:
{expansion}

Generate exactly 3 solutions:

SOLUTION 1 - QUICK FIX:
- What: 
- How:
- Time: 
- Risk:

SOLUTION 2 - SMART FIX:
- What:
- How:
- Time:
- Risk:

SOLUTION 3 - ARCHITECTURE FIX:
- What:
- How:
- Time:
- Risk:

RECOMMENDED: (which one and why)
"""
            }
        ]
    )
    return chat_completion.choices[0].message.content

def run_agent3(analysis, expansion):
    print("\n\U0001F4A1 AGENT 3 — Solution Generator Starting...")
    print("=" * 50)
    solutions = generate_solutions(analysis, expansion)
    print(solutions)
    print("=" * 50)
    return solutions

if __name__ == "__main__":
    test_analysis = "Login button not working on iOS mobile devices"
    test_expansion = "CSS touch events affected, auth flow at risk"
    run_agent3(test_analysis, test_expansion)
