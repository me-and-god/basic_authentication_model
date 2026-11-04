"""Database table model"""


from app.core.base import Base

from uuid import UUID
import uuid
from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__="users"

    id              : Mapped[UUID]  = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name            : Mapped[str]   = mapped_column(String, nullable=False)
    email           : Mapped[str]   = mapped_column( String, nullable=False, unique=True)
    hashed_password : Mapped[str]   = mapped_column(String, nullable= False, unique=False)
