from sqlalchemy.orm import Session
from backend.db.schemas import company as schema
from backend.db.models import company as model


def get_company(db: Session, company_id: int):
    return db.query(model.Company).filter(model.Company.id == company_id).first()


def get_company_manager_by_email(db: Session, email: str):
    return db.query(model.CompanyManager).filter(model.CompanyManager.email == email).first()


def get_company_manager(db: Session, company_manager_id: int):
    return db.query(model.CompanyManager).filter(model.CompanyManager.id == company_manager_id).first()
