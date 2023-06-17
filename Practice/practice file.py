class Book:

    def __init__(self, title, author, num_pages, ISBN, publisher):
        self.title = title
        self.author = author
        self._num_pages = num_pages
        self._ISBN = ISBN
        self._publisher = publisher


book1 = Book("The Hobbit", "J.R.R. Tolkien", 310, "978-0-261-10235-4", "Allen & Unwin")
book2 = Book("The Fellowship of the Ring", "J.R.R. Tolkien", 423, "978-0-261-10236-1", "Allen & Unwin")
book3 = Book("The Two Towers", "J.R.R. Tolkien", 352, "978-0-261-10237-8", "Allen & Unwin")
book4 = Book("The Return of the King", "J.R.R. Tolkien", 416, "978-0-261-10238-5", "Allen & Unwin")
book5 = Book("The Silmarillion", "J.R.R. Tolkien", 365, "978-0-261-10239-2", "Allen & Unwin")

print(book1.title)
print(book1.author)
print(book1.num_pages)

