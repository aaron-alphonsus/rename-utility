#!/bin/env python3

# ***** rename.py *****
# A file management utility written in Python to perform batch file operations.
# CSC461 Programming Languages, Fall 2016 (JMW)
# Usage: python rename.py [-h] [-v] [-p] [-i] [-d] [-dt] [-D DDMMYYYY] 
#        [-T HHMMSS] [-l] [-u] [-t n] [-r oldstring newstring] [-n countstring]
#        [files [files ...]]
# <Will be changed later> Parses arguments and prints each argument value

import sys, argparse

from renamingaction import AddTransform

from renamer import Renamer 

import counttransform, lowercase, uppercase, regex, trim

from delete import Delete
from touch import Touch

'''parser = argparse.ArgumentParser( usage = "-h for help, -v for verbose," 
   "-i for int, -f for float" )'''

parser = argparse.ArgumentParser()

# optional switches (may occur in any order)
parser.add_argument( "-v", "--verbose", action="store_true", 
    help="print old and new filenames during processing" )
parser.add_argument( "-p", "--print", action="store_true", 
    help="print old and new filenames, do not rename" )
parser.add_argument( "-i", "--interactive", action="store_true", 
    help="interactive mode, ask user prior to processing each file" )
parser.add_argument( "-d", "--delete", action="store_true", 
    help="delete files" )
parser.add_argument( "-dt", "--touch", action="store_true", 
    help="\"touch\" files (update date/time stamp to current date/time" )

parser.add_argument( "-D", "--date", metavar="DDMMYYYY", 
    help="change file datestamps" )
parser.add_argument( "-T", "--time", metavar="HHMMSS", 
    help="change file timestamps" )

parser.add_argument( "-l", "--lower", action=AddTransform(lowercase.Lowercase),
                     dest="operations", nargs=0,
    help="convert filenames to lowercase" )
parser.add_argument( "-u", "--upper", action=AddTransform(uppercase.Uppercase),
                     dest="operations", nargs=0,
    help="convert filenames to uppercase" )

parser.add_argument( "-t", "--trim", metavar="n", type=int,
                     action=AddTransform(trim.TrimTransformer), dest="operations",
    help="positive n: trim n chars from the start of each filename\n"
         "negative n: trim n chars from the end of each filename" )

parser.add_argument( "-r", "--replace", action=AddTransform(regex.RegexTransformer), nargs=2, 
                     metavar=("oldstring", "newstring"), type=str,
                     dest = "operations",
                     help="replace \"oldstring\" with \"newstring\" in filenames" )
parser.parse_args("-r one two -r three four".split())

parser.add_argument( "-n", "--number", metavar="countstring", dest="operations",
                     action=AddTransform(counttransform.CountTransform),
    help="#'s in \"countstring\" become numbers" )

# followed by 1 or more strings
parser.add_argument( "files", type=str, nargs='+', help="list of filenames" )
 
# parse command arguments
args = parser.parse_args()

if args.delete:
    Delete(args.files)

if args.touch:
    Touch(args.files)    

# print results of parsing
print( '\ncmd args:', sys.argv )
print()
print( 'argparse:', args )
print()

print( 'args.verbose =', args.verbose )
print( 'args.print =', args.print )
print( 'args.interactive =', args.interactive )
print( 'args.delete =', args.delete )
print( 'args.touch =', args.touch )

print( 'args.date =', args.date )
print( 'args.time =', args.time )

print( 'args.operations =', args.operations )

print ( "files", args.files )
