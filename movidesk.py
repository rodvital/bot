import bot
from auxilio import AbrirAba
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

    muitorapido = velocidadepadrao / 20   # velocidadepadrao = 2 será 0.1
    rapido = velocidadepadrao / 4         # velocidadepadrao = 2 será 0.5
    normal = velocidadepadrao           # velocidadepadrao = 2 será 2
    lento = velocidadepadrao * 1.5        # velocidadepadrao = 2 será 3

    logging.debug('Iniciando')
    AbrirAba('https://loglabdigital.movidesk.com/Home', 2)

    NaTelaLogin()
    logging.debug('Usuário Logado')

    botao_opcoes = 'img_movidesk/opcoes.png'
    botao_imprimir_ticket = 'img_movidesk/imprimir_ticket.png'
    botao_imprimir = 'img_movidesk/imprimir.png'
    botao_salvar_pdf = 'img_movidesk/salvar_pdf.png'

    for ticket in lista_ticket:
        bot.pressionar_tecla_atalho('ctrlleft', 'space', muitorapido, rapido)
        bot.Preencher_Texto(ticket, muitorapido)
        bot.pressionar_tecla('enter', rapido, lento)
        logging.debug('Pesquisou pelo Ticket')

        bot.Localizar_Click_Imagem(botao_opcoes, tempoPos=rapido)
        bot.Localizar_Click_Imagem(botao_imprimir_ticket, tempoPos=normal)
        bot.Localizar_Click_Imagem(botao_imprimir, tempoPos=normal)

        tela_login = 'img_movidesk/imprimir_impressora_erro.png'
        posicao = bot.VerificarImagemExiste(tela_login)
        if posicao is not None:
            bot.Mensagem(
                'Alerta', 'Configurar para Imprimir como PDF', 'Não é PDF', 'OK')
            logging.debug('Impressora não é PDF')
            return

        bot.Localizar_Click_Imagem(botao_salvar_pdf, tempoPos=rapido)
        endereco = salvarem + ticket + '.pdf'
        bot.Preencher_Texto(endereco, rapido)
        bot.pressionar_tecla('enter', rapido, lento)
        logging.debug('Salvou o Arquivo')
        bot.pressionar_tecla('esc', rapido, rapido)
        bot.pressionar_tecla_atalho('altleft', 'w', rapido, normal)

    bot.pressionar_tecla_atalho('ctrlleft', 'w', rapido, normal)
    bot.Mensagem('Alerta', 'Processo Finalizado', 'Finalizado', 'OK')
