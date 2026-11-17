import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
text = "The student is studying Python programming"
words = nltk.word_tokenize(text)
tags = nltk.pos_tag(words)
print(tags)
