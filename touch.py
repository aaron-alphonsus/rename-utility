import os

def Touch (names, ctlFunc = lambda s, d: True):
    """ Takes in list of files. 
        Changes timestamp of each file to current date/time. """
    for n in names:
        if ctlFunc(n, "*TOUCH*"):
            os.utime(n)
