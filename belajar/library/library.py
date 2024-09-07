from belajar.utils import read_file, book_lists, response_formater, clear_screen

program_running = True
while program_running:
    clear_screen()

    print(f'{"=" * 10} SELAMAT DATANG DI PERPUSTAKAAN {"=" * 10}')
    print("SILAHKAN PILIH MENU: ")
    print("1. LIST BUKU")
    print("2. CARI JUDUL BUKU")
    print("3. EXIT")

    menu_input = input("INSERT MENU 1/2/3: ")

    if menu_input not in ["1", "2", "3"]:
        print("Invalid Input")

    match menu_input:
        case "1":
            books = read_file("books.txt")
            response_formater(books, "BOOK LISTS")
            continue
        case "2":
            search_book = input("Insert book title: ").lower().split()
            books = book_lists("books.txt")

            if ''.join(search_book).isdigit():
                print("Invalid input, please enter a valid book title.")


            print("Books found: ")
            found_books = False
            for book in books:
                if all(word in book.lower() for word in search_book):
                    print("=>", book)
                    found_books = True

            if not found_books:
                print("No matching books found.")
            continue
        case "3":
            program_running = False
            print("PROGRAM EXIT")
            break
