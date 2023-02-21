import os
from print_Banner import menu
from _print import prints
from _for import for_functions
from _input import input_function
from if_Else_Elif import if_functions, import_if
from _while import while_functions

if __name__ == "__main__":
    while(1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Selecione a opção desejada para verificar o exemplo de funcionamento:")
        menu()    
        x=input("Digite a opção desejada: ")
        if(x=="1"):
            prints()
        elif(x=='2'):
            input_function()
        elif(x=='3'):
            if_functions()
            import_if("Externo")
        elif(x=="4"):
            for_functions() 
        elif(x=='5'):
            while_functions()     


        input("\n\nDigite enter para prosseguir...")
