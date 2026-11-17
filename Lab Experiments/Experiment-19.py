import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.wsd import lesk
sentence = ["I", "went", "to", "the", "bank", "to", "deposit", "money"]
sense = lesk(sentence, "bank")
print("Word: bank")
print("Meaning:", sense.definition() if sense else "Not found")
