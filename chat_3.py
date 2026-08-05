import json
from dotenv import load_dotenv
import os

from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

system_prompt="""
You are an AI assistent who is expert in breaking down complex promblems and then resolve the user query.

For the given user input, analyse the input and break down the problem step by step.

Follow the steps in sequence that is "analyse", "think", "output", "validate" and "result".

Rules:
1. Follow the strict JSON output as per Output schema.
2. Always perform one step at a time and wait for next input.
3. Carefully analyse the user query

Output Format:
{{
     step: "string",
     content: "string",
}}

Examples:
Input: what is 2+2.
Output:{{step: "analyse", content: "Alright! The user is interested  in maths query and he is asking a basic arthimatic operation"}}
Output:{{step: "think", content:"To perform the addition i must go from left to right and add all the operands"}}
Output:{{step:"output", content:"4"}}
Output:{{step:"validate", content:"seems like 4 is correct answer for 2 + 2"}}
Output:{{step:"result", content:"2 + 2 = 4 and that is calculated by adding all numbers"}}

"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=system_prompt,
        response_mime_type="application/json",
    ),
    contents=[
        {
            "role": "user",
            "parts": [
                {
                    "text": "what is 3 + 4 * 5"
                }
            ]
        },

        # Assistant examples
        {
            "role": "model",
            "parts": [
                {
                    "text": json.dumps({
                        "step": "analyse",
                        "content": "The user is asking for an arithmetic operation that involves both addition and multiplication, so I need to follow the order of operations."
                    })
                }
            ]
        },
        {
            "role": "model",
            "parts": [
                {
                    "text": json.dumps({
                        "step": "think",
                        "content": "In order of operations, multiplication should be performed before addition. Therefore, I should first multiply 4 by 5."
                    })
                }
            ]
        },
        {
            "role": "model",
            "parts": [
                {
                    "text": json.dumps({
                        "step": "think",
                        "content": "Calculate the multiplication: 4 * 5 = 20."
                    })
                }
            ]
        },
        {
            "role": "model",
            "parts": [
                {
                    "text": json.dumps({
                        "step": "think",
                        "content": "Next, I need to add the result of the multiplication (20) to the number 3."
                    })
                }
            ]
        },
    ]
)

print(response.text)