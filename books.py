from fastapi import FastAPI, Body

app=FastAPI()

BOOKS=[
    {'title': "Harry Potter", 'author': "J.K. Rowling", 'category': "Fantasy"},
    {'title': "The Lord of the Rings", 'author': "J.R.R. Tolkien", 'category': "Fantasy"},
    {'title': "The Hobbit", 'author': "J.R.R. Tolkien", 'category': "Fantasy"},
    {'title': "A Game of Thrones", 'author': "George R.R. Martin", 'category': "Fantasy"},
    {'title': "The Catcher in the Rye", 'author': "J.D. Salinger", 'category': "Fiction"},
    {'title': "To Kill a Mockingbird", 'author': "Harper Lee", 'category': "Fiction"},
    {'title': "1984", 'author': "George Orwell", 'category': "Fiction"},
    {'title': "Animal Farm", 'author': "George Orwell", 'category': "Fiction"},
    {'title': "Brave New World", 'author': "Aldous Huxley", 'category': "Fiction"},
    {'title': "The Great Gatsby", 'author': "F. Scott Fitzgerald", 'category': "Fiction"},
    {'title': "The Da Vinci Code", 'author': "Dan Brown", 'category': "Mystery"},
    {'title': "Angels & Demons", 'author': "Dan Brown", 'category': "Mystery"}

]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{title}")
async def read_book(title: str):
    for book in BOOKS:
        if book.get('title') == title:
            return book
    return {"message": "Book not found"}


@app.get("/books/category/{category}")
async def read_book_by_category(category: str):
    books = []
    for book in BOOKS:
        if book.get('category').lower() == category.lower():
            books.append(book)
    return books

@app.get("/books/author/{author}")
async def read_book_by_author(author: str):
    books = []
    for book in BOOKS:
        if book.get('author').lower() == author.lower():
            books.append(book)
    return books

@app.get("/books/author/{author}/category/{category}")
async def read_book_by_author_and_category(author: str, category: str):
    books = []
    for book in BOOKS:
        if book.get('author').lower() == author.lower() and book.get('category').lower() == category.lower():
            books.append(book)
    return books

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return new_book

@app.put("/books/update_book/{title}")
async def update_book(title: str, updated_book=Body()):
    for book in BOOKS:
        if book.get('title') == title:
            book.update(updated_book)
            return book
    return {"message": "Book not found"}

@app.delete("/books/delete_book/{title}")
async def delete_book(title: str):
    for book in BOOKS:
        if book.get('title') == title:
            BOOKS.remove(book)
            return {"message": "Book deleted"}
    return {"message": "Book not found"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)


