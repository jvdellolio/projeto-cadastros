from projeto.lib.interface import *
from projeto.lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # opção de listar o conteudo do arquivo!
        lerarquivo(arq)
    elif resposta == 2:
        # cadastrar nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar (arq, nome, idade)
    elif resposta == 3:
        # opção de sair do sitema
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(1)