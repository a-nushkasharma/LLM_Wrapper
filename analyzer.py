import re

def extract_functions(sol_code):
    pattern = r'(function\s+\w+\s*\(.*?\)[^{]*{[^}]*})'
    matches = re.findall(pattern, sol_code, re.DOTALL)
    return matches
