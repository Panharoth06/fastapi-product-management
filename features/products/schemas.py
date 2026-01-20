from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from uuid import UUID

class ProductOut(BaseModel):
    product_id: UUID = Field(alias="id")
    name: str
    description: str
    price: float
    quantity: int

    model_config = ConfigDict(
        from_attributes=True,  # allows ORM object parsing
        populate_by_name=True  # accepts alias names
    )
    
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
    


