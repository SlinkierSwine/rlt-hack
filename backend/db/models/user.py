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

    user = db.orm.relationship("User", uselist=False, backref="base_user")
    company_moderator = db.orm.relationship("CompanyModerator", uselist=False, backref="base_user")


class User(Base):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, index=True)
    experience = db.Column(db.Integer, default=0)
    rating = db.Column(db.Integer, default=0)
    
    base_user_id = db.Column(db.Integer, db.ForeignKey("base_users.id"))
    current_tasl_id = db.Column(db.Integer, db.ForeignKey("tasks.id"))

