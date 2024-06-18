# Function for the print menu options
def print_menu():
    print('\n######################')
    print('1: (A)dd a new book.')
    print('2: Bo(r)row books.')
    print('3: Re(t)urn a book.')
    print('4: (L)ist all books.')
    print('5: E(x)it.')
    print('######################\n')


# Start function to perform a certain option based on the users selection
def start():
    x = input("Your selection: ").lower()
    letter_options = ["a", "r", "t", "l", "x"]
    number_options = ["1", "2", "3", "4", "5"]
    while x not in letter_options and x not in number_options:
        print("\nWrong selection! Please select a valid option")
        return print_menu(), start()

    if x == "a" or x == "1":
        option_1(allBooks)

    elif x == "r" or x == "2":
        option_2(allBooks, borrowed_isbn, borrowed_names, borrowed_books)

    elif x == "t" or x == "3":
        option_3(borrowed_isbn, borrowed_names, borrowed_books)

    elif x == "l" or x == "4":
        option_4(allBooks, borrowed_isbn)

    elif x == "x" or x == "5":
        option_5(allBooks, borrowed_isbn)


# Option 1 function to add a book to the library
def option_1(allBooks):
    # User input book name
    book_name = input(str("\nBook name: "))

    # Ensuring the book name is valid input
    while not book_name or "*" in book_name or "%" in book_name:
        print("Invalid book name!")
        book_name = input("\nBook name: ")
    else:
        author_name = input("\nAuthor name: ")
        edition = input("\nEdition: ")

        # Ensuring the edition is valid input
        while not edition.isdigit() or "." in edition:
            print("Invalid edition!")
            edition = input("\nEdition: ")
        else:
            isbn = input("\nISBN: ")

        # Ensuring the ISBN is valid input
        for books in allBooks:
            if isbn == books[0]:
                print("\nDuplicate ISBN is found! Cannot add the book.")
                return print_menu(), start()

        while not isbn.isdigit() or len(isbn) != 13:
            print("Invalid ISBN!")
            isbn = input("\nISBN: ")

        for books in allBooks:
            if isbn == books[0]:
                print("\nDuplicate ISBN is found! Cannot add the book.")
                return print_menu(), start()

            # Ensuring the ISBN by multiplying the digits by specific weight factor, and checking if the result is a
            # multiple by 10

            isbn_total = 0

            for i in range(0, 13):
                index = int(isbn[i])
                if i % 2 == 0:
                    isbn_total += index
                else:
                    isbn_total += index * 3

            while isbn_total % 10 != 0:
                print("\nInvalid ISBN!")
                return print_menu(), start()

            # Adding new book to library
            else:
                print("\nA new book is added successfully.")
                one_new_book = [isbn, book_name, author_name, edition, []]
                allBooks.append(one_new_book)
                return print_menu(), start()


# Existing books in the library
allBooks = [
    ['9780596007126', "The Earth Inside Out", "Mike B", 2, ['Ali']],
    ['9780134494166', "The Human Body", "Dave R", 1, []],
    ['9780321125217', "Human on Earth", "Jordan P", 1, ['David', 'b1', 'user123']]
]

# Lists to track the borrowed ISBNs, names, and books
borrowed_isbn = []
borrowed_names = []
borrowed_books = []


# Option 2 function to borrow books from the library
def option_2(allBooks, borrowed_isbn, borrowed_names, borrowed_books):
    # Input for the name of the borrower and search term
    name_of_borrower = input("\nEnter the borrower name: ")
    search_term = input("\nSearch term: ").lower()

    found_items = []
    book_found = False

    for book in allBooks:

        # Checking if the book is already borrowed
        if book[0] in borrowed_isbn:
            print("\nNo books found!")
            return print_menu(), start()

        # Checking for matches with the search term
        elif search_term.endswith("%") and book[1].lower().startswith(search_term[:-1]):
            found_items.append(book[1])
            borrowed_isbn.append(book[0])
            borrowed_books.append(book[1])
            borrowed_names.append(name_of_borrower)
            book_found = True

        # Checking for matches with the search term
        elif search_term.endswith("*") and search_term[:-1].lower() in book[1].lower():
            found_items.append(book[1])
            borrowed_books.append(book[1])
            borrowed_isbn.append(book[0])
            borrowed_names.append(name_of_borrower)
            book_found = True

        # Checking for an exact match with the search term
        elif search_term == book[1].lower():
            found_items.append(book[1])
            borrowed_isbn.append(book[0])
            borrowed_books.append(book[1])
            borrowed_names.append(name_of_borrower)
            book_found = True

    # For no books that match the search term
    if not book_found:
        print("\nNo books found!")
        return print_menu(), start()

    # Updating the list of borrower's names, allBooks, and book name
    for book in found_items:
        print("\n'{}' is borrowed!".format(book))
        for i in range(len(allBooks)):
            if allBooks[i][1] == book:
                allBooks[i][4].append(name_of_borrower)
    return print_menu(), start()


# Option 3 function to return a borrowed book
def option_3(borrowed_isbn, borrowed_names, borrowed_books):
    returned_isbn = input("\nISBN: ")

    # Checking if ISBN in borrowed books, and removing the borrowed books and isbn if being returned by user
    if returned_isbn in borrowed_isbn:
        index = borrowed_isbn.index(returned_isbn)
        returned_books = borrowed_books[index]
        returned_names = borrowed_names[index]
        borrowed_isbn.remove(returned_isbn)
        borrowed_books.remove(returned_books)
        borrowed_names.remove(returned_names)

        # Printing the returned book
        print("\n'{}' is returned.".format(returned_books))

    else:
        print("\nNo book is found!")
    return print_menu(), start()


# Option 4 function to list all the books and their availability status in the library
def option_4(allBooks, borrowed_isbn):
    for books in allBooks:
        availability = "[Available]"
        if books[0] in borrowed_isbn:
            availability = "[Unavailable]"

        print("---------------")
        print(availability)
        print("{} - {}".format(books[1], books[2]))
        print("E: {} ISBN: {}".format(books[3], books[0]))
        print("borrowed by: {}".format(books[4]))

    return print_menu(), start()


# Option 5 function to display the final list of books as the program exits
def option_5(allBooks, borrowed_isbn):
    print("\n$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
    for books in allBooks:
        availability = "[Available]"
        if books[0] in borrowed_isbn:
            availability = "[Unavailable]"

        print("---------------")
        print(availability)
        print("{} - {}".format(books[1], books[2]))
        print("E: {} ISBN: {}".format(books[3], books[0]))
        print("borrowed by: {}".format(books[4]))


print_menu()
start()
