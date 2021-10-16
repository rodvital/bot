import webbrowser
import bot
from time import sleep

newtab = 2  # open in a new tab, if possible

url = "https://cadastro.vacinacuiaba.com.br/"
webbrowser.open(url, newtab)
sleep(2)  # carregar


botao_fechar = 'imagens/fechar.png'
botao_consultar = 'imagens/consultar.png'
texto_cpf = 'imagens/cpf.png'
cpf = '89409876168'


bot.Localizar_Click_Imagem(botao_fechar, 0.5)
bot.Localizar_Click_Imagem(botao_consultar, 2)
bot.Preencher_Texto_Localizar_Imagem(texto_cpf, 0.5, cpf)
