import os

def Delete (names, ctlFunc = lambda s, d: True):
    """ Takes in list of files. Deletes each file. """
    for n in names:
        if ctlFunc(n, "*DELETE*"):
            os.remove(n) 
