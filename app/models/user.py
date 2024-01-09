import uuid
from sqlmodel import Field, SQLModel
from typing import Optional


class UserBase(SQLModel):
    # We use UUID as the primary key
    username: str
    email: str
    password: str

    def __getitem__(self, item):
        return getattr(self, item)

class AdminUser(UserBase, table=True):
    id: str = Field(default_factory=uuid.uuid4, primary_key=True)
