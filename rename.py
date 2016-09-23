#!/usr/bin/env python3

# ***** rename.py *****
# A file management utility written in Python to perform batch file operations.
# CSC461 Programming Languages, Fall 2016 (JMW)
# Usage: python rename.py [-h] [-v] [-p] [-i] [-d] [-dt] [-D DDMMYYYY] 
#        [-T HHMMSS] [-l] [-u] [-t n] [-r oldstring newstring] [-n countstring]
#        [files [files ...]]
# renames files.

import sys, argparse, glob, os

from renamingaction import AddTransform

from renamer import Renamer 

import counttransform, lowercase, uppercase, regex, trim

from delete import Delete
from touch import Touch
from changeDate import changeDate
from changeTime import changeTime

parser = argparse.ArgumentParser()

# optional switches (may occur in any order)
renmods = parser.add_mutually_exclusive_group()

renmods.add_argument("-v", "--verbose", action="store_true", 
                     help="print old and new filenames during processing")
renmods.add_argument("-p", "--print", action="store_true", 
                     help="print old and new filenames, do not rename")
renmods.add_argument("-i", "--interactive", action="store_true", 
                     help="interactive mode, ask user prior to processing each file")
parser.add_argument("-d", "--delete", action="store_true", 
                    help="delete files")
parser.add_argument("-dt", "--touch", action="store_true", 
                    help="\"touch\" files (update date/time stamp to current date/time")

parser.add_argument("-D", "--date", metavar="DDMMYYYY", 
                    help="change file datestamps")
parser.add_argument("-T", "--time", metavar="HHMMSS", 
                    help="change file timestamps")

renacts = parser.add_argument_group("renaming", "flags to transform file names")
renacts.add_argument("-l", "--lower", action=AddTransform(lowercase.Lowercase),
                     dest="operations", nargs=0,
                     help="convert filenames to lowercase")
renacts.add_argument("-u", "--upper", action=AddTransform(uppercase.Uppercase),
                     dest="operations", nargs=0,
                     help="convert filenames to uppercase")

renacts.add_argument("-t", "--trim", metavar="n", type=int,
                     action=AddTransform(trim.TrimTransformer), dest="operations",
                     help="positive n: trim n chars from the start of each filename\n"
                     "negative n: trim n chars from the end of each filename")

renacts.add_argument("-r", "--replace", action=AddTransform(regex.RegexTransformer), nargs=2, 
                     metavar=("oldstring", "newstring"), type=str,
                     dest = "operations",
                     help="replace \"oldstring\" with \"newstring\" in filenames")

renacts.add_argument("-n", "--number", metavar="countstring", dest="operations",
                     action=AddTransform(counttransform.CountTransform),
                     help="#'s in \"countstring\" become numbers")

# followed by 1 or more strings
parser.add_argument("files", type=str, nargs='+', help="list of filenames")

# parse command arguments
args = parser.parse_args()
try:

    if args.verbose:
        ctlFunc = lambda src, dest: print(src, "=>", dest) or True
    elif args.print:
        ctlFunc = lambda src, dest: print(src, "=>", dest) and False
    elif args.interactive:
        ctlFunc = lambda src, dest: input("%s => %s : y/N: " % (src, dest)).upper() == "Y"
    else:
        ctlFunc = lambda src, dest: True
        
    if os.name == "nt":
        args.files = [name for pat in args.files for name in glob.iglob(pat)]
    if args.delete:
        Delete(args.files, ctlFunc)
        exit()

    if args.touch:
        Touch(args.files, ctlFunc)
        exit()

    if args.date:       
        changeDate( args.files, args.date[-1], ctlFunc)

    if args.time:       
        changeTime( args.files, args.time[-1], ctlFunc)

    if args.operations:
        renamer = Renamer(args.operations)
        renamer.apply(args.files, ctlFunc)
except OSError as ose:
    print(ose.strerror)
    exit(1)
except KeyboardInterrupt:
    print()
    exit(1)
