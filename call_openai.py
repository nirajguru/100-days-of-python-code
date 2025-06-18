from openai import OpenAI

# Set OPENAI_API_KEY in the environment variables
client = OpenAI()

response = client.responses.create(
    input = "What is the capital of Lonodon",
    instructions= "Talk like a teacher",
    model= "gpt-4o"
)

print(response.output_text)