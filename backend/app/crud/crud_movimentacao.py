from sqlalchemy.orm import Session
from app.models.movimentacao_model import Movimentacao, TipoMovimentacao
from app.models.produto_model import Produto
from app.schemas.movimentacao_schema import MovimentacaoCreate
from fastapi import HTTPException

def registrar_movimentacao(db: Session, movimentacao_data: MovimentacaoCreate):
    produto = db.query(Produto).filter(Produto.id == movimentacao_data.produto_id).first()

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")

    # Atualiza estoque
    if movimentacao_data.tipo == TipoMovimentacao.entrada:
        produto.quantidade_estoque += movimentacao_data.quantidade
    elif movimentacao_data.tipo == TipoMovimentacao.saida:
        if produto.quantidade_estoque < movimentacao_data.quantidade:
            raise HTTPException(status_code=400, detail="Estoque insuficiente.")
        produto.quantidade_estoque -= movimentacao_data.quantidade

    # Cria movimentação
    nova_movimentacao = Movimentacao(
        tipo=movimentacao_data.tipo,
        quantidade=movimentacao_data.quantidade,
        observacao=movimentacao_data.observacao,
        produto_id=movimentacao_data.produto_id,
        usuario_id=movimentacao_data.usuario_id
    )

    db.add(nova_movimentacao)
    db.commit()
    db.refresh(nova_movimentacao)
    return nova_movimentacao
