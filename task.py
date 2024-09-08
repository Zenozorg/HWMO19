class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class User:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"

book1 = Book("1984", "George Orwell")
book2 = Book("Brave New World", "Aldous Huxley")

user1 = User("Alice")
user2 = User("Bob")

print(book1)
print(book2)
print(user1)
print(user2)
