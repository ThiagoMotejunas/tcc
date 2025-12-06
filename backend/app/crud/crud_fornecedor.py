from sqlalchemy.orm import Session
from app.models.fornecedor_model import Fornecedor
from app.schemas.fornecedor_schema import FornecedorCreate


def criar_fornecedor(db: Session, fornecedor: FornecedorCreate):
    novo_fornecedor = Fornecedor(**fornecedor.model_dump())
    db.add(novo_fornecedor)
    db.commit()
    db.refresh(novo_fornecedor)
    return novo_fornecedor


def listar_fornecedores(db: Session):
    return db.query(Fornecedor).all()


def buscar_fornecedor_por_id(db: Session, fornecedor_id: int):
    return db.query(Fornecedor).filter(Fornecedor.id == fornecedor_id).first()

def deletar_fornecedor(db: Session, fornecedor_id: int):
    fornecedor = db.query(Fornecedor).filter(Fornecedor.id == fornecedor_id).first()
    if not fornecedor:
        return None
    db.delete(fornecedor)
    db.commit()
    return fornecedor