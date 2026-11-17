import nltk
from nltk.tag import UnigramTagger
from nltk.corpus import brown
nltk.download('brown')
train_data = brown.tagged_sents()[:500]
tagger = UnigramTagger(train_data)
words = ["The", "dog", "runs", "quickly"]
result = tagger.tag(words)
print("POS Tags:", result)
