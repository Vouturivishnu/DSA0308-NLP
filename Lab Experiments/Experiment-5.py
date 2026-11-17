from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["playing", "played", "plays", "running", "runner",
         "happiness", "studies", "connected"]
for word in words:
    print(word, "->", ps.stem(word))
