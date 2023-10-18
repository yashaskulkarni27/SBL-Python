import os
def list_files_in_directory():
    try:
        current_directory = os.getcwd()
        files = os.listdir(current_directory)
        print(f"Files in the current directory ({current_directory}):")
        for file in files:
            if os.path.isfile(file):
                print(file)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Usage
list_files_in_directory()
