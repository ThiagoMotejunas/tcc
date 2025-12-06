from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    codigo = Column(String, nullable=False, unique=True)
    categoria = Column(String, nullable=True)
    preco = Column(Float, nullable=False)
    quantidade_estoque = Column(Integer, nullable=False)
    estoque_minimo = Column(Integer, nullable=False, default=5)  # Novo campo para o estoque mínimo
    descricao = Column(String, nullable=True)
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"))

    fornecedor = relationship("Fornecedor")

