import bot
from auxilio import AbrirAba
import config


def BotVacinaCuiaba(cpf):
    AbrirAba('https://cadastro.vacinacuiaba.com.br', 2)

    if config.APP_ROOT == '':
        botao_fechar = 'static/img_vacina/fechar.png'
        botao_consultar = 'static/img_vacina/consultar.png'
        texto_cpf = 'static/img_vacina/cpf.png'

    else:
        botao_fechar = config.APP_ROOT + '\\static\\img_vacina\\fechar.png'
        botao_consultar = config.APP_ROOT + '\\static\\img_vacina\\consultar.png'
        texto_cpf = config.APP_ROOT + '\\static\\img_vacina\\cpf.png'

    bot.Localizar_Click_Imagem(botao_fechar, 0.5)
    bot.Localizar_Click_Imagem(botao_consultar, 2)
    bot.Preencher_Texto_Localizar_Imagem(texto_cpf, 0.5, cpf)
