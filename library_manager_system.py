from abc import ABC, abstractmethod

class Readable(ABC):
    def __init__(self, name, year_of_release, type ):
        self.type = type
        self.name = name
        self.year_of_release = year_of_release

    def show_info(self):
        return f"Name: {self.name}, Year of release:{self.year_of_release}. "
    

class Book(Readable):
    def __init__(self, name, year_of_release, author, genre):
        super().__init__(name,year_of_release, "Book" )
        self.author = author
        self.genre = genre

    def show_info(self):
        return f"{super().show_info()} Author: {self.author}, Genre: {self.author}"
    

class Magazine(Readable):
    def __init__(self, name, year_of_release,month):
        super().__init__(name,year_of_release, "Magazine")
        self.authors = []
        self.month = month

    def add_author(self,name):
        self.authors.append(name)
        print("The author is added successfully ")
    
    def remove_by_author(self,name):
        for author in self.authors:
            if name == author:
                self.authors.remove(author)
                print("The author has been successfully removed.")
                return
        print("No author fiund with this name.")

    def show_authors(self):
        a = ""
        for author in self.authors:
            a += author + ", "
        return f"Authors: {a}"
    
    def has_author(self,name):
        if name not in self.authors:
            return False
        return True

    def show_info(self):
        return f"{super().show_info()} Author: {self.show_authors}, Month: {self.month}"
    
class Library:
    def __init__(self):
           self.readables = []

    def add_readable(self,readable):
            self.readables.append(readable)
            print("The readable has been added successfully.")
        
    def remove_readable_by_name(self,name):
            for readable in self.readables:
                if readable.name == name:
                    self.readables.remove(readable)
                    print("The readable has been successfully removed.")
                    return
            print("No readable found with that name.")

    def search_by_author(self,name):
            found_readables = []
            for readable in self.readables:
                if readable.type == "Book" and readable.author == name:
                    found_readables.append(readable)
                elif readable.type == "Magazine" and readable.has_author(name):
                    found_readables.append(readable)
            return found_readables
    
    def view_all_readables(self):
        if not self.readables:
            print("No readables in the library.")
        for readable in self.readables:
            print(readable.show_info())
        
def main_menu(Library):
    while True:
        print("1. Add readable.")
        print("2. Remove readable by name ") 
        print("3. Search by author.") 
        print("4. View all readables.")
        print("5. Exit.") 

        choice = input("Enter a choice.")  

        if choice == '1':
            print("1. Add Book")
            print("2. Add Magazine")
            choice2 = int(input("Choice: "))
            if choice2 == 1:
               name = input("Enter a name:")
               year_if_release = input("Enter a year of release:")
               author = input("Enter an author:")
               genre = input("Enter a genre: ")
               book = Book(name,year_if_release,author,genre)
               library.add_readable(book)
            elif choice2 == 2:
                name = input("Enter the name of the magazine: ")
                year_of_release = input("Enter the year of release: ")
                month = input("Enter the month: ")
                magazine = Magazine(name, year_of_release, month)
                library.add_readable(magazine)
                while True:
                    add_author = input("Do you want to add an author? (yes/no): ")
                    if add_author.lower() == 'yes':
                        author_name = input("Enter the author name: ")
                        magazine.add_author(author_name)
                    else:
                        break
        elif choice == '2':
            name = input("Enter the name of the readable to remove: ")
            library.remove_readable_by_name(name)
        elif choice == '3':
            author = input("Enter the author's name to search: ")
            found_readables = library.search_by_author(author)
            if found_readables:
                for readable in found_readables:
                    print(readable.show_info())
            else:
                print("No readables found for this author.")
        elif choice == '4':
            library.view_all_readables()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


library = Library()
main_menu(library)