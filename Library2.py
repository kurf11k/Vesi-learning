import datetime

class Person:
    def __init__(self, name, lastname, birthdate):
        self.name = name
        self.lastname = lastname
        self.whole_name = f"{name} {lastname}"
        self.birthdate = birthdate
        
class Reader(Person):
    def __init__(self, name, lastname, birthdate):
        super().__init__(name, lastname, birthdate)
        self.borrowed_books = []
        
    def add_borrowed_book(self, book):
        self.borrowed_books.append(book)
    
    
class Author(Person):
    def __init__(self, name, lastname):
        super().__init__(name, lastname, None)         

class Borrowing:
    def __init__(self, book, reader):
        self.book = book
        self.reader = reader
        self.date = datetime.datetime.now()
        
class Book:
    def __init__(self, name, count_pages, author):
        self.name = name
        self.author = author
        self.count_pages = count_pages
        
    def show(self):
        print(f"Jméno knihy: {self.name} Autor: {self.author.whole_name} stran: {self.count_pages}")

class Library:
    def __init__(self, name, books = []):
        self.name = name
        self.books = books
        self.readers = []
        self.borrowings = []
    
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, book):
        self.books.remove(book)
    
    def show_all_books(self):
        for book in self.books:
            book.show()
            
    def add_reader(self, reader):
        self.readers.append(reader)
        
    def borrow_book(self, book, reader):
        new_borrowing = Borrowing(book, reader)
        self.borrowings.append(new_borrowing)
        
    def show(self):
        print(f"{self.name}")


libraries = []

def show_all_libraries():
    for lib in libraries:
            lib.show()
            
def add_new_library():
    pass


print("MENU")
print("1 - Seznam knihoven")
print("2 - Seznam knih")
print("3 - Seznam autorů")
print("4 - Přidat knihovnu")
print("5 - Přidat knihu")
print("6 - Smazat knihu")


while True:
    action = input("Zadej číslo akce, jež chceš provést: ")
    
    if action == "1" :
        show_all_libraries()
    
    elif action == "2":
        show_all_libraries
        lib = input("Vyberte knihovnu: ")
        ##dodělat zobrazení knih v knigovně
        
    elif action == "3":
        