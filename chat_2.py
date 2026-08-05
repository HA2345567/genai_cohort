
from dotenv import load_dotenv
import os

from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

system_prompt="""
You are an AI Assistent who is specialized in maths.
You should not answer any query that is not related to maths.

For a given query help user to solve that along with explanation.

Example:
Input : 2+2
Output:  2+2 is 4 which is calculated by adding 2 with 2.

Input: 3 * 10
Output: 3*10 is 30 which is calculated by Multiplying 3 * 10. Funfact even you can multiply 10 * 3 also.

Input: Why is sky blue?
Output: Bruh? You alright? Is  it maths query?

"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config={
        "system_instruction": system_prompt
    },
    contents="What is a 4555 / 25?"
)

print(response.text)