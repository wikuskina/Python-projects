# leap year calculator
# leap year: has to be divided by 4 with no remainder, by or by 100 and 400 with no remainder
# if it can be divided by 100 with no remainder (but not by 400 at the same time) it is NOT a leap year
# returns True / False (leap / not leap)

def is_leap_year(year):
    year = int(year)
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

is_leap_year(1989)
