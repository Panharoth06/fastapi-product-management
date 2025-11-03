from fastapi import FastAPI
from models import Product
from repository import products
from utils import find_product_by_id

app = FastAPI()

@app.get("/message")
def greet():
    return "Jg yy tha pg rean Fast API"


@app.get("/products")
def get_products():
    return products


@app.get('/products/{id}')
def get_product_by_id(id: int):
    return find_product_by_id(id)


@app.post('/products')
def add_product(product: Product):
    products.append(product)
    return product

@app.put('/products/{id}')
def update_product_by_id(id: int, update_request: Product):
    for index, p in enumerate(products):
        if p.id == id:
            products[index] = update_request
            return update_request
    return {"message": f"Product with ID {id} not found"}


@app.delete('/products/{id}')
def delete_product_by_id(id: int):
    for index, p in enumerate(products):
        if p.id == id:
            products.remove(p)
            return 'No content'
    return {"message": f"Product with ID {id} not found"}
