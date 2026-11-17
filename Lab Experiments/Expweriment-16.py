pip install spacy
python -m spacy download en_core_web_sm
import spacy
nlp = spacy.load("en_core_web_sm")
text = "Google was founded in California by Larry Page and Sergey Brin."
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, "->", ent.label_)
