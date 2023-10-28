class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
    def addBook(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)

    def showInfo(self):
        print(f'The library has {self.noBooks} books')
        for book in self.books:
            print('->' + book)

b1=Library()
b1.addBook('Five Feet Apart')
b1.addBook('The Last Summer')
b1.addBook('Midnight Sun')
b1.showInfo()
