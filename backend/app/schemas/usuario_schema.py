from pydantic import BaseModel, Field, EmailStr

class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str = Field(..., max_length=72)
    perfil: str 

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    perfil: str

    class Config:
        orm_mode = True
