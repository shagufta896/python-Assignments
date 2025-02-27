###  Convert a number to words:

def number_to_words(num):
    units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    if num < 10:
        return units[num]
    else:
        return "Number out of range (0-9)"

num = int(input("Enter a number (0-9): "))
print("Number in words:", number_to_words(num))
