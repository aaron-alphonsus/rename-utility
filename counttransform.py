import re

class CountTransform:
    def __init__(self, pattern):
        """Initialize the pattern for a Countstring Transform"""
        self.idx = 0
        self.prefix, replace, self.suffix = re.split("(#+)", pattern)
        self.sublen = len(replace)

    def apply(self, name):
        """Apply the countstring transformation. Discard the original name and return the nth form of the template."""
        self.idx += 1
        return '{0}{1:0{width}}{2}'.format(self.prefix, self.idx, self.suffix, width=self.sublen)
