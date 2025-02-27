day = int(input("Day: "))
month = int(input("month (1-12): "))
months= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total = sum(months[:month-1]) + day
print("Day of the year:", total)