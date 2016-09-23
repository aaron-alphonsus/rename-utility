import datetime
import os
import time
import re

def changeTime( names, time ):
    """ Takes in list of files and string containing time in HHMMSS format.
        Changes time in each file timestamp. """
    
    # parse time
    try:
        hour, minute, second = re.fullmatch("(\d\d)(\d\d)(\d\d)", time).groups()
    except AttributeError as e:
        raise

    # convert strings to ints
    hour = int(hour)
    minute = int(minute)
    second = int(second)

    for name in names:

        # get DD MM YYYY from file
        p_timestamp = os.path.getmtime(name)
        mdt = datetime.datetime.fromtimestamp(p_timestamp)
        
        # construct new datetime object with file date and provided time
        mdt = datetime.datetime (mdt.year, mdt.month, mdt.day, hour, minute, second)
        
        # change to new file timestamp by passing in datetime.timestamp()  
        os.utime( name, (mdt.timestamp(), mdt.timestamp() ))
