import re
text = "I want to travel from mumbai to chennai with flight number 12323"
if re.search(r"mumbai", text, re.IGNORECASE):
    text = re.sub(r"mumbai", "bangalore", text, flags=re.IGNORECASE)
if re.search(r"chennai", text, re.IGNORECASE):
    text = re.sub(r"chennai", "pune", text, flags=re.IGNORECASE)
if re.search(r"\b\d{5}\b", text):
    text = re.sub(r"\b\d{5}\b", "21342", text)
print("Updated Text:", text)
