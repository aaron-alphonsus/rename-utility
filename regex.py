import re

class RegexTransformer:
    def __init__(self, pat, rep):
        """Initialize a RegexTransformer"""
        self.pat = re.compile(pat)
        self.rep = rep

    def apply(self, name):
        """Transform a name with the given pattern"""
        return self.pat.sub(self.rep, name)
