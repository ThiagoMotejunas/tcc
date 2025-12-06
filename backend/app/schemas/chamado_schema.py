from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


# Enums usados no model
class TipoSolicitacao(str, Enum):
    alteracao = "alteracao"
    exclusao = "exclusao"


class StatusChamado(str, Enum):
    pendente = "pendente"
    em_andamento = "em_andamento"
    resolvido = "resolvido"


# Schema para criação de chamado
class ChamadoCreate(BaseModel):
    usuario_id: int
    titulo: str
    descricao: str
    tipo: TipoSolicitacao


# Schema para atualização de status
class ChamadoStatusUpdate(BaseModel):
    status: StatusChamado


# Schema de retorno
class ChamadoOut(BaseModel):
    id: int
    usuario_id: int
    titulo: str
    descricao: str
    tipo: TipoSolicitacao
    status: StatusChamado
    data_criacao: datetime

    class Config:
        from_attributes = True  # Pydantic v2 compatibility
