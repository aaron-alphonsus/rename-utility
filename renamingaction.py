import argparse

def AddTransform(xfrm):
    class RenamingAction (argparse.Action) :
        def __call__(self, parser, namespace, values, option_string):
            print("got values: ", *values)
            val = xfrm(*values)
            ops = getattr(namespace, self.dest)
            if ops is None:
                ops = []
            ops.append(val)
            setattr(namespace, self.dest, ops)
    return RenamingAction
