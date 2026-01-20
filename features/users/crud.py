from uuid import UUID
from sqlalchemy.orm.session import Session
from . import models, schemas


def get_users(db: Session):
    return db.query(models.User).all()


def get_user_by_id(db: Session, user_id: UUID) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str) -> models.User:
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user_in: schemas.UserIn) -> models.User:
    db_user = models.User(**user_in.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def patch_user(db: Session, user_id: UUID, user_in: schemas.UserUpdate):
    user = get_user_by_id(db, user_id)

    if not user:
        return None

    user_update = user_in.model_dump(exclude_unset=True)

    for key, value in user_update.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user


def update_password(db: Session, user_id: UUID, user_new_password: str):
    user = get_user_by_id(db, user_id)

    if not user:
        return None

    user.password = user_new_password

    db.commit()
    db.refresh(user)

    return user


def delete_user(db: Session, user_id: UUID):
    user = get_user_by_id(db, user_id)

    if not user:
        return None

    db.delete(user)
    db.commit()
