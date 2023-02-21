from print_Banner import banner

def if_functions():
    banner('if and else')#if else

    nota = 6

    if nota <6:
        print('abaixo da média')
    elif nota ==6:
        print('Média')
    else:
        print('Acima da média')

def import_if(x):
    if __name__ == "__main__":
        return print(f"hello master, acesso {x} à função.")
    else:
        return print(f"Intruser, acesso {x} à função.")

import_if("Interno")