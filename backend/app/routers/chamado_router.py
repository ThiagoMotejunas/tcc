from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.chamado_schema import ChamadoCreate, ChamadoOut, ChamadoStatusUpdate
from app.crud import crud_chamado
from app.dependencies import get_db

router = APIRouter(prefix="/chamados", tags=["Chamados"])


@router.post("/", response_model=ChamadoOut, status_code=status.HTTP_201_CREATED)
def criar_chamado(
    chamado: ChamadoCreate,
    db: Session = Depends(get_db),
):
    # Para testes, fixamos usuario_id = 1. Você pode mudar conforme necessário.
    return crud_chamado.criar_chamado(db, chamado, usuario_id=1)


@router.get("/", response_model=List[ChamadoOut])
def listar_chamados(db: Session = Depends(get_db)):
    return crud_chamado.listar_chamados(db)


@router.get("/{chamado_id}", response_model=ChamadoOut)
def buscar_chamado(chamado_id: int, db: Session = Depends(get_db)):
    chamado = crud_chamado.buscar_chamado_por_id(db, chamado_id)
    if not chamado:
        raise HTTPException(status_code=404, detail="Chamado não encontrado.")
    return chamado


@router.patch("/{chamado_id}/status", response_model=ChamadoOut)
def atualizar_status_chamado(
    chamado_id: int,
    status_data: ChamadoStatusUpdate,
    db: Session = Depends(get_db),
):
    chamado = crud_chamado.atualizar_status_chamado(db, chamado_id, status_data)
    if not chamado:
        raise HTTPException(status_code=404, detail="Chamado não encontrado.")
    return chamado
