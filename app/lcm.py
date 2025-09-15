# Find LCM (Least Common Multiple)
import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("LCM is:", abs(a * b) // math.gcd(a, b))
