import cmath
a = int(input("Please enter a: "))
b = int(input("Please enter b: "))
c = int(input("Please enter c: "))

y = cmath.sqrt(b**2 - 4*a*c)
x1 = (-b + y) / (2*a)
x2 = (-b - y) / (2*a)

print(f"The solutions are: {x1} and {x2}")
