import bot
from auxilio import AbrirAba


def BotVacinaCuiaba(cpf):
    AbrirAba('https://cadastro.vacinacuiaba.com.br', 2)

    botao_fechar = 'img_vacina/fechar.png'
    botao_consultar = 'img_vacina/consultar.png'
    texto_cpf = 'img_vacina/cpf.png'

    bot.Localizar_Click_Imagem(botao_fechar, 0.5)
    bot.Localizar_Click_Imagem(botao_consultar, 2)
    bot.Preencher_Texto_Localizar_Imagem(texto_cpf, 0.5, cpf)
