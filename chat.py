
# from dotenv import load_dotenv

# from openai import OpenAI

# load_dotenv()

# client = OpenAI()

# result = client.chat.completions.create(
#     model="gpt-4"
#     message=[
#         {
#             "role": "user",
#             "content": "what is greater? 4.5 or 9.8"
#         }
#     ]

# )

# print(result.choice[0].message.content)


from dotenv import load_dotenv
import os

from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="what is greater? 4.5 or 9.8"
)

print(response.text)