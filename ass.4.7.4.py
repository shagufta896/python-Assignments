number = input("Enter a number: ")
digits = [int(d) for d in number]

# Difference between greatest and smallest digits
print("Difference:", max(digits) - min(digits))

