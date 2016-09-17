# ***** rename.py *****
# A file management utility written in Python to perform batch file operations.
# CSC461 Programming Languages, Fall 2016 (JMW)
# Usage: python rename.py [-h] [-v] [-p] [-i] [-d] [-dt] [-D DDMMYYYY] 
#        [-T HHMMSS] [-l] [-u] [-t n] [-r oldstring newstring] [-n countstring]
#        [files [files ...]]
# <Will be changed later> Parses arguments and prints each argument value

import sys, argparse

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

parser.add_argument( "-l", "--lower", action="store_true", 
    help="convert filenames to lowercase" )
parser.add_argument( "-u", "--upper", action="store_true", 
    help="convert filenames to uppercase" )

parser.add_argument( "-t", "--trim", metavar="n", 
    help="positive n: trim n chars from the start of each filename\n"
         "negative n: trim n chars from the end of each filename" )

parser.add_argument( "-r", "--replace", action="append", nargs="*", 
    metavar=("oldstring", "newstring"), 
    help="replace \"oldstring\" with \"newstring\" in filenames" )
parser.parse_args("-r one two -r three four".split())

parser.add_argument( "-n", "--number", metavar="countstring", 
    help="#'s in \"countstring\" become numbers" )

'''parser.add_argument( "-i", "--integer", type=int, metavar="N", 
    help="supply an int value" )
parser.add_argument( "-f", "--real", type=float, metavar="N", 
    help="supply a float value" )'''
'''
# required positional arguments
parser.add_argument( "x", type=int, help="base" )
parser.add_argument( "y", type=int, help="exponent" )
'''

# followed by 0 or more strings
parser.add_argument( "files", type=str, nargs='*', help="list of filenames" )
 
# parse command arguments
args = parser.parse_args()

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

print( 'args.lower =', args.lower )
print( 'args.upper =', args.upper )

print( 'args.trim =', args.trim )
print( 'args.replace =', args.replace )
print( 'args.number =', args.number )

print ( "files", args.files )
'''
print( 'args.integer =', args.integer )
print( 'args.real =', args.real )
print( args.x, "**", args.y, "=", args.x ** args.y )
print( "names: ", args.names )
'''
