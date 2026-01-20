from fastapi import APIRouter, Depends, status, Request, Body
from sqlalchemy.orm import Session
from core.database import get_db
from features.products import schemas
from features.products.services import ProductService as product_service
from .schemas import ProductOut, ProductIn
from common.schemas import BaseAPIResponseModel
from common.base_responses import BaseAPIResponse
from uuid import UUID

router = APIRouter()

@router.get('', response_model=BaseAPIResponseModel[list[ProductOut]], status_code=status.HTTP_200_OK)
def get_products(db: Session = Depends(get_db), request: Request = None) -> BaseAPIResponseModel[list[ProductOut]]: 
    
    products = product_service.get_all_products(db)
    
    return BaseAPIResponse.success(
        request=request,
        data=[p.model_dump(mode='json') for p in products],  # serialize to json
        message='Products retrieved successfully'
    )


@router.post('', response_model=BaseAPIResponseModel[ProductOut], status_code=status.HTTP_201_CREATED)
def create_product(product_in: ProductIn = Body(...), db: Session = Depends(get_db), request: Request = None)-> BaseAPIResponseModel[ProductOut]:
    
    product = product_service.create_product(db, product_in)
    
    return BaseAPIResponse.success(
        request=request,
        data=product.model_dump(mode='json'),
        message='Product created successfully'
    )

@router.get('/{product_id}', response_model=BaseAPIResponseModel[ProductOut], status_code=status.HTTP_200_OK)
def get_product_by_id(product_id: UUID, db: Session = Depends(get_db), request: Request = None) -> BaseAPIResponseModel[ProductOut]:
    
    product = product_service.get_product_by_id(db, product_id)
    
    return BaseAPIResponse.success(
        request= request,
        data=product.model_dump(mode='json'),
        message=f'Product with ID: {product_id} retrived successfully'
    )
    
@router.patch('/{product_id}', response_model=BaseAPIResponseModel[ProductOut], status_code=status.HTTP_200_OK)
def update_product(product_id: UUID, product_in: schemas.ProductUpdate = Body(...), db: Session = Depends(get_db), request: Request = None) -> BaseAPIResponseModel[ProductOut]:
    
    product = product_service.update_product(db, product_id, product_in)
    
    return BaseAPIResponse.success(
        request=request,
        data= product.model_dump('json'),
        message=f'Product with ID: {product_id} updated successfully'
    )
    
@router.delete("/{product_id}", response_model=None)
def delete_product(product_id: UUID, db: Session = Depends(get_db), request: Request = None):
    
    product_service.delete_product(db, product_id)

    return BaseAPIResponse.success(
        request=request,
        data=None, 
        message=f"Product deleted successfully"
    )
