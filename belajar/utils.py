import os

def read_file(filename):
    try:

        with open(filename, 'r') as file:
            data = file.read().strip().split("\n")
        return data

    except FileNotFoundError:

        print(f"Error: The file {filename} was not found.")
        return []

    except Exception as e:

        print(f"An unexpected error occurred: {e}")
        return []

def book_lists(filename):
    with open(filename, 'r') as file:
        book_titles = file.read().splitlines()
    return book_titles

def response_formater(data, label):
    print(f'''
    
{"=" * 10} {label} {"=" * 10}
{data}
{"=" * 10} {label} {"=" * 10}

''')

def clear_screen():
    if os.name != 'nt':
        os.system('clear')

    os.system('cls')

