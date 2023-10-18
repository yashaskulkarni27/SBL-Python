try:
    num = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

else:
    print("Division was successful.")

finally:
    print("Program execution is complete.")
