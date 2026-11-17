import nltk
grammar = nltk.CFG.fromstring("""
S -> SG SV | PL PV
SG -> 'he' | 'she'
PL -> 'they' | 'we'
SV -> 'runs' | 'plays'
PV -> 'run' | 'play'
""")
parser = nltk.ChartParser(grammar)
sentences = [
    "he runs",
    "they run",
    "he run",
    "they runs"
]
for sentence in sentences:
    tokens = sentence.split()
    try:
        result = list(parser.parse(tokens))
        if result:
            print(sentence, "-> Correct Agreement")
        else:
            print(sentence, "-> Incorrect Agreement")
    except ValueError:
        print(sentence, "-> Incorrect Agreement")
