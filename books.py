from fastapi import FastAPI
from fastapi.params import Body

app=FastAPI()
BOOKS=[{'title':'Title One','Author':'Author One','category':'science'},
       {'title':'Title two','Author':'Author two','category':'science'},
       {'title':'Title three','Author':'Author three','category':'history'},
       {'title':'Title four','Author':'Author four','category':'math'},
       {'title':'Title five','Author':'Author five','category':'math'},
       {'title':'Title six','Author':'Author two','category':'math'}]
@app.get("/books")
async def read_all_books():
    return BOOKS
@app.get("/books/mybook")
async def read_all_books():
    return {'book title':'My favorite  Book'}
#@app.get("/books/{dynamic_param}")
#async def read_all_books(dynamic_param: str):
    return {'dynamic_param':dynamic_param}
@app.get("/books/{book_title}")
async def read_books(book_title:str):
       for book in BOOKS:
              if  book.get('title').casefold() == book_title.casefold():
                     return book

@app.get("/books/{book_author}/")
async def read_author_catagory(book_author:str,book_category:str):
    return_book=[]
    for book in BOOKS:
        if book.get('Author').casefold() == book_author.casefold() and book.get('category').casefold() == book_category.casefold():
            return_book.append(book)
    return return_book
@app.post("/books/create_book/")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
from fastapi import Body

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break