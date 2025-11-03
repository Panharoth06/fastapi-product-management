from repository import products

def find_product_by_id(id: int):
    for p in products:
        if p.id == id:
            return p

    return f"Product with ID: {id} not found"
