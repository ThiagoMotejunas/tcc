from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.fornecedor_schema import FornecedorCreate, FornecedorOut
from app.crud import crud_fornecedor
from app.dependencies import get_db

router = APIRouter(prefix="/fornecedores", tags=["Fornecedores"])


@router.post("/", response_model=FornecedorOut, status_code=status.HTTP_201_CREATED)
def criar_fornecedor(fornecedor: FornecedorCreate, db: Session = Depends(get_db)):
    return crud_fornecedor.criar_fornecedor(db, fornecedor)


@router.get("/", response_model=List[FornecedorOut])
def listar_fornecedores(db: Session = Depends(get_db)):
    return crud_fornecedor.listar_fornecedores(db)


@router.get("/{fornecedor_id}", response_model=FornecedorOut)
def buscar_fornecedor(fornecedor_id: int, db: Session = Depends(get_db)):
    fornecedor = crud_fornecedor.buscar_fornecedor_por_id(db, fornecedor_id)
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado.")
    return fornecedor


@router.delete("/{fornecedor_id}", response_model=FornecedorOut)
def deletar_fornecedor(fornecedor_id: int, db: Session = Depends(get_db)):
    fornecedor = crud_fornecedor.deletar_fornecedor(db, fornecedor_id)
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado.")
    return fornecedor
