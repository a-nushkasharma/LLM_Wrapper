import json
from analyzer import extract_functions
from llm_api import call_gpt_analysis
from prompt_templates import VULNERABILITY_DETECTION_PROMPT

def analyze_contract(input_file, output_file):
    with open(input_file, 'r') as f:
        code = f.read()

    functions = extract_functions(code)
    results = []

    for fn in functions:
        try:
            response = call_gpt_analysis(VULNERABILITY_DETECTION_PROMPT, fn)
            data = json.loads(response)
            results.extend(data)
        except Exception as e:
            print(f"Error analyzing function: {fn[:50]}... \n{e}")

    with open(output_file, 'w') as out:
        json.dump({
            "contract_file": input_file,
            "analysis_results": results,
            "documentation": {
                "region": "Function or basic block in the contract",
                "basic_block_summary": "High-level summary of what this block does",
                "violated_property": "Security property likely violated",
                "reason": "Explanation for why this might be vulnerable"
            }
        }, out, indent=2)
