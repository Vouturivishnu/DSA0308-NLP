from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
documents = [
    "Python is a programming language",
    "Machine learning uses Python",
    "Natural language processing is interesting"
]
query = ["Python programming"]
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(documents + query)
similarity = cosine_similarity(tfidf[-1], tfidf[:-1])
print("Document Ranking:")
ranking = similarity[0].argsort()[::-1]
for i in ranking:
    print("Document", i + 1, "Score:", round(similarity[0][i], 3))
