from pydantic import BaseModel, ConfigDict
from typing import Optional


class UserOut(BaseModel):
    username: str
    email: str

    model_config = ConfigDict(
        from_attributes=True,
    )


class UserIn(BaseModel):
    username: str
    email: str
    password: str
    confirm_password: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None


class UserPasswordUpdate(BaseModel):
    old_password: str
    new_password: str
    confirm_new_password: str

