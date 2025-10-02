from pydantic import BaseModel     #data validation

class product(BaseModel):
    id:int
    name:str
    description:str
    price:float
    quantity:int