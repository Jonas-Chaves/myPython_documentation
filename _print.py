from print_Banner import banner

def prints():
    banner("Exemplos de Print")

    print('''
    Impressão de texto longo
    com quebra de linha
    na console.
    ''')
    x="Alfredo"
    print(f"Nome da variável x= {x}")
    print("Operações no print, Soma= ",23+55)

    lista=['item 1','item 2','item 3']
    print('Imprimir lista= ',lista)

    print('Nome ', end='')
    print('Sobrenome ', end='*-*')
    print('\nNome', 'Sobrenome',sep='@')