class Library:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.libraries = []
        self.books = []

    def add_libraries(self, library):
        self.libraries.append(library)

        file = open(LIBRARY_PATH, mode="a", encoding='utf-8')
        file.write(f"{library.id};{library.name}\n")
        file.close()       

    def show_name_library(self):
        return f"{self.name}"

    def add_book(self, book):
        self.books.append(book)
        
        file = open(BOOKS_PATH, mode="a", encoding='utf-8')
        file.write(f"{book.id};{book.name};{book.author};{book.pages};{self.id}\n")
        file.close()        
    
    def show_books(self):
        print(self.name)
        print(self.books)
        
    def show_authors(self):
        print(self.name)
        pass

class Book:
    def __init__(self, id, name, author, pages):
        self.id = id
        self.name = name
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.name}/t{self.author}/t{self.pages}"

#Function

LIBRARY_PATH = "Libraries/libs"
BOOKS_PATH = "Libraries/books"


def find_book_id():
    max = 0
    for lib in libraries:
        for book in lib.books:
            if book.id > max:
                max = book.id
    return max + 1

def find_lib_id():
    max = 0
    for lib in libraries:
        if lib.id > max:
            max = lib.id
    return max + 1

def load_libraries():
    libs = []
    file = open(file=LIBRARY_PATH, mode="r", encoding='utf-8')
    for line in file:
        cols = line.split(";")
        new_lib = Library(cols[0], cols[1].replace("\n", ""))
        libs.append(new_lib)
    return libs

def load_books_to_libs(libs):
    file = open(file=BOOKS_PATH, mode="r", encoding="utf-8")
    for line in file:
        cols = line.split(";")
        new_book = Book(int(cols[0]), cols[1], cols[2], cols[3])
        for lib in libs:
            lib_id = cols[4].replace("\n", "")
            if lib.id == lib_id:
                lib.books.append(new_book)


libraries = load_libraries()
load_books_to_libs(libraries) 


def list_library():
    print("Seznam knihoven")
    for lib in libraries:
        print(f"{lib.id} - {lib.name}")


def input_to_library():
    choice = input("Zadej do jak?? knihovny chce?? vstoupit: ")
    for lib in libraries:
        if choice == lib.id:
            library = lib

    while True:
        print("Seznam knih:")
        for index, b in enumerate(library.books):
            print(f"{index + 1}. {b.id} - {b.name} - {b.author} - {b.pages}")
        print()
        print("1 - P??idat knihu")
        print("2 - Smazat knihu")
        print("3 - Upravit knihu")
        print("4 - Zp??t")
        choice = int(input("Vyber z mo??nosti: "))
        if choice == 1:
            id = find_book_id()
            name = input("N??zev knihy: ")
            autor = input("Jm??no autora: ")
            pages = input("Po??et stran: ")
            book = Book(id, name, autor, pages)
            library.add_book(book)

        elif choice == 2:
            delete = int(input("Vyber podle po??ad??, jakou knihu chce?? smazat: "))
            libraries.pop(delete - 1)

        elif choice == 3:
            choice = int(input("Jakou knihu podle po??ad??, chce?? upravit? "))
            for index, book in enumerate(library.books):
                if choice == index + 1:
                    print("1 - N??zev")
                    print("2 - Autor")
                    print("3 - Po??et stran")
                    choice = int(input("Co chce?? upravit? "))
                    if choice == 1:
                        book.name = input("Zadej nov?? jm??no: ")
                    elif choice == 2:
                        book.author = input("Zadej nov??ho autora: ")
                    elif choice == 3:
                        book.pages = input("Zadej nov?? po??et str??nek: ")
                    else:
                        print("Chyba")
                        break
        else:
            break


def add_library():
    id = find_lib_id()
    new_name = input("Zadej nov?? n??zev knihovny: ")
    new_library = Library(id, new_name)
    libraries.append(new_library)

def rename_library():
    delete = int(input("Zadej knihovnu, kterou chce?? p??epsat: "))
    for index, lib in enumerate(libraries):
        if index + 1 == delete:
            lib.name = input("Zadej nov?? n??zev knihovny: ")


def delete_library():
    delete = int(input("Vyber podle po??ad??, jakou knihu chce?? smazat: "))
    libraries.pop(delete - 1)

# Hlavn?? cyklus
def main_loop():    
    while True:
        print("MENU")
        print("1 - Seznam knihoven")
        print("2 - Vstup do knihovny")
        print("3 - P??idat knihovnu")
        print("4 - Upravit n??zev knihovny")
        print("5 - Smazat knihovnu")
        print("6 - Opustit MENU") 
        choice = input("Vyber z mo??nosti: ")
        
        if choice == "1":
            list_library()

        elif choice == "2":
            list_library()
            input_to_library()

        elif choice == "3":
            list_library()
            add_library()

        elif choice == "4":
            list_library()
            rename_library()   
        
            
        elif choice == "5":
            list_library()
            delete_library()

        elif choice == "6":
            break
        
        else:
            print("Chyba! Zkus to znovu")
            continue
    

if __name__ == "__main__":
    main_loop()