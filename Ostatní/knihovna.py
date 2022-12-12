class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, name, author, pages):
        book = Book(name, author, pages)
        self.books.append(book)
        return book

class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

# KNIHOVNA HRANICE
libraryhranice = Library("Knihovna Hranice")
hranicebook1 = libraryhranice.add_book("Kytice", "Karel Jaromír Erben", 219)
hranicebook2 = libraryhranice.add_book("Hamlet", "William Shakespeare", 294)
hranicebook3 = libraryhranice.add_book("Staré pověsti české", "Alois Jirásek", 235)
hranicebook4 = libraryhranice.add_book("Máj", "Karel Hynek Mácha", 187)
hranicebook5 = libraryhranice.add_book("Lakomec", "Molière", 262)
hranicebook6 = libraryhranice.add_book("Král Lávra", "Karel Havlíček Borovský", 135)
hranicebook7 = libraryhranice.add_book("Revizor", "Nikolaj Vasiljevič Gogol", 178)
all_pages_hranice = hranicebook1.pages + hranicebook2.pages + hranicebook3.pages + hranicebook4.pages + hranicebook5.pages + hranicebook6.pages + hranicebook7.pages

# KNIHOVNA OLOMOUC
libraryolomouc = Library("Knihovna Olomouc")
olomoucbook1 = libraryolomouc.add_book("Bílá Nemoc", "Karel Čapek", 217)
olomoucbook2 = libraryolomouc.add_book("Romeo a Julie", "William Shakespeare", 175)
olomoucbook3 = libraryolomouc.add_book("Bídníci", "Victor Hugo", 328)
olomoucbook4 = libraryolomouc.add_book("Maryša", "Vilém Mrštík", 125)
olomoucbook5 = libraryolomouc.add_book("Babička", "Božena Němcová", 365)
all_pages_olomouc = olomoucbook1.pages + olomoucbook2.pages + olomoucbook3.pages + olomoucbook4.pages + olomoucbook5.pages

def hranice_authors():
    print("Autoři")
    print(f"1. {hranicebook1.author}")
    print(f"2. {hranicebook2.author}")
    print(f"3. {hranicebook3.author}")
    print(f"4. {hranicebook4.author}")
    print(f"5. {hranicebook5.author}")
    print(f"6. {hranicebook6.author}")
    print(f"7. {hranicebook7.author}")

def hranice_name_books():
    print("Název knih")
    print(f"1. {hranicebook1.name}")
    print(f"2. {hranicebook2.name}")
    print(f"3. {hranicebook3.name}")
    print(f"4. {hranicebook4.name}")
    print(f"5. {hranicebook5.name}")
    print(f"6. {hranicebook6.name}")
    print(f"7. {hranicebook7.name}")

def hranice_pages():
    print(hranicebook1.pages)
    print(hranicebook2.pages)
    print(hranicebook3.pages)
    print(hranicebook4.pages)
    print(hranicebook5.pages)
    print(hranicebook6.pages)
    print(hranicebook7.pages)
    print("Celkový počet stran", all_pages_hranice)

def hranice_books():
    print("Název knihy - Jméno autora - Počet stran")
    print(f"1. {hranicebook1.name} - {hranicebook1.author} - {hranicebook1.pages}")
    print(f"2. {hranicebook2.name} - {hranicebook2.author} - {hranicebook2.pages}")
    print(f"3. {hranicebook3.name} - {hranicebook3.author} - {hranicebook3.pages}")
    print(f"4. {hranicebook4.name} - {hranicebook4.author} - {hranicebook4.pages}")
    print(f"5. {hranicebook5.name} - {hranicebook5.author} - {hranicebook5.pages}")
    print(f"6. {hranicebook6.name} - {hranicebook6.author} - {hranicebook6.pages}")
    print(f"7. {hranicebook7.name} - {hranicebook7.author} - {hranicebook7.pages}")
    

def olomouc_authors():
    print("Autoři")
    print(f"1. {olomoucbook1.author}")
    print(f"2. {olomoucbook2.author}")
    print(f"3. {olomoucbook3.author}")
    print(f"4. {olomoucbook4.author}")
    print(f"5. {olomoucbook5.author}")

