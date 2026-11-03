class MorphologicalFSM:
    def __init__(self):
        self.states = {"q0", "q1", "q2", "reject"}
        self.start_state = "q0"
        self.final_states = {"q2"}
        self.current_state = self.start_state
        self.reg_nouns = {"fox", "cat", "dog", "student", "restaurant"}
        self.irreg_sg = {"goose", "mouse"}
        self.irreg_pl = {"geese", "mice"}
    def reset(self):
        self.current_state = self.start_state
    def parse(self, lemma, affix=""):
        """Processes a lemma and an optional inflectional affix (e.g., '+s')."""
        self.reset()
        if lemma in self.reg_nouns:
            self.current_state = "q1" 
        elif lemma in self.irreg_sg or lemma in self.irreg_pl:
            self.current_state = "q2" 
        else:
            self.current_state = "reject"
            return f"Rejected: '{lemma}' is not recognized in the lexicon."
        if affix == "+s":
            if self.current_state == "q1":
                surface = lemma + "es" if lemma.endswith(("x", "s", "z")) else lemma + "s"
                self.current_state = "q2"
                return f"Accepted: {lemma} + {affix} --> Surface Form: '{surface}'"
            elif self.current_state == "q2":
                self.current_state = "reject"
                return f"Rejected: Irregular noun '{lemma}' cannot take plural suffix '-s'."
        elif affix == "":
            if self.current_state in self.final_states or self.current_state == "q1":
                return f"Accepted: '{lemma}' is valid."
        return f"Rejected: Invalid morphological sequence."
    def orthographic_e_insertion(self, lemma):
        """Simulates the FST orthographic rule: ε -> e / {x, s, z} ^ __ s #"""
        if lemma.endswith(("x", "s", "z")):
            return lemma + "es"
        return lemma + "s"
fsm = MorphologicalFSM()
test_sequences = [
    ("dog", "+s"),
    ("mouse", "+s"),
    ("geese", ""),
    ("fox", "+s"),
    ("mice", "+s")
]
print("=== FSM MORPHOLOGICAL PARSING SIMULATION ===")
for lemma, affix in test_sequences:
    result = fsm.parse(lemma, affix)
    print(f"Query: ({lemma}, '{affix if affix else 'ε'}') ==> {result}")
