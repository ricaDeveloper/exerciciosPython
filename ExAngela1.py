#Ex1
'''
a=int(input('digite um numero negativo: '))

if a<0 and a%2==0:
    print('o numero digitado é negativo e divisivel por 2. ')
'''
#Ex2
'''
A=int(input('digite um numero : '))
B=int(input('digite um outro numero : '))

if A==B:
    C=A+B
else:
    C=A*B

print(C)
'''
#Ex3
'''
x=int(input('digite um numero : '))
y=int(input('digite um outro numero : '))
z=int(input('digite um outro numero : '))

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
#Ex4
'''
x=int(input('digite o valor de x: '))
y=int(input('digite o valro de y: '))

if x<y:
    z=int(input('digite um numero : '))

    if z==y:
        print('o valor digitado é o limite superior')
    elif z==x:
        print('o valor digitado é o limite inferior')
    elif x<z and z<y:
        print('o valor digitado pertence ao intervalo')
    elif z>y:
        print('o valor digitado está fora do intervalo e é maior do que o limite superior')
    elif z<x:
        print('o valor digitado está fora do intervalo e é menor do que o limite inferior1')
else:
    print('o valor de y deve ser maior do que o de x.')
'''
#Ex5
'''
a=int(input('digite o valor de a: '))
b=int(input('digite o valor de b: '))
c=int(input('digite o valor de c: '))

if a==0:
    print('a deve ser maior que 0.')

else:
    d=(b**2 - 4*a*c)

    x1=(-b+d**(1/2))/(2*a)
    x2=(-b-d**(1/2))/(2*a)
print('Valor de x1: ',x1)
print('Valor de x2: ',x2)
'''

#Ex6
'''
N1=int(input('digite a nota 1: '))
P1=float(input('digite o peso da nota 1(entre 0.1 e 0.9): '))
N2=int(input('digite a nota 2: '))
P2=float(input('digite o peso da nota 2(entre 0.1 e 0.9): '))

media=N1*P1+N2*P2

if mediaReal==10:
    print('aprovado com distinção!!!')
elif mediaReal>6.99:
    print('aprovado.')
else:
    print('reprovado.')
'''
#Ex7
'''
dia=int(input('digite um numero que corresponde a um dia da semana(1 a 7): '))

if dia==1:
    print('Domingo.')
elif dia==2:
    print('Segunda.')
elif dia==3:
    print('Terça.')
elif dia==4:
    print('Quarta.')
elif dia==5:
    print('Quinta.')
elif dia==6:
    print('Sexta!!!.')
elif dia==7:
    print('Sábado.')
'''   
