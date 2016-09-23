class TrimTransformer:
    def __init__(self, num):
        """Create a trim transformer with a specific trim amount"""
        self.num = num
    def apply(self, name):
        """Trim the name"""
        if self.num > 0:
            return name[self.num:]
        else :
            return name[:self.num]
