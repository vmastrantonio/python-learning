# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles

working = True
cont = 0
soma = 0


while working:
    num = int(input("Digite um valor ou ( 999 ) para sair: "))
    if num != 999:
        soma += num
        cont += 1
    else:
        working = False
        
print(f"A soma de todos números é {soma}, você digitou {cont} números!")