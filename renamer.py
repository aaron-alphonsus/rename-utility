import os
import os.path
import datetime

class Renamer:
    """This class performs the file renaming"""
    def __init__(self):
        self.operations = []

    def addOp(self, op):
        self.operations << op

    def transformSingle(self, name):
        for op in self.operations:
            name = op.apply(name)
        return name

    def transform(self, nameList):
        return {name: self.transformSingle(name) for name in nameList}

    def apply(self, nameList):
        nameMap = transform(self, nameList)
        for src, dst in items(nameMap):
            os.rename(src, dst)
