import json
import os
from dotenv import load_dotenv

from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

system_prompt = """
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

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=system_prompt,
        response_mime_type="application/json",
    ),
)

query = input("> ")

response = chat.send_message(query)

while True:
    parsed_response = json.loads(response.text)

    print(f"🧠 {parsed_response['step']}: {parsed_response['content']}")

    if parsed_response["step"] == "result":
        break

    response = chat.send_message("Continue to the next step only.")