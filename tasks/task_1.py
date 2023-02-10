def calculate(days):
    YEAR = 365
    WEEK = 7
    years = days // YEAR
    days %= YEAR
    weeks = days // WEEK
    days %= WEEK
    return years, weeks, days


input_days = int(input("Enter days: "))
years, weeks, days = calculate(input_days)
print(f"Years: {years}")
print(f"Weeks: {weeks}")
print(f"Days: {days}")