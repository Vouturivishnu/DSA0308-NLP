import nltk
grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'a' | 'the'
N -> 'boy' | 'apple'
V -> 'eats'
""")
parser = nltk.ChartParser(grammar)
sentence = "the boy eats an apple".split()
grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'a' | 'the' | 'an'
N -> 'boy' | 'apple'
V -> 'eats'
""")
parser = nltk.ChartParser(grammar)
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
