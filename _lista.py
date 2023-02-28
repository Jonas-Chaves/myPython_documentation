from print_Banner import banner

def lista_function():
    frutas=['banana', 'abacaxi', 'maça', 'uva']
    print(frutas)
    frutas.append('abacate')#Adiciona ao fianl da fila o item.
    print(frutas)
    frutas.pop()#Remove o último item.
    print(frutas)
    frutas.pop(0)#Remove item em posição indicada na lista.
    print(frutas)
    frutas.insert(1,"Pêra")#Adiciona item na posição indicada.
    print(frutas)
    frutas.remove("maça")#Remove o item de nome indicado.
    print(frutas)
    frutas.reverse()#Inverte a lista
    print(frutas)
    print(frutas.count("abacaxi"))#Conta na lista quantos do item de nome indicado existem na mesma.
    del frutas[:]#Deleta todos os itens da lista.
    print(frutas)

    print("Tamnaho da lista= ",len(frutas))

    for i in frutas:
        print(frutas.index(i) , i, sep=" - ")

    numeros = [14.55, 67, 89.88, 10, 21.5]
    print(min(numeros), max(numeros), sum(numeros),sep=" - ") 
    print(numeros.sort())

    linha=[2 for i in range(5)]
    print(linha)

    matriz=[[3 for i in range(5)] for i in range(5)]
    print(matriz)
lista_function()