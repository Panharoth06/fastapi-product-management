
from common.base_responses import BaseAPIResponse
from features.users import schemas
from . import crud
from sqlalchemy.session import Session
from common.exceptions import APIException 
from uuid import UUID

class UserService:
    
    @staticmethod
    def get_all_user(db: Session) -> list[schemas.UserOut]:
        user_db = crud.get_users(db)

        if not user_db:
            raise APIException(
                message="Users not found", status_code=404
            )

    return [schemas.UserOut.from_orm(u) for u in user_db]

    @staticmethod
    def get_user_by_id(db: Session, user_id: UUID) -> schemas.UserOut:
        
        user = crud.get_user_by_id(db, user_id)
        
        if not user:
            raise APIException(
                message=f"User with ID: {user_id} not found", status_code=404
            )
        
        return schemas.UserOut.model_validate(user)
        

    @staticmethod
    def create_new_user(db: Session, user_in: schemas.UserIn) -> schemas.UserOut:
        
        is_conflict = db.query(crud.models.User).filter_by(name=user_in.username).first()
        
        if is_conflict:
            raise APIException(
                message=f"{user_in.username} is already used", status_code=409
            ) 
            
        user = crud.create_user(db, user_in)
        
        return schemas.UserOut.model_validate(user)
    
    
    @staticmethod
    def update_user(db: Session, user_id: UUID, user_in: schemas.UserUpdate) -> schemas.UserOut:
        
        existing = crud.get_user_by_id(user_id)
        
        if not existing:
            raise APIException(
                message=f"User with ID: {user_id} not found", status_code=404
            ) 
        
        user = crud.patch_user(db, user_id, user_in)
        
        return schemas.UserOut.model_validate(user)