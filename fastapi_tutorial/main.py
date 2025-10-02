from fastapi import FastAPI,Depends
from models import product
from database import engine, Sessionlocal
import database_models
from sqlalchemy.orm import Session

app= FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():  
    return "Welcome To Telusko Trac"

products=[
    product(id=1,name="phone",description="budget phone",price=1199,quantity=10),
    product(id=2,name="laptop",description="gaming laptop",price=1799,quantity=5),
    product(id=3,name="tv",description="budget tv",price=1499,quantity=3),
    product(id=4,name="pen",description="Blue ink pen",price=13,quantity=17)
]

def get_db():
    db= Sessionlocal()
    try:
        yield db
    finally:
        db.close()
    

def init_db():
    db=Sessionlocal()
    count=db.query(database_models.product).count
    if count==0:
        for product in products:
            db.add(database_models.product(**product.model_dump()))
        db.commit()
init_db()


@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products=db.query(database_models.product).all()
    return db_products
 
@app.get("/product/{id}")
def get_product_by_id(id:int, db: Session = Depends(get_db)):
    db_products=db.query(database_models.product).filter(database_models.product.id==id).first()
    if db_products:
        return db_products
        
    return "product not found"

@app.post("/product")               #Add product
def add_product(product:product, db:Session = Depends(get_db)):
    db.add(database_models.product(**product.model_dump()))
    db.commit()
    return products

@app.put("/product/{id}")                #update_product
def update_product(id:int, product:product, db: Session = Depends(get_db)):
    db_products=db.query(database_models.product).filter(database_models.product.id==id).first()
    if db_products:
        db_products.name=product.name
        db_products.description=product.description
        db_products.price=product.price
        db_products.quantity=product.quantity
        db.commit()
        return "Product updated" 
    else:
        return "No product found"

@app.delete("/product/{id}")             #delete_product
def delete_product(id:int, db: Session = Depends(get_db)):
    db_products=db.query(database_models.product).filter(database_models.product.id==id).first()
    if db_products:
        db.delete(db_products)
        db.commit()
        return "product Deleted "
    else:
        return "product Not found" 