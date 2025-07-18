import openai

# Replace with your actual OpenAI key
openai.api_key = "api_Key"

def call_gpt_analysis(prompt, code_snippet):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in smart contract vulnerability detection."},
            {"role": "user", "content": prompt + "\n\n" + code_snippet}
        ],
        temperature=0.2
    )
    return response['choices'][0]['message']['content']
