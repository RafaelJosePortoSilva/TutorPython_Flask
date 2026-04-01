from app.models import Desafio


def executar_codigo(codigo_usuario):
    """
    Executa o código do usuário e retorna a função definida.
    Espera que o usuário crie uma função chamada `solucao`
    """
    contexto = {}

    if codigo_usuario.find("import os") == True:
        print("Oh o espertinho ae")
        codigo_usuario=""

    try:
        exec(codigo_usuario, contexto)
        funcao = contexto.get("solucao")

        if not funcao:
            return None, "Função 'solucao' não definida"

        return funcao, None

    except Exception as e:
        return None, str(e)


def rodar_testes(desafio_id, codigo_usuario):
    desafio = Desafio.query.get(desafio_id)

    if not desafio:
        return {"erro": "Desafio não encontrado"}

    funcao, erro = executar_codigo(codigo_usuario)

    if erro:
        return {"erro": erro}

    resultados = []

    for caso in desafio.casos_teste:
        try:
            entrada = eval(caso.entrada)
            esperado = caso.saida_esperada

            resultado = funcao(*entrada)

            passou = str(resultado) == esperado

            resultados.append({
                "entrada": entrada,
                "esperado": esperado,
                "resultado": resultado,
                "passou": passou
            })

        except Exception as e:
            resultados.append({
                "erro": str(e),
                "passou": False
            })

    sucesso = all(r["passou"] for r in resultados if "passou" in r)

    return {
        "sucesso": sucesso,
        "resultados": resultados
    }