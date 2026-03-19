from agent1 import run_agent1
from agent2 import run_agent2
from agent3 import run_agent3
from agent4 import run_agent4
from agent5 import run_agent5

def run_ideaforge():
    print("🚀 IDEAFORGE AI — STARTING FULL PIPELINE")
    print("=" * 50)
    
    issues = run_agent1()
    if not issues:
        return
        
    analysis = issues
    expansion = run_agent2(analysis)
    solutions = run_agent3(analysis, expansion)
    security = run_agent4(analysis, solutions)
    run_agent5(analysis, solutions, security)
    
    print("\n✅ IDEAFORGE PIPELINE COMPLETE!")

if __name__ == "__main__":
    run_ideaforge()