# app/dependencies.py

from app.database import SessionLocal
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.models.usuario_model import Usuario
from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import get_db
from typing import Optional

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # apenas placeholder se ainda não estiver implementado

# Essa função fornece a sessão com o banco para os endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Placeholder até termos autenticação de fato
def get_current_user():
    # Por enquanto retorna um usuário "falso", apenas para testes
    fake_user = Usuario(id=1, nome="Admin", email="admin@example.com", senha="1234", tipo="admin")
    return fake_user


# Configurações de criptografia e tokens
SECRET_KEY = "secrectkey"  # Alterar para chave secreta mais forte
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Funções para autenticação e geração de tokens
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para gerar o token de acesso
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Função para verificar o token
def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise credentials_exception
