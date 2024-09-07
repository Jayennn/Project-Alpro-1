from belajar.utils import read_file
import random


def main():
    khodam = read_file("lists.txt")
    if not khodam:
        return

    name = input("Enter your name: ")
    if not name:
        print("Name cannot be empty.")
        return

    if len(khodam) == 0:
        print("No khodam available.")

    result = khodam[random.randint(0, len(khodam) - 1)]
    print(f'''
Name: {name} 
Your khodam: {result}
''')

main()

if __name__ == '__main__':
    main()