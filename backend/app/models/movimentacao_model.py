from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum

class TipoMovimentacao(str, enum.Enum):
    entrada = "entrada"
    saida = "saida"

class Movimentacao(Base):
    __tablename__ = "movimentacoes"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(Enum(TipoMovimentacao), nullable=False)
    quantidade = Column(Integer, nullable=False)
    data = Column(DateTime(timezone=True), server_default=func.now())
    observacao = Column(String, nullable=True)

    produto_id = Column(Integer, ForeignKey("produtos.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    produto = relationship("Produto")
    usuario = relationship("Usuario")
