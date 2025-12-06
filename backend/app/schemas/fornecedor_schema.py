from pydantic import BaseModel, EmailStr
from typing import Optional

# Entrada (POST e futuramente PUT)
class FornecedorCreate(BaseModel):
    nome: str
    cnpj: str
    telefone: Optional[str] = None
    email: Optional[EmailStr] = None
    cep: Optional[str] = None
    logradouro: Optional[str] = None
    numero: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None


# Saída (Response Model)
class FornecedorOut(FornecedorCreate):
    id: int

    class Config:
        from_attributes = True
