import bot
from auxilio import AbrirAba, NumLockLigado
import sys
import logging


def NaTelaLogin():
    tela_login = 'img_movidesk/tela_login.png'
    posicao = bot.VerificarImagemExiste(tela_login)
    if posicao is not None:
        bot.Mensagem('Alerta', 'Usuário não está logado', 'Não Logado', 'OK')
        logging.debug('Usuário NÃO Logado')
        sys.exit()


def BotImprimirPDFTicket(lista_ticket, salvarem, velocidadepadrao):

    muitorapido = velocidadepadrao/20   # velocidadepadrao = 2 será 0.1
    rapido = velocidadepadrao/4         # velocidadepadrao = 2 será 0.5
    normal = velocidadepadrao           # velocidadepadrao = 2 será 2
    lento = velocidadepadrao*1.5        # velocidadepadrao = 2 será 3

    logging.debug('Iniciando')
    AbrirAba('https://loglabdigital.movidesk.com/Home', 2)

    NaTelaLogin()
    logging.debug('Usuário Logado')

    botao_localizar_titulo = 'img_movidesk/localizar_titulo.png'
    botao_opcoes = 'img_movidesk/opcoes.png'
    botao_imprimir_ticket = 'img_movidesk/imprimir_ticket.png'
    botao_imprimir = 'img_movidesk/imprimir.png'
    botao_salvar_pdf = 'img_movidesk/salvar_pdf.png'

    if NumLockLigado:
        origemNumLock = True
        bot.pressionar_tecla('numlock', 0, muitorapido)
        logging.debug('Num Lock Ligado, foi preciso desligar')
    else:
        origemNumLock = False
        logging.debug('Num Lock Desligado')

    primeiravez = True
    for ticket in lista_ticket:
        # bot.Localizar_Click_Imagem(
        #     botao_localizar_titulo, rapido, alterarhorizontal=-20)
        # logging.debug('Localizou a Lupa e Relógio')

        # if not primeiravez:
        #     bot.ClickMesmoLugar(rapido)
        #     bot.pressionar_tecla('home', 0, rapido)
        #     bot.pressionar_tecla_atalho('shiftleft', 'end', 0, rapido)
        #     bot.pressionar_tecla('del', 0, rapido)
        #     logging.debug(
        #         'Não é Primeria Vez, teve que dar mais um click para voltar caixa de seleção e apagar o selecionado')

        # bot.Preencher_Texto(ticket, 0)
        # bot.pressionar_tecla('enter', rapido, lento)
        # logging.debug('Pesquisou pelo Ticket')

        bot.pressionar_tecla_atalho('ctrlleft', 'space', rapido, normal)
        bot.Preencher_Texto(ticket, 0)
        bot.pressionar_tecla('enter', rapido, lento)
        logging.debug('Pesquisou pelo Ticket')

        bot.Localizar_Click_Imagem(botao_opcoes, tempoPos=rapido)
        bot.Localizar_Click_Imagem(botao_imprimir_ticket, tempoPos=normal)
        bot.Localizar_Click_Imagem(botao_imprimir, tempoPos=normal)
        bot.Localizar_Click_Imagem(botao_salvar_pdf, tempoPos=rapido)
        endereco = salvarem+ticket+'.pdf'
        bot.Preencher_Texto(endereco, rapido)
        bot.pressionar_tecla('enter', rapido, lento)
        logging.debug('Salvou o Arquivo')
        bot.pressionar_tecla('esc', rapido, rapido)
        bot.pressionar_tecla_atalho('altleft', 'w', rapido, normal)
        # primeiravez = False

    if origemNumLock:
        bot.pressionar_tecla('numlock', 0, 0.1)
