import os
import os.path
import datetime

class Renamer:
    """This class performs the file renaming"""
    def __init__(self, operations = []):
        """Initialize the renamer with a list of operations"""
        self.operations = operations

    def addOp(self, op):
        """Append a new operation to the renaming pipeline"""
        self.operations << op

    def transformSingle(self, name):
        """Apply the renaming pipeline to a single name"""
        for op in self.operations:
            name = op.apply(name)
        return name

    def transform(self, nameList):
        """Convert a list of names into a map from the old name to the new name"""
        return {name: self.transformSingle(name) for name in nameList}

    def apply(self, nameList, ctlFunc = lambda s, d: True):
        """Rename the files given in namelist with the renaming pipeline."""
        nameMap = self.transform(nameList)
        for src, dst in nameMap.items():
            if ctlFunc(src, dst):
                os.rename(src, dst)
