books = []
no_of_books = 0
val = 'Y'


def addBookToLib(val,no_of_books):
    while(val != 'N'):
        addBooks = input("Add Books: ")
        books.append(addBooks)
        no_of_books += 1
        print(books)
        val = input("Y for Continue, N for stop")
    return no_of_books

def checkBooksInLib(books, no_of_books):
    if(len(books) == no_of_books):
        print("The total number of books are same in lib")
    else:
        print("The books are not matching")

res = addBookToLib(val, no_of_books)
checkBooksInLib(books, res)