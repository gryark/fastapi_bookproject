from fastapi import FastAPI, Body

app=FastAPI()

class Book:
    id: int
    title: str
    author: str
    category: str
    description: str
    rating: int

    def __init__(self, id, title, author, category, description, rating):
        self.id=id
        self.title=title
        self.author=author
        self.category=category
        self.description=description
        self.rating=rating


BOOKS=[
    Book(1, "Clean Code", "Robert C. Martin", "Programming", "A Handbook of Agile Software Craftsmanship", 4),
    Book(2, "Code Complete", "Steve McConnell", "Programming", "A Practical Handbook of Software Construction", 4),
    Book(3, "Design Patterns", "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides", "Programming", "Elements of Reusable Object-Oriented Software", 5),
    Book(4, "The Pragmatic Programmer", "Andrew Hunt, David Thomas", "Programming", "Your Journey to Mastery", 5),
    Book(5, "Structure and Interpretation of Computer Programs", "Harold Abelson, Gerald Jay Sussman", "Programming", "A Computer Science Classic", 5),
    Book(6, "Harry Potter", "J.K. Rowling", "Fantasy","Very good book", 5),
]

@app.get("/books")
async def read_all_books():
    return BOOKS