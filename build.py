import os, re, json

files = [
    "temp_zip/ideaforge/.gitlab/duo-workflow/agents/01-issue-intelligence.yml",
    "temp_zip/ideaforge/.gitlab/duo-workflow/agents/02-problem-expansion.yml",
    "temp_zip/ideaforge/.gitlab/duo-workflow/agents/03-solution-generator.yml",
    "temp_zip/ideaforge/.gitlab/duo-workflow/agents/04-security-scanner.yml",
    "temp_zip/ideaforge/.gitlab/duo-workflow/agents/05-pr-generator.yml"
]

components = []
prompts = []
routers = []
last_id = None

for idx, fpath in enumerate(files):
    if not os.path.exists(fpath): continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    name_match = re.search(r'^name:\s*(.+)$', content, re.M)
    original_name = name_match.group(1).strip() if name_match else f"agent_{idx}"
    comp_name = original_name.replace("-", "_")
    
    tools = []
    tools_match = re.search(r'^tools:\s*\n((?:\s+-\s+[^\n]+\n?)+)', content, re.M)
    if tools_match:
        for line in tools_match.group(1).split('\n'):
            if '-' in line:
                tools.append(line.split('-')[1].strip())
    
    instr_match = re.search(r'^instructions:\s*\|\s*\n(.*)$', content, re.M | re.S)
    if instr_match:
        instructions = instr_match.group(1).strip()
        instructions = re.sub(r'\n?tools:.*$', '', instructions, flags=re.S)
    else:
        instructions = "Placeholder instructions."
        
    components.append(f'''    - name: "{comp_name}"\n      type: AgentComponent\n      prompt_id: "{comp_name}_prompt"\n      inputs: ["context:goal"]\n      toolset: {json.dumps(tools)}''')
      
    system_prompt_indented = "\\n".join(["          " + line for line in instructions.split('\\n')])
    prompts.append(f'''    - prompt_id: "{comp_name}_prompt"\n      name: "{original_name} Prompt"\n      prompt_template:\n        system: |\n{system_prompt_indented}\n        user: |\n          {{{{goal}}}}\n        placeholder: history\n      unit_primitives: []\n      params:\n        timeout: 180''')

    if last_id:
        routers.append(f'''    - from: "{last_id}"\n      to: "{comp_name}"''')
    
    last_id = comp_name

if last_id:
    routers.append(f'''    - from: "{last_id}"\n      to: "end"''')

yaml_content = f'''name: "IdeaForge Automated Flow"\ndescription: "A 5-agent sequential orchestration."\npublic: true\ndefinition:\n  version: v1\n  environment: ambient\n  components:\n{chr(10).join(components)}\n\n  prompts:\n{chr(10).join(prompts)}\n\n  routers:\n{chr(10).join(routers)}\n\n  flow:\n    entry_point: "issue_intelligence"\n'''

with open("flows/ideaforge-flow.yml", "w", encoding="utf-8") as f:
    f.write(yaml_content)
