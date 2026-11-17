from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
text = [
    "Python is a programming language",
    "Python is used for software development",
    "The weather is very beautiful today"
]
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(text)
for i in range(len(text) - 1):
    score = cosine_similarity(
        vectors[i], vectors[i + 1]
    )[0][0]
    print("Sentence", i + 1, "and", i + 2,
          "Similarity:", round(score, 3))
