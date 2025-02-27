
### *4. Count Uppercase and Lowercase Letters in a String*

string = input("Enter a string: ")
upper = 0
lower = 0

for char in string:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)



