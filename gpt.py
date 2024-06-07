from g4f.client import Client

client = Client()

completions = client.chat.completions.create(model="gpt-4o", messages=[{"content": "hi"}])
print(completions.choices[0].message.content)