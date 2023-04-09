#Ex1
'''
num1=int(input("determine um intervalo: "))
num2=int(input("digite um outro numero inteiro para ver seus intervalos: "))

if num1<=num2:
    for i in range(num1,num2+1):
        print(i)
else:

    print("digite valores validos")
'''
#Ex2
'''
soma=0
num=int(input("digite os valores para descobrir a media: "))

for i in range(num):
    valor=int(input("Digite o valor: "))
    soma+=valor

media=soma/num
print("média: ",media)
'''
#Ex3 
'''
maior=0
menor=99999
soma=0

num=int(input("digite os valores para descobrir a media: "))

for i in range (num):
    valor=int(input("Digite o valor: "))
    soma+=valor
    if valor<menor:
        menor=valor
    if valor>maior:
        maior=valor

media = soma/num

print("média: ",media)
print("maior numero: ",maior)
print("menor numero:",menor)
'''
#Ex4
'''
n=int(input("digite o valor de N: "))

fat=1

for i in range(1, n+1):
    fat=i

print(f"o valor fatorial de {n} é: {fatorial}")
'''
#Ex5
'''
n=int(input("digite o valor de N: "))

for i in range(0, 11):
    T = n*i
    print(f"{n}*{i}={T}")
'''
#Ex6
'''
tempMin=1000
diaMinimo=0

for d in range(1,31):
    T=0.011*(d**3)-0.3*(d*2)+0.04*d

    if T<T_min:
        T_min=T
        d_min=d
print(f"O dia com a temperatura mínima é o dia {d_min}")
'''
#Ex7
'''
import random

print("adivinhe o numero (0 a 100)")
numeroJogador=-1
numeroComputador=-1

numeroComputador=random.randint(0,100)

while numeroJogador!=numeroComputador:
    numeroJogador=int(input("DIGITE UM NÚMERO: ")) 

    if numeroJogador>numeroComputador:
        print("O seu numero é MAIOR que o do computador")
    if numeroJogador<numeroComputador:
        print("O seu numero é MENOR que o do computador") 
    if numeroJogador==numeroComputador:
        print("\nvoce acertou o numero!")
'''
#Ex7-8-9-10
'''
import random
import os

numComputador=random.randint(0, 100)

print("adivinhe o numero!(0 a 100)")
print("\ndigite 2020 para sair\n")

numJogador=-1
cont=0

while numJogador!=numComputador:
    desis=0
    numJogador=int(input("Escolha um numero: "))

    if numJogador>numComputador and numJogador!=2020:
        print("\nO seu número é MAIOR que o do computador\n")

    if numJogador<numComputador:
        print("\nO seu número é MENOR que o do computador\n")

    if numJogador==numComputador:
        print("voce acertou!\n")

    if numJogador>100 and numJogador!=1001:
        print("\nmaximo 100!\n")

    if numJogador<=100:
        cont+=1

    if numJogador==1001:
        print("\nquer mesmo desistir?")

        while d<1 or d>3:
            print("\t(1)Sim\t(2)Não\t(3)Reiniciar partida")
            d= int(input("\t:"))

            if d==1:
                numJogador=numComputador
                print("\ntente novamente\n")

            if d==2:
                print("continuando jogo...")

            if d==3:
                numComputador=random.randint(0, 100)
                print("outro numero gerado")
                cont=0
                os.system("pause")
                os.system("cls")

print("tentativas: ", cont)
'''
#Ex11-12
'''
num1=int(input("\nescolha um numero: "))
num2=int(input("\nescolha outro numero: "))
print("\nescolha um numero nesse intervalo que voce deseja saber os divisiveis: ")
div = int(input("divisiveis de: "))

for i in range(num1, num2+1):
    if i % div == 0:
        print(i)
'''
#Ex13
'''
listaTimes=["GUARANI", "SÃO PAULO", "PALMEIRAS", "CRUZEIRO",
         "SANTOS", "FERROVIÁRIA", "JUVENTUS", "GOIÁS",
         "ÍBIS", "SINOP"]

for i in range(len(listaTimes)):
    print(f"{i}-{listaTimes[i]}")
'''
#Ex14-15-16
'''
import random

pedra=1
papel=2
tesoura=3
opcJogador=-1
contScript=0
contJogador=0
contEmpate=0

print('---digite 0 para parar de jogar---')

while opcJogador!=0:
    script=random.randint(0,3)
    print('opções-> PEDRA=1 / PAPEL=2 / TESOURA=3 ')
    opcJogador=int(input('escolha sua opção: '))

    if opcJogador>-1 and opcJogador<4:

        if opcJogador==script:
            print('empate!')
            contEmpate=contEmpate+1
        elif opcJogador==1 and script==2:
            print('voce perdeu! pedra perde para papel')
            contScript=contScript+1
        elif opcJogador==1 and script==3:
            print('voce ganhou! pedra ganha de tesoura')
            contJogador=contJogador+1
        elif opcJogador==2 and script==1:
            print('voce ganhou! papel ganha de pedra')   
            contJogador=contJogador+1 
        elif opcJogador==2 and script==3:
            print('voce perdeu! papel perde para tesoura')
            contScript=contScript+1
        elif opcJogador==3 and script==1:
            print('voce perdeu! tesoura perde para pedra')
            contScript=contScript+1
        elif opcJogador==3 and script==2:
            print('voce ganhou! tesoura ganha de papel')
            contJogador=contJogador+1
    else:
        print('DIGITE VALORES VALIDOS.(1 a 3)')
if opcJogador==0:
        print('voce empatou {contEmpate} vezes!',contEmpate)
        print('voce perdeu {contScript} vezes!',contScript)
        print('voce ganhou {contJogador} vezes!',contJogador)
'''           
