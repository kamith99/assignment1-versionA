#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Summer 2024
Program: assignment1.py 
Author: Dalsha Kamith Balasooriya

The python code in this file (a1_bkamith.py) is original work written by
Dalsha Kamith Balasooriya. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Description: This Script calculate the number of weekend days (Saturdays and Sundays) between two given dates. The user provides the start and end dates as command-line arguments in the format YYYY-MM-DD. The script includes error checking for invalid dates and ensures the earlier date is always used as the start date.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    """" Determines the day of the week for a given date using Tomohiko Sakamoto's algorithm."""
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month:int, year:int) -> int:
    """Returns the maximum number of days in a given month, accounting for leap years."""
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if month == 2 and leap_year(year):
        return 29
    return days_in_month.get(month, 32)


def leap_year(year: int) -> bool:
    """Checks whether a given year is a leap year."""
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

def after(date: str) -> str:
    '''
    Calculates the date for the next day given a current date in YYYY-MM-DD format.

    Return the date for the next day of the given date in YYYY-MM-DD format.
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
    """Prints a usage message to the user and exits the script"""
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    print("Both dates must be valid and in the format YYYY-MM-DD.")
    print("The first date should be earlier than or equal to the second.")
    print("The program calculates the number of weekend days in the range.")
    sys.exit(1)


def valid_date(date: str) -> bool:
    """Validates whether a given string is a valid date in the format YYYY-MM-DD."""
    
    # Ensure the input length matches the expected format and contains hyphens at correct positions
    if len(date) != 10 or date[4:5] != '-' or date[7:8] != '-':
        return False

    try:
        # Break down the date string and convert parts to integers
        parts = date.split('-')
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])

        # Validate the month range
        if month < 1 or month > 12:
            return False

        # Validate the day based on the month's maximum days
        if day < 1 or day > mon_max(month, year):
            return False

        return True  # Date passed all checks
    except (ValueError, IndexError):
        # If splitting or conversion fails, the date is invalid
        return False


def day_count(start_date: str, stop_date: str) -> int:
    """Counts the number of weekend days (Saturday and Sunday) between two dates"""
    weekend_days = 0
    current_date = start_date
    
    while current_date != stop_date:
        year, month, day = map(int, current_date.split('-'))
        if day_of_week(year, month, day) in ['sat', 'sun']:
            weekend_days += 1
        current_date = after(current_date)
    
    # Check the stop date itself if it's a weekend day
    year, month, day = map(int, stop_date.split('-'))
    if day_of_week(year, month, day) in ['sat', 'sun']:
             weekend_days += 1
    
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