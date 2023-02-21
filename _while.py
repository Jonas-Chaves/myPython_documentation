from print_Banner import banner

def while_functions():
    banner('Exemplos com While')
    print('Primeiro While')
    x = 0
    while(1):
        print(x)
        if x == 3:
            break
        x+=1

    print('Segundo While')
    count = 0
    while (count < 3):     
        count += 1
        print("Hello")

    print('Terceiro While')
    a = [1, 2, 3, 4]
    while a:
        print(a.pop())

    print('Quarto While')
    i = 0
    a = 'geeksforgeeks'
    
    while i < len(a): 
        if a[i] == 'e' or a[i] == 's': 
            i += 1
            continue
        print('Current Letter :', a[i])
        i += 1
