from app import create_app
from app.models import db, Desafio, CasoTeste, Dificuldade

app = create_app()

def criar_desafio(nome, descricao, dificuldade, casos):
    desafio = Desafio(
        nome=nome,
        descricao=descricao,
        dificuldade=dificuldade
    )

    db.session.add(desafio)
    db.session.flush()

    testes = [
        CasoTeste(
            desafio_id=desafio.id,
            entrada=str(caso["entrada"]),
            saida_esperada=str(caso["saida"])
        )
        for caso in casos
    ]

    db.session.add_all(testes)


with app.app_context():
    db.drop_all()
    db.create_all()

    desafios = [

        # 1
        {
            "nome": "Soma de dois números",
            "desc": "Retorne a soma de dois números.",
            "dif": Dificuldade.FACIL,
            "casos": [
                {"entrada": [2, 3], "saida": 5},
                {"entrada": [10, 5], "saida": 15},
            ]
        },

        # 2
        {
            "nome": "Número par",
            "desc": "Retorne True se o número for par.",
            "dif": Dificuldade.FACIL,
            "casos": [
                {"entrada": [2], "saida": True},
                {"entrada": [3], "saida": False},
            ]
        },

        # 3
        {
            "nome": "Dobro",
            "desc": "Retorne o dobro do número.",
            "dif": Dificuldade.FACIL,
            "casos": [
                {"entrada": [4], "saida": 8},
                {"entrada": [7], "saida": 14},
            ]
        },

        # 4
        {
            "nome": "Maior número",
            "desc": "Retorne o maior entre dois números.",
            "dif": Dificuldade.FACIL,
            "casos": [
                {"entrada": [2, 9], "saida": 9},
                {"entrada": [10, 3], "saida": 10},
            ]
        },

        # 5
        {
            "nome": "Fatorial",
            "desc": "Calcule o fatorial de um número.",
            "dif": Dificuldade.MEDIO,
            "casos": [
                {"entrada": [5], "saida": 120},
                {"entrada": [3], "saida": 6},
            ]
        },

        # 6
        {
            "nome": "Quadrado",
            "desc": "Retorne o quadrado do número.",
            "dif": Dificuldade.FACIL,
            "casos": [
                {"entrada": [3], "saida": 9},
                {"entrada": [6], "saida": 36},
            ]
        },

        # 7
        {
            "nome": "Soma lista",
            "desc": "Some todos os elementos da lista.",
            "dif": Dificuldade.MEDIO,
            "casos": [
                {"entrada": [[1,2,3]], "saida": 6},
                {"entrada": [[5,5]], "saida": 10},
            ]
        },

        # 8
        {
            "nome": "Tamanho string",
            "desc": "Retorne o tamanho da string.",
            "dif": Dificuldade.FACIL,
            "casos": [
                {"entrada": ["abc"], "saida": 3},
                {"entrada": ["python"], "saida": 6},
            ]
        },

        # 9
        {
            "nome": "Inverter string",
            "desc": "Retorne a string invertida.",
            "dif": Dificuldade.MEDIO,
            "casos": [
                {"entrada": ["abc"], "saida": "cba"},
                {"entrada": ["ola"], "saida": "alo"},
            ]
        },

        # 10
        {
            "nome": "Palíndromo",
            "desc": "Retorne True se for palíndromo.",
            "dif": Dificuldade.MEDIO,
            "casos": [
                {"entrada": ["arara"], "saida": True},
                {"entrada": ["python"], "saida": False},
            ]
        },

        # 11
        {
            "nome": "Maior da lista",
            "desc": "Retorne o maior valor da lista.",
            "dif": Dificuldade.MEDIO,
            "casos": [
                {"entrada": [[1,5,3]], "saida": 5},
                {"entrada": [[10,2]], "saida": 10},
            ]
        },

        # 12
        {
            "nome": "Menor da lista",
            "desc": "Retorne o menor valor da lista.",
            "dif": Dificuldade.MEDIO,
            "casos": [
                {"entrada": [[1,5,3]], "saida": 1},
                {"entrada": [[10,2]], "saida": 2},
            ]
        },

        # 13
        {
            "nome": "Multiplicação",
            "desc": "Multiplique dois números.",
            "dif": Dificuldade.FACIL,
            "casos": [
                {"entrada": [3,4], "saida": 12},
                {"entrada": [2,5], "saida": 10},
            ]
        },

        # 14
        {
            "nome": "Divisão inteira",
            "desc": "Retorne a divisão inteira.",
            "dif": Dificuldade.FACIL,
            "casos": [
                {"entrada": [7,2], "saida": 3},
                {"entrada": [9,3], "saida": 3},
            ]
        },

        # 15
        {
            "nome": "Número positivo",
            "desc": "Retorne True se positivo.",
            "dif": Dificuldade.FACIL,
            "casos": [
                {"entrada": [5], "saida": True},
                {"entrada": [-1], "saida": False},
            ]
        },

        # 16
        {
            "nome": "Contar vogais",
            "desc": "Conte quantas vogais há na string.",
            "dif": Dificuldade.MEDIO,
            "casos": [
                {"entrada": ["banana"], "saida": 3},
                {"entrada": ["xyz"], "saida": 0},
            ]
        },

        # 17
        {
            "nome": "Último elemento",
            "desc": "Retorne o último elemento da lista.",
            "dif": Dificuldade.FACIL,
            "casos": [
                {"entrada": [[1,2,3]], "saida": 3},
                {"entrada": [[5]], "saida": 5},
            ]
        },

        # 18
        {
            "nome": "Primeiro elemento",
            "desc": "Retorne o primeiro elemento da lista.",
            "dif": Dificuldade.FACIL,
            "casos": [
                {"entrada": [[1,2,3]], "saida": 1},
                {"entrada": [[9]], "saida": 9},
            ]
        },

        # 19
        {
            "nome": "Potência",
            "desc": "Calcule a potência (a^b).",
            "dif": Dificuldade.MEDIO,
            "casos": [
                {"entrada": [2,3], "saida": 8},
                {"entrada": [3,2], "saida": 9},
            ]
        },

        # 20
        {
            "nome": "Contar pares",
            "desc": "Conte quantos números pares há na lista.",
            "dif": Dificuldade.MEDIO,
            "casos": [
                {"entrada": [[1,2,3,4]], "saida": 2},
                {"entrada": [[2,2,2]], "saida": 3},
            ]
        },
    ]

    for d in desafios:
        criar_desafio(d["nome"], d["desc"], d["dif"], d["casos"])

    db.session.commit()

    print("🔥 Banco populado com 20 desafios!")