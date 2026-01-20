from sqlalchemy.orm import Session
from . import models, schemas
from uuid import UUID


def get_products(db: Session):
    return db.query(models.Product).all()


def get_product_by_id(db: Session, product_id: UUID):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def create_product(db: Session, product_in: schemas.ProductIn):
    db_product = models.Product(**product_in.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def patch_product(db: Session, product_id: UUID, product_in: schemas.ProductUpdate):
    product = get_product_by_id(db, product_id)

    if not product:
        return None

    update_product = product_in.model_dump(
        exclude_unset=True
    )  # only include provided fields

    for key, value in update_product.items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return product


def delete_product(db: Session, product_id: UUID):
    product = get_product_by_id(db, product_id)
    if not product:
        return None

    db.delete(product)
    db.commit()
    return product
