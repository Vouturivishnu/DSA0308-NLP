import nltk
patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*ly$', 'RB'),
    (r'.*s$', 'NNS'),
    (r'.*', 'NN')
]
tagger = nltk.RegexpTagger(patterns)
sentence = "Students are playing happily"
words = sentence.split()
print("POS Tags:", tagger.tag(words))
