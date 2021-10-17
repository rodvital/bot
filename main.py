import logging
from movidesk import BotImprimirPDFTicket
# from vacinacuiaba import BotVacinaCuiaba
logging.basicConfig(filename='logging.log', level=logging.DEBUG, encoding='utf-8',
                    format=u'%(asctime)s %(name)s %(levelname)s %(message)s',
                    filemode='w')

# BotVacinaCuiaba('89409876168')

salvarem = 'f:\\Downloads\\teste_ticket\\'
tickets = ['21166', '21167']
BotImprimirPDFTicket(tickets, salvarem, 2)
