from app.models import db, CasoTeste, Desafio


def adicionar_caso_teste(desafio_id, entrada, saida_esperada):
    desafio = Desafio.query.get(desafio_id)

    if not desafio:
        return None

    caso = CasoTeste(
        desafio_id=desafio_id,
        entrada=entrada,
        saida_esperada=saida_esperada
    )

    db.session.add(caso)
    db.session.commit()

    return caso


def listar_casos(desafio_id):
    return CasoTeste.query.filter_by(desafio_id=desafio_id).all()


def deletar_caso(caso_id):
    caso = CasoTeste.query.get(caso_id)

    if not caso:
        return False

    db.session.delete(caso)
    db.session.commit()
    return True