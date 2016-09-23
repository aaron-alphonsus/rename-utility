import datetime
import os
import time
import re

def changeDate(names, date):
    """ Takes in list of files and string containing date in DDMMYYYY format.
        Changes date in each file timestamp. """  

    # parse date
    try:
        day, month, year = re.fullmatch("(\d\d)(\d\d)(\d\d\d\d)", date).groups()
    except AttributeError as e:
        raise
 
    # convert strings to ints
    day = int(day)
    month = int(month)
    year = int(year)
           
    for name in names:

        # get HH MM SS from file
        p_timestamp = os.path.getmtime(name)
        mdt = datetime.datetime.fromtimestamp(p_timestamp)

        # construct new datetime object with file time and provided date
        mdt = datetime.datetime(year, month, day, mdt.hour, mdt.minute, mdt.second)

        # change to new file timestamp by passing in datetime.timestamp() 
        os.utime(name, (mdt.timestamp(), mdt.timestamp()))
