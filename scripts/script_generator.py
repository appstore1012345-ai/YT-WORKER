from datetime import datetime

# Topic (abhi hardcoded)
topic = "Daily Motivation"

# Simple script generate
script = f"""
आज का विषय: {topic}

अगर आप रोज़ अपने लक्ष्य की ओर
छोटे कदम बढ़ाते हैं,
तो एक दिन बड़ी जीत ज़रूर मिलेगी।

कभी हार मत मानो।
"""

# File me save karo
with open("generated_script.txt", "w", encoding="utf-8") as file:
    file.write(script)

# Log print (GitHub Actions me dikhega)
print("✅ Script generated successfully")
print("🕒 Time:", datetime.now())
# Existing script generation code ke baad

# Output folder me save karo
with open("output/script.txt", "w", encoding="utf-8") as f:
    f.write(script)

print("Saved to output/script.txt ✅")
- name: Upload generated script
  uses: actions/upload-artifact@v3
  with:
    name: generated-script
    path: scripts/script_generator.py
