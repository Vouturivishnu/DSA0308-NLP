import nltk
nltk.download("punkt_tab")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger")
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
sample_text = (
    "The engineers are running faster, computing complex algorithms, and"
    " successfully bettering their previous software models."
)
print("=== ORIGINAL TEXT ===")
print(sample_text)
def perform_morphological_analysis(text):
  tokens = word_tokenize(text)
  stemmer = PorterStemmer()
  lemmatizer = WordNetLemmatizer()
  pos_tags = nltk.pos_tag(tokens)
  print(
      "\n=== MORPHOLOGICAL BREAKDOWN (Token | POS Tag | Stem | Lemma) ==="
  )
  print(f"{'Token':<15} | {'POS Tag':<10} | {'Stem':<12} | {'Lemma':<12}")
  print("-" * 60)
  for word, tag in pos_tags:
    stemmed = stemmer.stem(word)
    pos_lower = tag[0].lower()
    wn_pos = (
        nltk.corpus.wordnet.NOUN
        if pos_lower not in ["j", "v", "r"]
        else (
            nltk.corpus.wordnet.ADJ
            if pos_lower == "j"
            else (
                nltk.corpus.wordnet.VERB
                if pos_lower == "v"
                else nltk.corpus.wordnet.ADV
            )
        )
    )
    lemmatized = lemmatizer.lemmatize(word.lower(), pos=wn_pos)
    print(f"{word:<15} | {tag:<10} | {stemmed:<12} | {lemmatized:<12}")
perform_morphological_analysis(sample_text)
