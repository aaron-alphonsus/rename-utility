import argparse

def AddTransform(xfrm):
    """Create an argparse.Action subclass that constructs a transformer instance from
the argument values and pushes the result into a list."""
    class RenamingAction (argparse.Action) :
        def __call__(self, parser, namespace, values, option_string):
            """Handle the arguments passed to the flag. Construct a transformer class and push it onto the destination"""
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
