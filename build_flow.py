import yaml
import glob
import os

files = sorted(glob.glob('agents/*.yaml'))
flow_def = {
    'name': 'IdeaForge Automated Flow',
    'description': 'A 5-agent sequential orchestration pipeline.',
    'public': True,
    'definition': {
        'version': 'v1',
        'environment': 'ambient',
        'components': [],
        'prompts': [],
        'routers': [],
        'flow': {}
    }
}

prev_node = None
for i, fpath in enumerate(files):
    with open(fpath, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    agent_name = data.get('name', f'agent_{i}')
    node_name = agent_name.replace('-', '_')
    
    # Add Component
    flow_def['definition']['components'].append({
        'name': node_name,
        'type': 'AgentComponent',
        'prompt_id': f"{node_name}_prompt",
        'inputs': ['context:goal'],
        'toolset': data.get('tools', [])
    })
    
    # Add Prompt
    instructions = data.get('instructions', data.get('description', ''))
    flow_def['definition']['prompts'].append({
        'prompt_id': f"{node_name}_prompt",
        'name': f"{agent_name} Prompt",
        'prompt_template': {
            'system': instructions,
            'user': '{{goal}}',
            'placeholder': 'history'
        },
        'unit_primitives': [],
        'params': {'timeout': 180}
    })
    
    # Add Router
    if prev_node:
        flow_def['definition']['routers'].append({
            'from': prev_node,
            'to': node_name
        })
    else:
        flow_def['definition']['flow']['entry_point'] = node_name
        
    prev_node = node_name

if prev_node:
    flow_def['definition']['routers'].append({
        'from': prev_node,
        'to': 'end'
    })

with open('flows/ideaforge-flow.yml', 'w', encoding='utf-8') as f:
    yaml.dump(flow_def, f, sort_keys=False)

print('Successfully generated flows/ideaforge-flow.yml')
