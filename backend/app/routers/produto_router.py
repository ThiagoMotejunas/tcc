from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.models.produto_model import Produto
from app.schemas.produto_schema import ProdutoCreate, ProdutoUpdate, ProdutoResponse
from app.crud import crud_produto
from app.dependencies import get_db

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.post("/", response_model=ProdutoResponse, status_code=status.HTTP_201_CREATED)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return crud_produto.criar_produto(db, produto)

@router.get("/", response_model=List[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return crud_produto.listar_produtos(db)

@router.get("/{produto_id}", response_model=ProdutoResponse)
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = crud_produto.buscar_produto_por_id(db, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    return produto

@router.put("/{produto_id}", response_model=ProdutoResponse)
def atualizar_produto(produto_id: int, produto: ProdutoUpdate, db: Session = Depends(get_db)):
    produto_atualizado = crud_produto.atualizar_produto(db, produto_id, produto)
    if not produto_atualizado:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    return produto_atualizado

@router.delete("/{produto_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto_deletado = crud_produto.deletar_produto(db, produto_id)
    if not produto_deletado:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    return None

@router.get("/produtos/estoque-minimo", response_model=List[ProdutoResponse])
def produtos_estoque_minimo(db: Session = Depends(get_db)):
    produtos = db.query(Produto).filter(Produto.quantidade_estoque < Produto.estoque_minimo).all()
    return produtos
