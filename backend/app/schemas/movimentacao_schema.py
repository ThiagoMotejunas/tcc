from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class MovimentacaoCreate(BaseModel):
    tipo: Literal["entrada", "saida"]
    produto_id: int
    quantidade: int
    observacao: Optional[str] = None
    usuario_id: int

class MovimentacaoResponse(BaseModel):
    id: int
    tipo: str
    produto_id: int
    quantidade: int
    observacao: Optional[str]
    usuario_id: int
    data: datetime

    class Config:
        from_attributes = True
