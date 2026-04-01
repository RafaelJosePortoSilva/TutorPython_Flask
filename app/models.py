from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum

db = SQLAlchemy()

class Dificuldade(enum.Enum):
    FACIL = "facil"
    MEDIO = "medio"
    DIFICIL = "dificil"

class Desafio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    dificuldade = db.Column(db.Enum(Dificuldade), nullable=False)

    casos_teste = db.relationship(
        'CasoTeste',
        backref='desafio',
        cascade="all, delete-orphan"
    )

class CasoTeste(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    desafio_id = db.Column(
        db.Integer,
        db.ForeignKey('desafio.id'),
        nullable=False
    )

    entrada = db.Column(db.Text, nullable=False)
    saida_esperada = db.Column(db.Text, nullable=False)
