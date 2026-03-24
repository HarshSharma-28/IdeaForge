import requests
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")
GROQ_KEY = os.getenv("GROQ_API_KEY")
PROJECT_ID = os.getenv("GITLAB_PROJECT_ID")

def get_repo_files():
    url = f"https://gitlab.com/api/v4/projects/{PROJECT_ID}/repository/tree"
    headers = {"PRIVATE-TOKEN": GITLAB_TOKEN}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []
    return response.json()

def expand_problem(analysis, files):
    client = Groq(api_key=GROQ_KEY)
    file_names = [f['name'] for f in files]
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""
You are a world-class software architect.

Based on this issue analysis:
{analysis}

And these files in the codebase:
{file_names}

Return in this exact format:
1. RELATED PROBLEMS: (what other problems could exist)
2. AFFECTED FILES: (which files likely need changes)
3. RISK AREAS: (what could break if not fixed)
4. HIDDEN ISSUES: (deeper problems this reveals)
5. ECOSYSTEM IMPACT: (how this affects overall system)
"""
            }
        ]
    )
    return chat_completion.choices[0].message.content

def run_agent2(analysis):
    print("\n\U0001F50D AGENT 2 — Problem Expansion Starting...")
    print("=" * 50)
    files = get_repo_files()
    expansion = expand_problem(analysis, files)
    print(expansion)
    print("=" * 50)
    return expansion

if __name__ == "__main__":
    test_analysis = "Login button not working on iOS mobile devices"
    run_agent2(test_analysis)
