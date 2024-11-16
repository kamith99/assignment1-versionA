#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Summer 2023
Program: assignment1.py 
Author: "Student Name"
The python code in this file (a1_[Student_id].py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]



def leap_year(year: int) -> bool:
    """Return True if the year is a leap year."""
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This function has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    tmp_day = day + 1  # next day

    if tmp_day > mon_max(month, year):
        to_day = tmp_day % mon_max(month, year)  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date


def usage():
    """Print a usage message to the user."""
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)


def valid_date(date: str) -> bool:
    """Check validity of date and return True if valid."""
    try:
        year, month, day = map(int, date.split('-'))
        if month < 1 or month > 12:
            return False
        if day < 1 or day > mon_max(month, year):
            return False
        return True
    except ValueError:
        return False


def day_count(start_date: str, stop_date: str) -> int:
    """Loops through range of dates and returns number of weekend days."""
    weekend_days = 0
    current_date = start_date
    
    while current_date != stop_date:
        year, month, day = map(int, current_date.split('-'))
        if day_of_week(year, month, day) in ['sat', 'sun']:
            weekend_days += 1
        current_date = after(current_date)
    
    return weekend_days


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
    
    start_date, stop_date = sys.argv[1], sys.argv[2]
    
    if not valid_date(start_date) or not valid_date(stop_date):
        usage()

    if start_date > stop_date:  # Ensure start_date is earlier than stop_date
        start_date, stop_date = stop_date, start_date

    weekend_days = day_count(start_date, stop_date)
    
    print(f"The period between {start_date} and {stop_date} includes {weekend_days} weekend days.")
