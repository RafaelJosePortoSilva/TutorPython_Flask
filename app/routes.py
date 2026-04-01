from flask import Blueprint, render_template, request, url_for, session,redirect
from app.service import desafio_svc
from app.service import juiz_svc

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def identificacao():
    if request.method == "POST":
        nome = request.form.get("nome-estudante")

        if nome:
            session["usuario"] = nome
            return redirect(url_for("main.index"))

    return render_template("identificacao.html")


@main.route("/home")
def index():
    if "usuario" not in session:
        return redirect(url_for("main.identificacao"))

    desafios = desafio_svc.listar_desafios()

    return render_template(
        "index.html",
        desafios=desafios,
        usuario=session["usuario"]
    )

@main.route("/desafio/<int:desafio_id>", methods=["GET", "POST"])
def ver_desafio(desafio_id):
    desafio = desafio_svc.buscar_desafio(desafio_id)

    if request.method == "POST":
        codigo = request.form.get("codigo")

        resultado = juiz_svc.rodar_testes(desafio_id, codigo)

        # tratar dicionario resultado

        return render_template(
            "desafio.html",
            desafio=desafio,
            resultado=resultado,
            codigo=codigo
        )

    return render_template("desafio.html", desafio=desafio)