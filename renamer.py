import os
import os.path
import datetime

class Renamer:
    """This class performs the file renaming"""
    def __init__(self, operations = []):
        self.operations = operations

    def addOp(self, op):
        self.operations << op

    def transformSingle(self, name):
        for op in self.operations:
            name = op.apply(name)
        return name

    def transform(self, nameList):
        return {name: self.transformSingle(name) for name in nameList}

    def apply(self, nameList, ctlFunc = lambda s, d: True):
        nameMap = self.transform(nameList)
        for src, dst in nameMap.items():
            if ctlFunc(src, dst):
                os.rename(src, dst)
