import webbrowser
import bot
from time import sleep

newtab = 2  # open in a new tab, if possible

# url = "https://cadastro.vacinacuiaba.com.br/"
# webbrowser.open(url, newtab)
# sleep(2)  # carregar


# botao_fechar = 'imagens/fechar.png'
# botao_consultar = 'imagens/consultar.png'
# texto_cpf = 'imagens/cpf.png'
# cpf = '89409876168'


# bot.Localizar_Click_Imagem(botao_fechar, 0.5)
# bot.Localizar_Click_Imagem(botao_consultar, 2)
# bot.Preencher_Texto_Localizar_Imagem(texto_cpf, 0.5, cpf)

url = "https://loglabdigital.movidesk.com/Ticket"
webbrowser.open(url, newtab)
sleep(2)  # carregar

botao_localizar_titulo = 'imagens/localizar_titulo.png'
botao_opcoes = 'imagens/opcoes.png'
botao_imprimir_ticket = 'imagens/imprimir_ticket.png'
botao_imprimir = 'imagens/imprimir.png'
botao_salvar_pdf = 'imagens/salvar_pdf.png'

salvarem = 'f:\\Downloads\\teste_ticket\\'

# tem que fazer uma verificação se numlock está ligado.. pois tem que rodar com ele desligado.
bot.pressionar_tecla('numlock', 0, 0.1)
tickets = ['21166', '21167']
primeiravez = True
for ticket in tickets:
    bot.Localizar_Click_Imagem(
        botao_localizar_titulo, 0.5, alterarhorizontal=-20)
    if not primeiravez:
        bot.ClickMesmoLugar(0.5)
    bot.pressionar_tecla('home', 0, 0.5)
    bot.pressionar_tecla_atalho('shiftleft', 'end', 0, 0.5)
    bot.pressionar_tecla('del', 0, 0.5)
    bot.Preencher_Texto(ticket, 0)
    bot.pressionar_tecla('enter', 0.5, 3)

    bot.Localizar_Click_Imagem(botao_opcoes, 0.5)
    bot.Localizar_Click_Imagem(botao_imprimir_ticket, 3)
    bot.Localizar_Click_Imagem(botao_imprimir, 2)
    bot.Localizar_Click_Imagem(botao_salvar_pdf, 1)
    endereco = salvarem+ticket+'.pdf'
    bot.Preencher_Texto(endereco, 0.5)
    bot.pressionar_tecla('enter', 0.5, 3)
    bot.pressionar_tecla('esc', 0.5, 0.5)
    bot.pressionar_tecla_atalho('altleft', 'w', 0.5, 3)
    primeiravez = False
