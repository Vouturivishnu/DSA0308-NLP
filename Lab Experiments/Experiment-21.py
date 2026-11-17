import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
text = "The intelligent student studies Python programming"
words = nltk.word_tokenize(text)
tags = nltk.pos_tag(words)
grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
chunk_parser = nltk.RegexpParser(grammar)
result = chunk_parser.parse(tags)
print(result)
print("\nNoun Phrases:")
for subtree in result.subtrees():
    if subtree.label() == 'NP':
        phrase = " ".join(word for word, tag in subtree.leaves())
        print(phrase, "-> A person, object or concept")
