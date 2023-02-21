from print_Banner import banner

def for_functions():
    banner('Exemplos de estruturas For')
    frutas=['banana','morango','abacaxi']#Lista
    print("Lista de caracteres=",frutas)
    for x in frutas:
        print("Item n° ",frutas.index(x)," da lista de frutas = ",x)

    for x in range(5):
        print(x)

    text = "OpenEDG Python Institute"
    for letter in text:
        if letter == "P":
            continue
        print(letter, end="")    