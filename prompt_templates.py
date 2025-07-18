VULNERABILITY_DETECTION_PROMPT = """
You are a smart contract security expert. Analyze the following Solidity code and identify suspicious regions (functions or code blocks) that might show any of the following vulnerabilities(multiple vulnerabilities might be present):

Reentrancy
Integer Overflow and Underflow
Timestamp Dependence
Denial of Service (DoS)
Gas Limit and Loops
Block Gas Limit DoS
Front-running
Unchecked External Call Return Values
Delegatecall Injection
Broken Access Control
Uninitialized Storage Pointers
Insecure Randomness
Fallback Function Misuse
Force Ether Sending (via selfdestruct)

Return a list of JSON entries, each in the format:
{
  "region": 
  "basic_block_summary": 
  "type_of_vulnerability": "
  "reason": 
}
the region must be the code section that has the vulnerability,basic block summary explains what the vulnerable region does,violated property must 
mention the vulnerability type and reason must  specify why the vulnerability occurs.

Only return valid JSON array.
"""
