class Publisher:
    pass
class Book(Publisher):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print("Title : ",self.title)
        print("Author : ",self.author)
class Python(Book):
    def __init__(self,title,author,price,no_of_pages):
        super().__init__(title,author)
        self.price=price
        self.no_of_pages=no_of_pages
    def display(self):
        print("BOOK Details")
        print("Title : ",self.title)
        print("Author : ",self.author)
        print("Price : ",self.price)
        print("No of Pages :",self.no_of_pages)

p=Python("The Alchemist","Paulo Coelho",200,179)
p.display()

















