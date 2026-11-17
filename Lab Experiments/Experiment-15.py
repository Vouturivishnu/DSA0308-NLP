import nltk
grammar = nltk.PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'the dog' [0.5] | 'a dog' [0.5]
VP -> 'barks' [1.0]
""")
parser = nltk.ViterbiParser(grammar)
sentence = ["the dog", "barks"]
for tree in parser.parse(sentence):
    print(tree)
    print("Probability:", tree.prob())
