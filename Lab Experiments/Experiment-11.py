import nltk
grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'cat' | 'mouse'
V -> 'chased'
""")
parser = nltk.ChartParser(grammar)
sentence = "the cat chased the mouse".split()
for tree in parser.parse(sentence):
    print(tree)
