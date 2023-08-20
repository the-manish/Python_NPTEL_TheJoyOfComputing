#Most of the years that can be divided by 4 are leap years.
#Exception:Century years are not leap years unless they are divided by 400.
#if year is divisible by 400 then is_leap_year elseif year is divisible by100 then not_leap_year
#else if year is divisible by 4 then is_leap_year
#else not_leap_year

import random

year=random.randint(2000,2018)
print(year)
if (year%4==0 and year%100!=0 or year%400==0):
    print("Given year is a leap year")
else:
    print("Given year is not a leap year")
