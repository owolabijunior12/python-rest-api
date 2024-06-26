
from pydantic import BaseModel
# creating a class has the model 
# use the BaseModel as the parameter
class BookModel(BaseModel):
    id: int
    name: str
    author: str
    year:int