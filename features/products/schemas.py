from pydantic import BaseModel, Field
from typing import Optional

class ProductOut(BaseModel):
    product_id: int = Field(alias='id') 
    name: str
    description: str
    price: float
    quantity: int
    
    model_config = {
        "from_attributes": True,  # Important! Allows SQLAlchemy models to be returned directly
        "populate_by_name": True  # allows using `id` or `problem_id` when creating model
    }
    
class ProductIn(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    


