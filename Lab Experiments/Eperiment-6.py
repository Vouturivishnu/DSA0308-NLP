import random
text = "I love natural language processing. I love Python programming."
words = text.lower().replace(".", "").split()
bigrams = {}
for i in range(len(words) - 1):
    bigrams.setdefault(words[i], []).append(words[i + 1])
word = "i"
result = [word]
for i in range(6):
    if word in bigrams:
        word = random.choice(bigrams[word])
        result.append(word)
    else:
        break
print("Generated Text:", " ".join(result))
