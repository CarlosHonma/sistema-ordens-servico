from app import db
from datetime import datetime

class OrdemServico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='aberta')
    data_abertura = db.Column(db.DateTime, default=datetime.utcnow)
    data_fechamento = db.Column(db.DateTime)
    observacoes = db.Column(db.Text)

    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey('cliente.id'),
        nullable=False
    )
