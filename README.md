# Criando um Bot com PYAUTOGUI e utilizando o Flask para Interface para Usuário
O pyautogui foi escolhido pela possibilidade de fazer a identificação dos locais onde o bot irá dar os clicks através das imagens (pasta `static/img_movidesk` ou `static/img_vacina`)

<p align="center">
 <a href="#objetivo">Objetivo</a> •
 <a href="#roadmap">Consultar o Vacina Cuiabá</a> • 
 <a href="#roadmap">Gerar PDF's do MoviDesk</a> • 
 <a href="#tecnologias">Tecnologias</a> • 
 <a href="#contribuicao">Contribuição</a> • 
 <a href="#licenc-a">Licença</a> • 
 <a href="#autor">Autor</a>
</p>

 * [Objetivo](#Objetivo)
 * [Consultar Vacina Cuiabá](#Consultar_Vacina_Cuiabá)
 * [Gerar PDF's do MoviDesk](#Gerar_PDF_do_MoviDesk)
 * [Tecnologias](#tecnologias)
   
<h1 align="center">
  <img alt="NextLevelWeek" title="#NextLevelWeek" src="./assets/TelaPrincipal.png" />
</h1>

<h4 align="center"> 
	🚧  Bot do Robozão 🚀 Em construção...  🚧
</h4>

## Objetivo
O objetivo do projeto foi testar a tecnologia do pyautogui e o Flask, e para ter uma utilidade foi feito através da Vacina Cuiabá, onde é um site aberto ao público e todos podem entender como funciona. 
Também foi implementado uma funcionalidade mais util e complicada, que é a Geração de PDF's de chamados (Tickets) do Sistema <a href="https://www.movidesk.com/">Movidesk</a>.

## Consultar Vacina Cuiabá
Este bot vai até a parte de consulta o CPF do Vacina Cuiabá, preenchendo o CPF Informado. 

## Gerar PDF's do MoviDesk
Esta bot tem localiza uma lista de 20 tickets informado através de "," (vírgula) ou enter, o local informado na máquina do usuário e também se deseja que a opção do histórico de alteração esteja marcada. Com isso ele gera os PDF's na pasta selecionada.

## Tecnologias
As tecnologia utilizadas foram o pyautogui e o Flask, sendo que para o pyautogui realizar o reconhecimento das imagens foi necessário instalar o Pillow e o opencv-python. 


