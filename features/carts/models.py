from sqlalchemy import Column, Integer, Float, ForeignKey, text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from core.database import Base
import uuid

# Avoid circular imports by using string names in relationship() if needed,
# but importing the model for ForeignKey is fine if structure allows.
# from features.users.models import User
# from features.products.models import Product


class Cart(Base):
    __tablename__ = "carts"

    id = Column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid.uuid4,
        server_default=text("gen_random_uuid()"),
    )

    product_id = Column(
        PG_UUID(as_uuid=True), ForeignKey("products.id"), nullable=False
    )

    quantity = Column(Integer, default=1)
    total_price = Column(Float, nullable=False)
    user_id = Column(PG_UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    # Relationships
    # Using string 'User' allows avoiding circular imports if User is not imported at top
    user = relationship(
        "User", backref=backref("cart_items", cascade="all, delete-orphan")
    )

    # Added product relationship so we can do `cart_item.product.name`
    product = relationship("Product")
