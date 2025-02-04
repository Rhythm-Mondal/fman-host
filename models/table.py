from typing import Any
from datetime import datetime
from enum import Enum
from uuid import UUID
from pydantic import BaseModel, Field, field_validator, EmailStr, AnyHttpUrl


class User(BaseModel):
    id: UUID
    email: EmailStr | None = None
    phone: str | None = None
    name: str | None = None
    avatar: AnyHttpUrl | None = None
    color: int | None = None


class DocType(Enum):
    DIR = "directory"
    FILE = "file"


class DocObject(BaseModel):
    id: UUID
    name: str
    type: DocType
    created: datetime
    last_updated: datetime
    storage_info: dict[str, Any] | None = None

