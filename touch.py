import os

def Touch (names):
    """ Takes in list of files. 
        Changes timestamp of each file to current date/time. """
    for n in names:
        os.utime(n)
