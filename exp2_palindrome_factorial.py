def is_palindrome_number(number):
    number_str = str(number)
    return number_str == number_str[::-1]


def is_palindrome_string(string):
    return string == string[::-1]


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


while True:
    print("Menu:")
    print("1. Check if a number is a palindrome")
    print("2. Check if a string is a palindrome")
    print("3. Find the factorial of a number")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        number = int(input("Enter a number: "))
        if is_palindrome_number(number):
            print(f"{number} is a palindrome number.")
        else:
            print(f"{number} is not a palindrome number.")
    elif choice == "2":
        string = input("Enter a string: ")
        if is_palindrome_string(string):
            print(f'"{string}" is a palindrome string.')
        else:
            print(f'"{string}" is not a palindrome string.')
    elif choice == "3":
        num = int(input("Enter a number to find its factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial(num)
            print(f"The factorial of {num} is {result}")
    elif choice == "4":
        break
    else:
        print("Invalid choice")
