def separate_even_odd(numbers):
    evenlist = []
    odd_list = []
    for num in numbers:

        if num % 2 == 0:
            evenlist.append(num)
        else:
            odd_list.append(num)
    return evenlist, odd_list

def merge_and_sort(list1, list2):
    merged_list = list1 + list2
    merged_list.sort()
    return merged_list

def update_and_delete(input_list, X_value):
    input_list[0] = X_value
    middle_index = len(input_list) // 2
    del input_list[middle_index]

def find_max_min(input_list):
    max_element = max(input_list)
    min_element = min(input_list)
    return max_element, min_element

def check_python_presence(names_list):
    return "python" in names_list

def main():
    numbers_list = []
    N = int(input("Enter the number of elements in the list: "))
    for i in range(N):
        num = int(input(f"Enter element {i + 1}: "))
        numbers_list.append(num)

    while True:
        print("\nMENU")
        print("1. Separate even and odd elements into two different lists")
        print("2. Merge and sort the two lists")
        print("3. Update first element with X value and delete the middle element of the list")
        print("4. Find max and min elements from the list")
        print("5. Add N names into the existing number list and check if the word 'python' is present in the list")
        print("6. Exit")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            even_nums, odd_nums = separate_even_odd(numbers_list)
            print("Even elements list:", even_nums)
            print("Odd elements list:", odd_nums)
        elif choice == 2:
            list1 = numbers_list.copy()
            list2 = [int(x) for x in input("Enter the elements for the second list separated by spaces: ").split()]
            merged_and_sorted_list = merge_and_sort(list1, list2)
            print("Merged and sorted list:", merged_and_sorted_list)
        elif choice == 3:
            X = int(input("Enter the value of X: "))
            update_and_delete(numbers_list, X)
            print("Updated list:", numbers_list)
        elif choice == 4:
            max_num, min_num = find_max_min(numbers_list)
            print("Max element:", max_num)
            print("Min element:", min_num)
        elif choice == 5:
            names_list = input("Enter N names separated by spaces: ").split()
            numbers_list.extend(names_list)
            print("Updated list:", numbers_list)
            python_present = check_python_presence(numbers_list)
            print("Is 'python' present in the list?", python_present)
        elif choice == 6:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-6).")

if __name__ == "__main__":
    main()
