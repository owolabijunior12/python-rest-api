# python REST Api using the FastAPi framework and uvicorn
# write for the CRUD

from fastapi import FastAPI, HTTPException 
from typing import List
import uvicorn
from model.bookModel import BookModel


# calling the FastAPI 
app = FastAPI()




if __name__ == '__main__':    
    uvicorn.run(app, host="0.0.0.0", port=1609)
