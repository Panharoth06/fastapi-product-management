from sqlalchemy.orm import Session
from . import schemas, crud
from common.exceptions import APIException
from uuid import UUID


class ProductService:
    @staticmethod
    def create_product(
        db: Session, product_in: schemas.ProductIn
    ) -> schemas.ProductOut:
        # Check if product already exists
        existing = db.query(crud.models.Product).filter_by(name=product_in.name).first()
        if existing:
            raise APIException(
                message=f"Product with name '{product_in.name}' already exists",
                status_code=409,
            )

        product = crud.create_product(db, product_in)
        # Convert ORM object to Pydantic schema
        return schemas.ProductOut.model_validate(product)

    @staticmethod
    def get_all_products(db: Session) -> list[schemas.ProductOut]:
        products = crud.get_products(db)
        if not products:
            raise APIException(message="Products not found", status_code=404)

        # Convert list of ORM objects to list of Pydantic schemas
        return [schemas.ProductOut.from_orm(p) for p in products]

    @staticmethod
    def get_product_by_id(db: Session, product_id: UUID) -> schemas.ProductOut:
        product = crud.get_product_by_id(db, product_id)
        if not product:
            raise APIException(
                message=f"product with ID: {product_id} not found", status_code=404
            )

        return schemas.ProductOut.from_orm(product)

    @staticmethod
    def update_product(
        db: Session, product_id: UUID, product_in: schemas.ProductUpdate
    ) -> schemas.ProductOut:
        product = crud.get_product_by_id(db, product_id)

        if not product:
            raise APIException(
                message=f"Product with ID: {product_id} not found", status_code=404
            )

        product = crud.patch_product(db, product_id, product_in)
        return schemas.ProductOut.from_orm(product)

    @staticmethod
    def delete_product(db: Session, product_id: UUID) -> any:
        product = crud.get_product_by_id(db, product_id)
        if not product:
            raise APIException(
                message=f"Product with ID: {product_id} not found", status_code=404
            )

        return crud.delete_product(db, product_id)

