# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

print("Bem vindo, insira dois números para prosseguir")

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

working = True

while working:
    print("""Menu:
        [1] somar
        [2] multiplicar
        [3] saber o maior          
        [4] novos números  
        [5] sair do programa  
        """)
    
    chosen = int(input("Escolha uma opção: "))
    
    if chosen == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
        
    elif chosen == 2:
        print(f"{num1} x {num2} = {num1 * num2}")
        
    elif chosen == 3:
        if num1 > num2:
            print(f"{num1} > {num2}")
        else:
            print(f"{num2} > {num1}")
            
    elif chosen == 4:
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        
    elif chosen == 5:
        working = False