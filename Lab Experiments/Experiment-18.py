import re
expression = "Human(Socrates) AND Mortal(Socrates)"
tokens = re.findall(r'[A-Za-z_][A-Za-z_0-9]*|[()]', expression)
print("Logical Expression:", expression)
print("Tokens:", tokens)
if "AND" in tokens and "(" in tokens and ")" in tokens:
    print("Valid Logical Expression")
else:
    print("Invalid Logical Expression")
