from sqlalchemy.orm import Session
from app.models.chamado_model import Chamado
from app.schemas.chamado_schema import ChamadoCreate, ChamadoStatusUpdate


def criar_chamado(db: Session, chamado: ChamadoCreate, usuario_id: int):
    db_chamado = Chamado(
        tipo=chamado.tipo,
        descricao=chamado.descricao,
        titulo=chamado.titulo,
        usuario_id=usuario_id,
    )
    db.add(db_chamado)
    db.commit()
    db.refresh(db_chamado)
    return db_chamado


def listar_chamados(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Chamado).offset(skip).limit(limit).all()


def buscar_chamado_por_id(db: Session, chamado_id: int):
    return db.query(Chamado).filter(Chamado.id == chamado_id).first()


def atualizar_status_chamado(db: Session, chamado_id: int, status_data: ChamadoStatusUpdate):
    db_chamado = db.query(Chamado).filter(Chamado.id == chamado_id).first()
    if db_chamado:
        db_chamado.status = status_data.status
        db.commit()
        db.refresh(db_chamado)
    return db_chamado
