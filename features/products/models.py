from sqlalchemy import Column, Integer, String, Float, text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
import uuid
from core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(
        PG_UUID(as_uuid=True), 
        primary_key=True, 
        index=True, 
        default=uuid.uuid4,
        server_default=text("gen_random_uuid()")
    )
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=0)