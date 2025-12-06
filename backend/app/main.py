from fastapi import FastAPI
from app.database import Base, engine
from app.models import usuario_model  # importa para garantir criação da tabela
from app.models import fornecedor_model
from app.models import produto_model
from app.models import movimentacao_model
from app.models import chamado_model
from app.routers import chamado_router
from app.routers import fornecedor_router
from app.routers import produto_router
from app.routers import movimentacao_router
from app.routers import usuario_router


app = FastAPI(debug=True)

# Cria as tabelas no banco (se ainda não existirem)
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"mensagem": "API SIGE rodando"}

app.include_router(chamado_router.router)
app.include_router(fornecedor_router.router)
app.include_router(produto_router.router)
app.include_router(movimentacao_router.router)
app.include_router(usuario_router.router)
