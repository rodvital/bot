from flask import render_template, redirect, flash, url_for, send_from_directory, request
from main import app
from vacinacuiaba import BotVacinaCuiaba
from movidesk import BotImprimirPDFTicket, regraExecucaoMovidesk
from auxilio import ArquivosPastaemLista, TextoemLista
import os


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
    texto_tickets = request.form.get('tickets')
    endereco = request.form.get('endereco')
    historico = request.form.get('historico')
    if not os.path.isdir(endereco):
        flash('O endereço informação não é um diretório na máquina')
    else:
        regra_exec = regraExecucaoMovidesk(texto_tickets, endereco, historico)
        lista_tickets = regra_exec['lista_tickets']
        if len(lista_tickets) > 20:
            flash('A lista tem mais de 20 tickets')
        elif len(lista_tickets) == 1 and lista_tickets[0] == '':
            flash('Nenhum item na lista de tickets')
        elif regra_exec['possuiArquivoPasta'] != '':
            flash(regra_exec['possuiArquivoPasta'])
        else:
            BotImprimirPDFTicket(
                regra_exec['lista_tickets'], endereco, regra_exec['precisahistorico'], 2)
    return redirect(url_for('index'))


@app.route('/static/<nome_arquivo>')
def imagem_static(nome_arquivo):
    return send_from_directory('static', nome_arquivo)