def olomouc_name_books():
    print("Název knih")
    print(f"1. {olomoucbook1.name}")
    print(f"2. {olomoucbook2.name}")
    print(f"3. {olomoucbook3.name}")
    print(f"4. {olomoucbook4.name}")
    print(f"5. {olomoucbook5.name}")

def olomouc_pages():
    print(olomoucbook1.pages)
    print(olomoucbook2.pages)
    print(olomoucbook3.pages)
    print(olomoucbook4.pages)
    print(olomoucbook5.pages)
    print("Celkový počet stran", all_pages_olomouc)

def olomouc_books():
    print("Název knihy - Jméno autora - Počet stran")
    print(f"1. {olomoucbook1.name} - {olomoucbook1.author} - {olomoucbook1.pages}")
    print(f"2. {olomoucbook2.name} - {olomoucbook2.author} - {olomoucbook2.pages}")
    print(f"3. {olomoucbook3.name} - {olomoucbook3.author} - {olomoucbook3.pages}")
    print(f"4. {olomoucbook4.name} - {olomoucbook4.author} - {olomoucbook4.pages}")
    print(f"5. {olomoucbook5.name} - {olomoucbook5.author} - {olomoucbook5.pages}")
   

while True:
    print("MENU")
    print("Seznam knihoven:")
    print("1 - Knihovna Hranice")
    print("2 - Knihovna Olomouc")
    print("3 - Opustit MENU")
    choice = input("Vyber z monžnosti ")
    if choice == "1":
        while True:
            print("Jsi v knihovně Hranice vyber z nabídky")
            print("1 - Zobrazit všechny názvy knih")
            print("2 - Zobrazit všechny autory")
            print("3 - Zobrazit počet stran")
            print("4 - Zobrazit všechny atributy")
            choice = input("Co chceš zobrazit? ")

            if choice == "1":
                hranice_name_books()
                print("1 - Zpět")
                print("2 - Opustit knihovnu")
                choice = input("Vyber z nabídky 1/2 ")
                if choice == "1":
                    continue
                else:
                    break
    
            elif choice == "2":
                hranice_authors()
                print("1 - Zpět")
                print("2 - Opustit knihovnu")
                choice = input("Vyber z nabídky 1/2 ")
                if choice == "1":
                    continue
                else:
                    break

            elif choice == "3":
                hranice_pages()
                print("1 - Zpět")
                print("2 - Opustit knihovnu")
                choice = input("Vyber z nabídky 1/2 ")
                if choice == "1":
                    continue
                else:
                    break
            elif choice == "4":
                hranice_books()
                print("1 - Zpět")
                print("2 - Opustit knihovnu")
                choice = input("Vyber z nabídky 1/2 ")
                if choice == "1":
                    continue
                else:
                    break
            
            else:
                print("Chyba! Zkus to znovu")
                continue


    elif choice == "2":
            while True:
                print("Jsi v knihovně Olomouc vyber z nabídky ")
                print("1 - Zobrazit všechny názvy knih")
                print("2 - Zobrazit všechny autory")
                print("3 - Zobrazit počet stran")
                print("4 - Zobrazit všechny atributy")
                choice = input("Co chceš zobrazit? ")

                if choice == "1":
                    olomouc_name_books()
                    print("1 - Zpět")
                    print("2 - Opustit knihovnu")
                    choice = input("Vyber z nabídky 1/2 ")
                    if choice == "1":
                        continue
                    else:
                        break
        
                elif choice == "2":
                    olomouc_authors()
                    print("1 - Zpět")
                    print("2 - Opustit knihovnu")
                    choice = input("Vyber z nabídky 1/2 ")
                    if choice == "1":
                        continue
                    else:
                        break

                elif choice == "3":
                    olomouc_pages()
                    print("1 - Zpět")
                    print("2 - Opustit knihovnu")
                    choice = input("Vyber z nabídky 1/2 ")
                    if choice == "1":
                        continue
                    else:
                        break
                elif choice == "4":
                    olomouc_books()
                    print("1 - Zpět")
                    print("2 - Opustit knihovnu")
                    choice = input("Vyber z nabídky 1/2 ")
                    if choice == "1":
                        continue
                    else:
                        break
                
                else:
                    print("Chyba! Zkus to znovu")
                    continue

    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Chyba! Zkus to znovu")
        continue



