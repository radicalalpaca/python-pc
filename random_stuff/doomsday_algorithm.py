"""Bad implementation of Conway's Doomsday algorithm."""

import math

days = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday"
]
months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]


def main():
    """
Main block.
    """
    year = year_input()
    leap_year = get_leap_year(year)
    month = month_input()
    day = day_input(leap_year, month)
    year_doomsday = calculate_year_doomsday(year)
    date = get_date(year, month, day, year_doomsday, leap_year)
    day_of_week = get_day(date)
    print(f"The date on {day}/{month}/{year} was {day_of_week}.")


def year_input():
    """
Takes input year from user.
    :return: year
    """
    while True:
        year_input_var = input("Enter year here: ")
        if not year_input_var.isdigit():
            print("Year must be a positive number.")
        else:
            year = int(year_input_var)
            if year < 0:
                print("Year must be a positive number")
            else:
                return year


def get_leap_year(year):
    """
Determines whether input year is a leap year or not.
    :param year:
    :return: Bool
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def month_input():
    """
Takes input month from user.
    :return: month
    """
    while True:
        month_input_var = input("Enter month here: ")
        if not month_input_var.isdigit():
            if month_input_var.lower() not in months:
                print("That is not a valid month.")
            else:
                month = months.index(month_input_var.lower()) + 1
                return month
        else:
            month = int(month_input_var)
            if month > 12 or month < 1:
                print("Month must be between 1 and 12.")
            else:
                return month


def day_input(leap_year, month):
    """
Takes day input from user.
    :param leap_year: Bool
    :param month: Int
    :return: day
    """
    while True:
        day_input_var = input("Enter day here: ")
        if not day_input_var.isdigit():
            print("Day must be a number between 1 and 31.")
        else:
            day = int(day_input_var)
            if day > 31 or day < 1:
                print("Day must be between 1 and 31.")
            elif leap_year and month == 2 and day > 29:
                print("Day must be between 1 and 29.")
            elif (not leap_year) and month == 2 and day > 28:
                print("Day must be between 1 and 28.")
            elif (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
                print("Day must be between 1 and 30.")
            else:
                return day


def calculate_year_doomsday(year):
    """
Calculates anchor day for a given year.
    :param year: Int
    :return: day (0 - 6)
    """
    day = (2 + year + math.floor(year / 4) - math.floor(year / 100)
           + math.floor(year / 400))
    return day % 7


def get_date(year, month, day, year_doomsday, leap_year):
    if month == 1 and leap_year:
        difference = int(abs((day - 4)) % 7)
        date = int((difference + year_doomsday) % 7)
        return date
    elif month == 1:
        difference = int(abs((day - 3)) % 7)
        date = int((difference + year_doomsday) % 7)
        return date
    elif month == 2 and leap_year:
        difference = int(abs((day - 29)) % 7)
        date = int((difference + year_doomsday) % 7)
        return date
    elif month == 2:
        difference = int(abs((day - 28)) % 7)
        date = int((difference + year_doomsday) % 7)
        return date
    elif month == 3:
        difference = int((day) % 7)
        date = int((difference + year_doomsday) % 7)
        return date
    elif month == 4:
        difference = int(abs((day - 4)) % 7)
        date = int((difference + year_doomsday) % 7)
        return date
    elif month == 5:
        difference = int(abs((day - 9)) % 7)
        date = int((difference + year_doomsday) % 7)
        return date
    elif month == 6:
        difference = int(abs((day - 6)) % 7)
        date = int((difference + year_doomsday) % 7)
        return date
    elif month == 7:
        difference = int(abs((day - 11)) % 7)
        date = int((difference + year_doomsday) % 7)
        return date
    elif month == 8:
        difference = int(abs((day - 8)) % 7)
        date = int((difference + year_doomsday) % 7)
        return date
    elif month == 9:
        difference = int(abs((day - 5)) % 7)
        date = int((difference + year_doomsday) % 7)
        return date
    elif month == 10:
        difference = int(abs((day - 10)) % 7)
        date = int((difference + year_doomsday) % 7)
        return date
    elif month == 11:
        difference = int(abs((day - 7)) % 7)
        date = int((difference + year_doomsday) % 7)
        return date
    else:
        difference = int(abs((day - 12)) % 7)
        date = int((difference + year_doomsday) % 7)
        return date


def get_day(date):
    return days[date].capitalize()


main()
