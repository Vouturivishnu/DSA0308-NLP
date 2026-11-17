text = "Ravi is a student. He studies Python. He likes programming."
sentences = text.split(".")
last_noun = None
for sentence in sentences:
    words = sentence.strip().split()
    if not words:
        continue
    if words[0].lower() in ["he", "she", "it", "they"]:
        print(words[0], "refers to", last_noun)
    else:
        last_noun = words[0]
        print("Entity:", last_noun)
