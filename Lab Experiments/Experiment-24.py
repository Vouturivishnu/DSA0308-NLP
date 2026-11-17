def dialog_act(sentence):
    sentence = sentence.lower()
    if sentence.startswith(("hi", "hello", "hey")):
        return "Greeting"
    elif sentence.endswith("?"):
        return "Question"
    elif "thank" in sentence:
        return "Thanking"
    elif sentence.startswith(("bye", "goodbye")):
        return "Goodbye"
    else:
        return "Statement"
dialogues = [
    "Hello",
    "How are you?",
    "I am fine",
    "Thank you",
    "Goodbye"
]
for sentence in dialogues:
    print(sentence, "->", dialog_act(sentence))
