year = int(input("Enter the year you want to check: "))

if ((year % 4 == 0) or (year % 400 == 0) and (year % 100 != 0)):
    print(f"{year} is the leap year")
else:
    print(f"{year} is not a leap year")