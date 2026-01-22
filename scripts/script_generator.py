
import os
from groq import Groq

# Load API key from GitHub Secrets
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")

# Initialize Groq client
client = Groq(api_key=api_key)

# Prompt for YouTube script
prompt = """
Write a 60-second YouTube Shorts script about an interesting fact.
Use simple English.
Add a strong hook in the first line.
"""

# Call Groq API
response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Get generated script
script = response.choices[0].message.content

# Save output to file (repo me save hoga)
output_path = "scripts/output_script.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(script)

print("✅ Script generated successfully")
print("📄 Saved at:", output_path)
print("------ SCRIPT START ------")
print(script)
print("------- SCRIPT END -------")
