class TrimTransformer:
    def __init__(self, num):
        self.num = num
    def apply(self, name):
        if self.num > 0:
            return name[self.num:]
        else :
            return name[:self.num]
