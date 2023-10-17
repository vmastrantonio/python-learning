# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela

lista = []

for i in range(0,5):
    num = int(input("Insira um número: "))
    
    if i == 0:
        lista.append(num)
    else:    
        if num > max(lista):
            lista.append(num)
            
        elif num < min(lista):
            lista.insert(0, num)
            
        else:
            for pos, item in enumerate(lista):
                if num < item:
                    if num > lista[pos - 1]:
                        lista.insert(pos, num)

print(f"Lista: {lista}")