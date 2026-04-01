from app.models import db, Desafio, Dificuldade


def criar_desafio(nome, descricao, dificuldade):
    desafio = Desafio(
        nome=nome,
        descricao=descricao,
        dificuldade=Dificuldade(dificuldade)
    )

    db.session.add(desafio)
    db.session.commit()

    return desafio


def listar_desafios():
    return Desafio.query.all()


def buscar_desafio(desafio_id):
    return Desafio.query.get(desafio_id)


def deletar_desafio(desafio_id):
    desafio = buscar_desafio(desafio_id)

    if not desafio:
        return False

    db.session.delete(desafio)
    db.session.commit()
    return True