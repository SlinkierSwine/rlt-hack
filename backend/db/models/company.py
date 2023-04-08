import sqlalchemy as db
from backend.db.db import Base


class Company(Base):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String)

    company_moderators = db.orm.relationship("CompanyModerator",  backref="company")


class CompanyModerator(Base):
    __tablename__ = "company_moderators"

    id = db.Column(db.Integer, primary_key=True, index=True)
    
    base_user_id = db.Column(db.Integer, db.ForeignKey("base_users.id"))
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))

