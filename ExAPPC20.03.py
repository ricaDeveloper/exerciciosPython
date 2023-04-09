#Ex1
'''
senhaReal=211101

senhaDigitada=int(input('tente acertar a senha: '))

if senhaDigitada==senhaReal:
    print('ACESSO PERMITIDO.')
else:
    print('ACESSO NEGADO.')
'''
#Ex2
'''
x=int(input('digite um numero : '))
y=int(input('digite um outro numero : '))
z=int(input('digite um outro numero : '))
#validação de lados
if x<y+z and y<x+z and z<y+x: 
    if x==z==y:
        print('é um trianguilo equilatero e consequentemente isóscele')
    elif x==y or x==z or y==z:
        print('é um triangulo isóscele')
    else:
        print('é um triangulo escaleno')
else:
    print('digite valores validos para um triangulo.')
'''
#Ex3
'''
num=int(input('digite um número: '))

if num%2==0:
    print('Número par.')
else:
    print('Número ímpar.')
'''
#Ex4
'''
a=int(input('digite o valor de A: '))
b=int(input('digite o valor de B: '))

res=a//b

if res%2==0:
    print('A é divisível por B.')
else:
    print('A não é divisível por B')
'''
#Ex5
'''
N1=float(input('digite a nota 1: '))
P1=float(input('digite o peso da nota 1(entre 0.1 e 0.9): '))
N2=float(input('digite a nota 2: '))
P2=float(input('digite o peso da nota 2(entre 0.1 e 0.9): '))

media=N1*P1+N2*P2
mediaReal=media/(P1/P2)

if mediaReal>=9:
    print('aprovado com louvor!!!')
elif mediaReal>=8 and mediaReal<9:
    print('parabéns, desempenho muito bom.')
elif mediaReal>=5:
    print('aprovado.')
else:
    print('reprovado.')
'''
#Ex6
'''
graus=int(input('digite a temperatura em Celsius: '))
#Procurei formulas na internet, não consegui fazer com as dadas no slide
Fahrenheit=1.8*graus+32

Kelvin=graus+273.15

Réaumur=graus/1.25

Rankine=graus*1.8+491.67

CelsiusK=Kelvin

CelsiusR=Réaumur

CelsiusRK=Rankine

print('Temperatura em Fahrenheit: ',Fahrenheit)
print('Temperatura em Kelvin: ',CelsiusK)
print('Temperatura em Rankine: ',CelsiusRK)
print('Temperatura em Réaumur: ',CelsiusR)
'''
#Ex7
'''
print('1-Celsius\t2-Fahrenheit\t3-Kelvin\t4-Rankine\t5-Réaumur\t')

opção=int(input('digite uma opção para converter: '))
opção2=int(input('agora escolha a outra: '))
graus=int(input('digite a temperatura: '))

if opção==1 and opção2==2:
    F=1.8*graus+32
    print(F)
elif opção==1 and opção2==3:
    K=graus+273.15
    print(K)
elif opção==1 and opção2==4:
    Rk=graus*1.8+491.67
    print(Rk)
elif opção==1 and opção2==5:
    Re=graus/1.25
    print(Re)
elif opção==2 and opção2==1:
    C=graus-32/1.8
    print(C)
elif opção==2 and opção2==3:
    K=graus*9/5-459.67
    print(K)
elif opção==2 and opção2==4:
    Rk=(graus-32)+491.67
    print(Rk)
elif opção==2 and opção2==5:
    Re=(graus-32)*0.44
    print(Re)
elif opção==3 and opção2==1:
    C=graus-273
    print(C)
elif opção==3 and opção2==2:
    F=(graus-273)*1.8+32
    print(F)
elif opção==3 and opção2==4:
    Rk=(graus-273.15)*1.8+491.67
    print(Rk)
elif opção==3 and opção2==5:
    Re=(graus-273.15)*0.8
    print(Re)
elif opção==4 and opção2==1:
    C=(graus-491.67)*5/9
    print(C)
elif opção==4 and opção2==2:
    F=graus-459.67
    print(F)
elif opção==4 and opção2==3:
    Rk=(graus-491.67)/1.8+273.15
    print(Rk)
elif opção==4 and opção2==5:
    Re=(graus-491.67)*0.44
    print(Re)
elif opção==5 and opção2==1:
    C=graus/0.8
    print(C)
elif opção==5 and opção2==2:
    F=graus*2.25+32
    print(F)
elif opção==5 and opção2==3:
    K=graus/0.8+273.15
    print(K)
elif opção==5 and opção2==4:
    Rk=(graus*2.225)+491.67
    print(Rk)
'''
#Ex8
'''
anoConstrução=int(input('digite o ano que o imovel foi construido: '))
anoAtual=int(input('digite o ano atual: '))

idadeCasa=anoAtual-anoConstrução

if idadeCasa<5:
    print('Não há descontos.')
elif idadeCasa>=5 and idadeCasa<20:
    print('Existe um desconto de 15%')
elif idadeCasa>=20 and idadeCasa<40:
    print('Existe um desconto de 25%')
elif idadeCasa>=40:
    print('Existe um desconto de 30%')
'''
#Ex9
'''
peso=float(input('digite seu peso: '))
altura=float(input('digite sua altura: '))

imc=peso/(altura*altura)

if imc<18.5:
    print('Baixo peso.')
elif imc>18.5 and imc<24.99:
    print('Normal.')
elif imc>25 and imc<29.99:
    print('Sobrepeso.')
elif imc>30:
    print('Obesidade.')
'''
#Ex10
'''
a=int(input('primeiro numero: '))
b =int(input('segundo numero : '))
c=int(input('terceiro numero: '))
print(a,b,c)
if(c<b):
    z=c
    c=b
    b=z
if(b<a):
    z=b
    b=a
    a=z
if(c<b):
    z=c
    c=b
    b=z
print(a,b,c)
'''
#Ex11
'''
Av1=float(input('digite a primeira nota: '))
Av2=float(input('digite a segunda nota: '))
Freq=int(input('digite sua frequencia em %: '))

media=(Av1+Av2)/2

if Freq<75:
    print('Reprovado.')
elif Freq>=75 and media<=4:
    print('Reprovado')
elif Freq>=75 and media>4 and media<6:
    print('Exame')
elif Freq>=75 and media>6:
    print('Aprovado')
'''
#Ex12
'''
x=int(input('digite o valor de X: '))

if x==0:
    print('digite um valor diferente de 0 para X.')
else:
    f=4*(x*x)-(3*x)+9
    res=f/x
    print(res)
'''

