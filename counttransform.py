import re

class CountTransform:
    def __init__(self, pattern):
        self.idx = 0
        self.prefix, replace, self.suffix = re.split("(#+)", pattern)
        self.sublen = len(replace)

    def apply(self, name):
        self.idx += 1
        return '{0}{1:0{width}}{2}'.format(self.prefix, self.idx, self.suffix, width=self.sublen)
