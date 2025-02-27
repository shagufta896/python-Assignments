day = int(input("Enter today's day: "))
month = int(input("Enter current month (1-12): "))
months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_left = months_days[month-1] - day
print("Days left in the month:", days_left)

 