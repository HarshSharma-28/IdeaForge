import requests
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"C:\Users\Harsh Sharma\Desktop\ideaforge\.env")

GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")
GROQ_KEY = os.getenv("GROQ_API_KEY")
PROJECT_ID = os.getenv("GITLAB_PROJECT_ID")

def get_gitlab_issues():
    url = f"https://gitlab.com/api/v4/projects/{PROJECT_ID}/issues"
    headers = {"PRIVATE-TOKEN": GITLAB_TOKEN}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"API Error ({response.status_code}): {response.text}")
        return []
    return response.json()

def analyze_issue(issue_text):
    client = Groq(api_key=GROQ_KEY)
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": f"""
You are a world-class software engineer.
Analyze this GitLab issue deeply.

Issue: {issue_text}

Return analysis in this exact format:
1. SURFACE PROBLEM: (what they said)
2. REAL PROBLEM: (what actually is wrong)
3. ROOT CAUSE: (why it happened)
4. SEVERITY: (Critical/High/Medium/Low)
5. AFFECTED AREAS: (what else might break)
6. RECOMMENDED FIX: (what should be done)
"""}]
    )
    return chat_completion.choices[0].message.content

def run_agent1():
    print("🤖 AGENT 1 — Issue Intelligence Starting...")
    print("=" * 50)
    if not GROQ_KEY:
        print("❌ GROQ_API_KEY missing in .env!")
        return None
    issues = get_gitlab_issues()
    if not issues:
        print("No issues found!")
        return None
    full_analysis = ""
    for issue in issues[:3]:
        print(f"\n📋 Issue: {issue['title']}")
        print("-" * 40)
        analysis = analyze_issue(issue['title'] + " " + issue.get('description', ''))
        print(analysis)
        print("=" * 50)
        full_analysis += analysis
    return full_analysis

if __name__ == "__main__":
    run_agent1()