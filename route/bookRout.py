from fastapi import FastAPI
from typing import List
from model.bookModel import BookModel
from controller.bookController import getAllBooks,creatingNewBookData,delSingleBook,SingleBook,updateSingleBook
from model.bookModel import BookModel
from fastapi import HTTPException
from util.data import books


app = FastAPI()

@app.get("/api/book/v1/getAll", res_model =list[BookModel])
# getting all the books datas
def getAllBooks():
    return books

@app.get("/books/v1/getOne/{book_id}", res_model=BookModel)
# getting single book data
def SingleBook(book_id:int):
    book = next(
        (
            book for book in books 
            if book.id == book_id
        ),
        None
    )
    if book is None:
        raise HTTPException(statusCode = 404, details = "book not found")
    return book

@app.post("/api/book/v1/createOne", res_model=BookModel)
# create/saving a new data for a book
def creatingNewBookData(book: BookModel):
    book.id = books[-1].id + 1 if books else 1
    books.append(book)
    return book
    
