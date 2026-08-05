
# chatgpt
# import tiktoken


# encoder = tiktoken.encoding_for_model('gpt-4o')

# print("vocal size", encoder.n_vocab) 

# text= "The cat sat on the mat"
# tokens = encoder.encode(text)

# print("Tokens",tokens) 

#Gemni 
# from google import genai

# client = genai.Client(api_key="AQ.Ab8RN6J8GHEojSlbUYvRiL-oYd3yUbyQsZr4cF6H0v8DLsdQ6Q")

# response = client.models.count_tokens(
#       model='gemini-2.0-flash',
#       contents='What is your name?',
#   )
# print(response)

# from google import genai

# client = genai.Client(api_key="AQ.Ab8RN6J8GHEojSlbUYvRiL-oYd3yUbyQsZr4cF6H0v8DLsdQ6Q")

# text = """
# Write a production-ready REST API using FastAPI with JWT authentication,
# PostgreSQL, SQLAlchemy, Alembic, Docker, and unit tests.
# """

# response = client.models.count_tokens(
#     model="gemini-2.5-flash",
#     contents=text
# )

# print(f"Tokens: {response.total_tokens}")


from google import genai

client = genai.Client(api_key="AQ.Ab8RN6J8GHEojSlbUYvRiL-oYd3yUbyQsZr4cF6H0v8DLsdQ6Q")

response = client.models.count_tokens(
    model="gemini-2.0-flash",
    contents="The cat sat on the mat"
)

print(response.total_tokens)
    