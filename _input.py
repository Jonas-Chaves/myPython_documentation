from print_Banner import banner

def input_function():
    banner('Exemplos Imput Teclado')

    print('O input sempre converte para string')
    x=input('Digite um número: ')
    print(type(x))

    print('Conversão de dados')
    x=int(input('Digite um número: '))
    print(type(x))
