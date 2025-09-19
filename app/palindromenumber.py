# Check palindrome number
num = int(input("Enter a number: "))
if str(num) == str(num)[::-1]:
    print("Palindrome Number")
else:
    print("Not Palindrome")
