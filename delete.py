import os

def Delete (names):
    """ Takes in list of files. Deletes each file. """
    for n in names:
        os.remove(n) 
