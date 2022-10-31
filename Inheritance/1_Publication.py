class Publication:
    def _init_(self, title, price):
        self.title = title
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Price:", self.price)

class Book(Publication):
    def _init_(self, title, price, pages):
        super()._init_(title, price)
        self.pages = pages

    def display(self):
        super().display()
        print("Pages:", self.pages)

class Lecture(Publication):
    def _init_(self, title, price, playtime):
        super()._init_(title, price)
        self.playtime = playtime

    def display(self):
        super().display()
        print("Playtime:", self.playtime)

T = input("Title: ")
P = input("Price: ")

Pub = Publication(T, P)
Pages = input("Number of pages: ")
B = Book(T, P, Pages)
Playtime = input("Playtime: ")
L = Lecture(T, P, Playtime)
print("\n")
print("OUTPUT: ")
B.display()
L.display()