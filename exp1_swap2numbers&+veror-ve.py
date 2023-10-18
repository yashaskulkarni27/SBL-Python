a = int(input("Enter the first number "))
b = int(input("Enter the second number "))

if a<0:
    print("number is negative")
elif a>0:
    print("number is positive")
else:
    print("number is 0")

print(a)
print(b)

temp = a
a = b
b = temp

print(f"1st no is {a}")
print(f"2nd no is {b}")