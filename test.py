
from fastapi import FastAPI
from book import Book

app = FastAPI()

books = [{"id": 1, "title": "Python Basics", "author": "Real P.", "pages": 635},
{"id": 2, "title": "Breaking the Rules", "author": "Stephen G.", "pages": 99},
{"id": 3, "title": "Python Advanced", "author": "Sindhu", "pages": 63},
{"id": 4, "title": "Analytics", "author": "Stephen G.", "pages": 80},
{"id": 5, "title": "Python practice", "author": "Real P.", "pages": 35},
{"id": 6, "title": "ML", "author": "Stephen G.", "pages": 19},
{"id": 7, "title": "DL", "author": "Real P.", "pages": 65},
{"id": 8, "title": "AI", "author": "Stephen G.", "pages": 26}]

@app.get("/")
def home():
    return {'message':'Hello'}

@app.get("/books")
def get_books(limit:int|None=None):
    '''Get all the books limited by optional count'''
    if limit:
        return {"books :":books[:limit]}
    return {"books: ":books}

@app.get("/books/{book_id}")
def get_book(book_id:int):
    """Get a specific book by ID."""
    for book in books:
        if book["id"]==book_id:
            return book
    return {"error":"book not found"}

@app.post("/books")
def create_book(book:Book):
    """Create a new book entry."""
    new_book = {
        "id":len(books)+1,
        "title":book.title,
        "author":book.author,
        "pages":book.pages
    }
    books.append(new_book)
    return new_book