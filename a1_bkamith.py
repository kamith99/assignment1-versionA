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
from assignment1 import after
after('2023-01-25')

# assignment1.py

def leap_year(year):
    """Determines if a given year is a leap year."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def mon_max(month, year):
    """Returns the maximum number of days in a given month."""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year(year) else 28
    return None  # Invalid month

def after(day, month, year, n):
    """Calculates the date after n days from the given date."""
    while n > 0:
        max_days = mon_max(month, year)
        if day + n <= max_days:
            day += n
            n = 0
        else:
            n -= (max_days - day + 1)
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
    return day, month, year

def day_of_week(day, month, year):
    """Determines the day of the week for a given date."""
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    f = day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)
    return f % 7  # 0=Saturday, 1=Sunday, ..., 6=Friday


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
    "Print a usage message to the user"
    ...


def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    ...

def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    ...

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    ...

if __name__ == "__main__":
    ...