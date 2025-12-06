from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum

class StatusChamado(str, enum.Enum):
    pendente = "pendente"
    em_andamento = "em_andamento"
    resolvido = "resolvido"
    recusado = "recusado"

class TipoSolicitacao(str, enum.Enum):
    alteracao = "alteracao"
    exclusao = "exclusao"

class Chamado(Base):
    __tablename__ = "chamados"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=False)
    tipo = Column(Enum(TipoSolicitacao), nullable=False)
    status = Column(Enum(StatusChamado), default=StatusChamado.pendente)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    usuario = relationship("Usuario")
