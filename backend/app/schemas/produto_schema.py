from pydantic import BaseModel
from typing import Optional


class ProdutoCreate(BaseModel):
    nome: str
    codigo: str
    categoria: Optional[str] = None
    preco: float
    quantidade_estoque: int
    estoque_minimo: int  
    descricao: Optional[str] = None
    fornecedor_id: int



class ProdutoUpdate(BaseModel):
    nome: Optional[str]
    codigo: Optional[str]
    categoria: Optional[str]
    preco: Optional[float]
    quantidade_estoque: Optional[int]
    descricao: Optional[str]
    fornecedor_id: Optional[int]


class ProdutoResponse(BaseModel):
    id: int
    nome: str
    codigo: str
    categoria: Optional[str]
    preco: float
    quantidade_estoque: int
    estoque_minimo: int  
    descricao: Optional[str]
    
    class Config:
        orm_mode = True

