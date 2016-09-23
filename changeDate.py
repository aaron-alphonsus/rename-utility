import datetime
import os
import time
import re

def changeDate(names, date):

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
        
        mdt = datetime.datetime(year, month, day, mdt.hour, mdt.minute, mdt.second)
   
        os.utime(name, (mdt.timestamp(), mdt.timestamp()))
