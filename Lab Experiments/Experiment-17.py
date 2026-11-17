import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet
word = "computer"
synsets = wordnet.synsets(word)
for syn in synsets:
    print("Synset:", syn.name())
    print("Meaning:", syn.definition())
    print()
