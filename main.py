from google import genai

# Your Gemini API key
client = genai.Client(api_key="AIzaSyCASEDb2_kwam1d0ap2zRA_avlRxUxD1i8")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Write a 150‑word response to: Why do I want to attend this summer STEM program?"
)

print(response.text)
