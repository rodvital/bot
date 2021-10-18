from flask import render_template, redirect, flash, url_for, send_from_directory, request
from main import app
from vacinacuiaba import BotVacinaCuiaba
from movidesk import BotImprimirPDFTicket
from auxilio import ArquivosPastaemLista, TextoemLista


@app.route('/')
def index():
    return render_template('lista.html', titulo='RPA do Robozão')


@app.route('/vacina', methods=['POST', ])
def vacina():
    cpf = request.form['cpf']
    BotVacinaCuiaba(cpf)
    return redirect(url_for('index'))


@app.route('/PdfMovidesk', methods=['POST', ])
def PdfMovidesk():
    texto_tickets = request.form['tickets']
    endereco = request.form['endereco']
    if endereco[:-1] != '\\':
        endereco = endereco + '\\'
    lista_tickets = TextoemLista(texto_tickets)
    possui = ArquivosPastaemLista(
        endereco, lista_tickets)
    if possui != '':
        flash(possui)
    else:
        BotImprimirPDFTicket(lista_tickets, endereco, 2)
    return redirect(url_for('index'))


@app.route('/static/<nome_arquivo>')
def imagem_static(nome_arquivo):
    return send_from_directory('static', nome_arquivo)
