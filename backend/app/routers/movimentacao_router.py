from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.movimentacao_schema import MovimentacaoCreate, MovimentacaoResponse
from app.crud import crud_movimentacao
from typing import List
from app.models.movimentacao_model import Movimentacao


router = APIRouter(prefix="/movimentacoes", tags=["Movimentações"])

@router.post("/", response_model=MovimentacaoResponse)
def criar_movimentacao(movimentacao: MovimentacaoCreate, db: Session = Depends(get_db)):
    return crud_movimentacao.registrar_movimentacao(db, movimentacao)

@router.get("/movimentacoes/recentes", response_model=List[MovimentacaoResponse])
def movimentacoes_recentes(db: Session = Depends(get_db)):
    movimentacoes = db.query(Movimentacao).order_by(Movimentacao.data.desc()).limit(10).all()  # Últimas 10 movimentações
    return movimentacoes
