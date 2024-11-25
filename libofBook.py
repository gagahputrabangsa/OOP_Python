class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Title:   
 {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
# Create book objects
book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1954)
book2 = Book("Pride and Prejudice", "Jane Austen", 1813)
