import os

def Touch (names):
    for n in names:
        os.utime(n)
