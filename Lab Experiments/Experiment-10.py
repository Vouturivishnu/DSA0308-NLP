words = ["I", "am", "playing", "football"]
tags = ["PRP", "VB", "NN", "NN"]
print("Before Transformation:")
print(list(zip(words, tags)))
for i, word in enumerate(words):
    if word.endswith("ing"):
        tags[i] = "VBG"
print("After Transformation:")
print(list(zip(words, tags)))
