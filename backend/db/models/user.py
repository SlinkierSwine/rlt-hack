import sqlalchemy as db
from backend.db.db import Base

class BaseUser(Base):
    __tablename__ = "base_users"

    id = db.Column(db.Integer, primary_key=True, index=True)
    email = db.Column(db.String, unique=True, index=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    middlename = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.sql.func.now())
    updated_at = db.Column(db.DateTime,  nullable=False, server_default=db.sql.func.now(), onupdate=db.sql.func.now())
    hashed_password = db.Column(db.String)
    is_active = db.Column(db.Boolean, default=True)

