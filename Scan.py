
import argparse
import socket
import portconf
import os
import time
from fktn.funcoes import find_ip


parse = argparse.ArgumentParser(description='Comandos: ')
parse.add_argument('-a', type=str, required=False, help='Ip ou Url do alvo, caso seja uma url, digitar a url completa')
parse.add_argument('-s', type=int, required=False, help='Salvar log da açao com --s 1')
args = parse.parse_args()


print('''
.d88888b                                      
88.    "'                                     
`Y88888b. .d8888b. .d8888b. 88d888b. 
      `8b 88'  `"" 88'  `88 88'  `88 
d8'   .8P 88.  ... 88.  .88 88    88
 Y88888P  `88888P' `88888P8 dP    dP 

 \n''')

 
print('='*50)
print(f'{"Scanner de Portas":^50}')
print('='*50)

argumento = str(input('Digite o alvo: '))

# Menu de opçoes
print("""\nEscolha uma opçao:\n
    [0] - Verificar uma porta manualmente
    [1] - Varredura de todas as portas (Processo lento)
    [2] - Varredura das portas mais conhecidas (Processo Rápido)
""")

# Escolha de opções e validação de resposta
opt = str(input('>> '))
while opt not in '012':
    print('    Opção invalida, tente novamente.')
    opt = str(input('>> '))

# Configurações das portas
portas_info = portconf.portas_info()
portas_co = portconf.portas_co()

# Opção de Porta Manual
if opt == '0':
    print()
    porta_sel = int(input('Porta: '))
    while porta_sel > 0:
        print(f'Verificando a Porta {porta_sel}', end='', flush=True)
        time.sleep(0.5)
        print('.', end='', flush=True)
        time.sleep(0.5)
        print('.', end='', flush=True)
        time.sleep(0.5)
        print('.', flush=True)
        time.sleep(0.5)

        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor = cliente.connect_ex((argumento, porta_sel))

        if servidor == 0:
            print(f'A porta {porta_sel} está aberta no ip {argumento}')
            cliente.close()
        else:
            print(f'A porta {porta_sel} não está aberta.')
            cliente.close()
            
        time.sleep(2)
        print('\n\n<-Digite 0 para parar->')
        porta_sel = int(input('\nPorta: '))
    
# opçao de varrer todas as portas
if opt == '1':
    for ports in range(1,65535):
        
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor = cliente.connect_ex((argumento, ports))
        print(f'Verificando a porta {ports}')

        if servidor == 0:

            print(f'PORTA {ports} ABERTA NO IP {argumento}')
            
            if args.s == 1:
                arquivo = open(f'{argumento} - Portas Abertas.txt', 'a')
                arquivo.write(f'Porta {ports} aberta no ip {argumento}\n')
                arquivo.close()
            
            cliente.close()

        

# Varredura das portas mais conhecidas
if opt == '2':
    print('\nFazendo a varredura das portas...\n\n')

    sitaxy = 0
    linha = 0

    for port in portas_co:

        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server = cliente.connect_ex((argumento, port))
        
        try:
            service = portas_info[port]
        except:
            service = '???'

        if server == 0:
            if sitaxy == 0:
                print(f"""
{'-'*55}
{'PORTA':^10} | {'STATUS':^10} | {' IP/URL':^15} | {'SERVIÇO':^10}
{'-'*55}""")
                sitaxy += 1

            print(f'{f"{port}":^10} | {"open":^10} | {f"{argumento}":^15} | {f"{service}":^10}')

            if args.s == 1:
                arquivo = open(f'{argumento} - Portas abertas.txt', 'a')
                arquivo.write(f'{f"{port}":^10} | {"open":^10} | {f"{argumento}":^15} | {f"{service}":^10}\n')
                arquivo.close()

            cliente.close()
    if sitaxy == 0:
        print('Nenhuma porta foi encontrada nesse ip.')

print(f'\n{"<< Fim >>":-^60}')
dufou = input('')
sakjfbius = input('')
