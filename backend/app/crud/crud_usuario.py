from sqlalchemy.orm import Session
from app.models.usuario_model import Usuario
from app.schemas.usuario_schema import UsuarioCreate
from passlib.hash import pbkdf2_sha256  # Trocar bcrypt por pbkdf2_sha256

def criar_usuario(db: Session, usuario: UsuarioCreate):
    usuario_db = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=pbkdf2_sha256.hash(usuario.senha), # Usando pbkdf2_sha256
        perfil=usuario.perfil
    )
    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)
    return usuario_db

def listar_usuarios(db: Session):
    return db.query(Usuario).all()

def obter_usuario_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def excluir_usuario(db: Session, usuario_id: int):
    usuario = obter_usuario_por_id(db, usuario_id)
    if usuario:
        db.delete(usuario)
        db.commit()
    return usuario
