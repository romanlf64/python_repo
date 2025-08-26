def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
    
year = 1980
number = is_year_leap(year)

print(f"Год {year}: {number}")
                      