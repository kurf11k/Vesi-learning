class Library:
    def __init__(self, name_library):
        self.name_library = name_library
        
    def books(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
        return f"Jméno knihy: {self.name}\nAutor: {self.author}\nstran: {self.pages}"

    def save(self):
        return [f"{self.name_library}\n{self.books(self.name, self.author, self.pages)}"]


    def reader(self, name_reader, borrow_book):
        self.name_reader = name_reader
        self.borrow_book = borrow_book
        for i in range(len(all_books)):
            if borrow_book in all_books[i]:
                all_books.remove(all_books[i])
                print(f"Čtenář {self.name_reader} si půjčil knihu {self.borrow_book}")
                break
        return all_books


    def print_all_books_in_library(self):
        for i in all_books:
            print(i)
            print()


library_hranice = Library("KNIHOVNA HRANICE")
library_hranice.books("Malý Princ", "Antoine de Saint-Exupéry", 154)
book1 = library_hranice.save()

library_hranice = Library("KNIHOVNA HRANICE")
library_hranice.books("Romeo a Julie", "William Shakespeare", 187)
book2 = library_hranice.save()

library_hranice = Library("KNIHOVNA HRANICE")
library_hranice.books("Krysař", "Viktor Dyk", 204)
book3 = library_hranice.save()

library_hranice = Library("KNIHOVNA HRANICE")
library_hranice.books("Na západní frontě klid", "Erich Maria Remarque", 219)
book4 = library_hranice.save()

library_hranice = Library("KNIHOVNA HRANICE")
library_hranice.books("Zkrocení zlé ženy", "William Shakespeare", 130)
book5 = library_hranice.save()

all_books = book1 + book2 + book3 + book4 + book5


library_hranice.reader("Jakub Veselka", "Krysař")
library_hranice.reader("Martin Kurfürst", "Na západní frontě klid")
print()
print("Knihy v knihovně")
print()
library_hranice.print_all_books_in_library()