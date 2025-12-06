from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

# Recupera a URL do banco de dados
DATABASE_URL = os.getenv("DATABASE_URL")

# Cria o engine de conexão
engine = create_engine(DATABASE_URL)

# Cria a sessão local para interagir com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()
