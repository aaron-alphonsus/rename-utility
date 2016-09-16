import re

class RegexTransformer:
    def __init__(self, pat, rep):
        self.pat = regex.compile(pat)
        self.rep = rep

    def apply(self, name):
        return self.pat.sub(self.rep, name)
