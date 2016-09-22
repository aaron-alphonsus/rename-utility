import argparse

def AddTransform(xfrm):
    class RenamingAction (argparse.Action) :
        def __call__(self, parser, namespace, values, option_string):
            if type(values) == list:
                val = xfrm(*values)
            else:
                val = xfrm(values)
            ops = getattr(namespace, self.dest)
            if ops is None:
                ops = []
            ops.append(val)
            setattr(namespace, self.dest, ops)
    return RenamingAction
