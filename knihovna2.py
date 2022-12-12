class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def show_name_library(self):
        return f"{self.name}"

    def add_book(self, name, author, pages):
        book = Book(name, author, pages)
        self.books.append(book)
        return book
    
    def show_books(self):
        print(self.name)
        print(self.books)
        
    def show_authors(self):
        print(self.name)
        pass

class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.name}/t{self.author}/t{self.pages}"

libraries = [] 

#Function

def list_library():
    print("Seznam knihoven")
    for index, lib in enumerate(libraries):
        print(f"{index + 1} - {lib.name}")


def input_to_library():
    choice = int(input("Zadej do jaké knihovny chceš vstoupit: "))
    for index, lib in enumerate(libraries):
        if choice == index + 1:
            library = lib

    while True:
        print("Seznam knih:")
        for index, b in enumerate(library.books):
            print(f"{index + 1}. {b.name} - {b.author} - {b.pages}")
        print()
        print("1 - Přidat knihu")
        print("2 - Smazat knihu")
        print("3 - Upravit knihu")
        print("4 - Zpět")
        choice = int(input("Vyber z možnosti: "))
        if choice == 1:
            name = input("Název knihy: ")
            autor = input("Jméno autora: ")
            pages = input("Počet stran: ")
            book = Book(name, autor, pages)
            library.books.append(book)

        elif choice == 2:
            choice = int(input("Vyber jakou knihu chceš smazat: "))
            for index, book in enumerate(library.books):
                if choice == index + 1:
                    library.books.remove(book)

        elif choice == 3:
            choice = int(input("Jakou knihu chceš upravit? "))
            for index, book in enumerate(library.books):
                if choice == index + 1:
                    print("1 - Název")
                    print("2 - Autor")
                    print("3 - Počet stran")
                    choice = int(input("Co chceš upravit? "))
                    if choice == 1:
                        book.name = input("Zadej nové jméno: ")
                    elif choice == 2:
                        book.author = input("Zadej nového autora: ")
                    elif choice == 3:
                        book.pages = input("Zadej nový počet stránek: ")
                    else:
                        print("Chyba")
                        break
        else:
            break


def add_library():
    newname = input("Zadej nový název knihovny: ")
    newname = Library(newname)
    libraries.append(newname)


def rename_library():
    delete = int(input("Zadej knihovnu, kterou chceš přepsat: "))
    for index, lib in enumerate(libraries):
        if index + 1 == delete:
            lib.name = input("Zadej nový název knihovny: ")


def delete_library():
    delete = int(input("Zadej knihovnu kterou chceš smazat: "))
    libraries.pop(delete - 1)

# Hlavní cyklus
def main_loop():
    while True:
        print("MENU")
        print("1 - Seznam knihoven")
        print("2 - Vstup do knihovny")
        print("3 - Přidat knihovnu")
        print("4 - Upravit název knihovny")
        print("5 - Smazat knihovnu")
        print("6 - Opustit MENU") 
        choice = input("Vyber z možnosti: ")
        
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
    # KNIHOVNA HRANICE
    libraryhranice = Library("Knihovna Hranice")
    hranicebook1 = libraryhranice.add_book("Kytice", "Karel Jaromír Erben", 219)
    hranicebook2 = libraryhranice.add_book("Hamlet", "William Shakespeare", 294)
    hranicebook3 = libraryhranice.add_book("Staré pověsti české", "Alois Jirásek", 235)
    hranicebook4 = libraryhranice.add_book("Máj", "Karel Hynek Mácha", 187)
    hranicebook5 = libraryhranice.add_book("Lakomec", "Molière", 262)
    hranicebook6 = libraryhranice.add_book("Král Lávra", "Karel Havlíček Borovský", 135)
    hranicebook7 = libraryhranice.add_book("Revizor", "Nikolaj Vasiljevič Gogol", 178)

    # KNIHOVNA OLOMOUC
    libraryolomouc = Library("Knihovna Olomouc")
    olomoucbook1 = libraryolomouc.add_book("Bílá Nemoc", "Karel Čapek", 217)
    olomoucbook2 = libraryolomouc.add_book("Romeo a Julie", "William Shakespeare", 175)
    olomoucbook3 = libraryolomouc.add_book("Bídníci", "Victor Hugo", 328)
    olomoucbook4 = libraryolomouc.add_book("Maryša", "Vilém Mrštík", 125)
    olomoucbook5 = libraryolomouc.add_book("Babička", "Božena Němcová", 365)

    libraries.append(libraryhranice)
    libraries.append(libraryolomouc)
    
    
    main_loop()
