# Function to append data to an existing file
def append_to_file(filename, data):
    try:
        with open(filename, 'a') as file:
            file.write(data + '\n')
        print(f"Data appended to '{filename}' successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to display the entire contents of a file
def display_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Contents of '{filename}':\n{content}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Usage
filename = "data.txt"
append_data = "Data has been appended successfully and can be seen here."
append_to_file(filename, append_data)
display_file_contents(filename)
