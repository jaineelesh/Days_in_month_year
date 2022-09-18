# 1. take month and year input from user
# 2. if month is february, check if year is leap year(29) or not(28)
# 3. else: get the days from db and display the result

def is_leap_year(year):
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


def no_of_days(month, year):
    if month == "feb":
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        if month == "jan" or month == "mar" or month == "may" or month == "jul" or month == "aug" or month == "oct" or month == "dec":
            return 31
        else:
            return 30


month = input("please enter the month: ")[0:3].lower()
year = int(input("please enter the year: "))

print(no_of_days(month, year))
