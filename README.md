# myPython_documentation

# Operadores de Comparação
==, !=, >, <, >=, <=

# Operadores Lógicos
and, or, not

# Operadores Bitwise
& faz um bitwise and, por exemplo, x & y = 0, que é 0000 0000 em binário.
| faz um bitwise ou, por exemplo, x | y = 31, que é 0001 1111 em binário.
˜  faz um bitwise não, por exemplo, ˜ x = 240*, que é 1111 0000 em binário.
^ faz um bitwise xor, por exemplo, x ^ y = 31, que é 0001 1111 em binário.
>> faz um bitwise right shift, por exemplo, y >> 1 = 8, que é 0000 1000 em binário.
<< faz um bitwise left shift, por exemplo, y << 3 = , que é 1000 0000 em binário.

# Print
- end - Altera o comportamento padrão do print de adicionar um \n ao finalizar a execução.
print('texto', end='')
- sep - Altera o separador padrão "Espaço" para o indicado.
print('texto1', 'texto2', sep='@')

# Input
- O input() sempre retorna uma string.
Para converter os tipos de dados podemo usar int(), str(), float().
Ex.: int(input()) 

# For
- Para o FOR iterar sobre uma sequência numérica usa-se a função range().
for i in range(10):
- Podemos usar o For para percorrer os itens de uma string/lista/dicionário.
palavra = 'Elefante'
for letra in palavra:
    print(letra,end='*')
Resultado=    E*l*e*f*a*n*t*e

# Range()
- range(start, stop, step)

