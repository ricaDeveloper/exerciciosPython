#Ex1
'''
N=0
maior=0
menor=100000
while (N==0):
    N=int(input('digite a qtd de repeticoes: '))

    if N<10:
        print('qtd precisa ser maior que 10.')
    else:    
        print('serão repetidas ',N)

while N!=0:
    x=int(input('digite o valor de x: '))

    if x>maior:
        maior=x
    if x<menor:
        menor=x
    N=N-1

print('maior: ',maior)
print('menor: ',menor)
'''
#Ex2
'''
idade=999
div=0
idadeTotal=0

while idade!=0:
    idade=0
    idade=int(input('digite a idade: '))

    if idade!=0:
        div=div+1

    idadeTotal=idadeTotal+idade
    media=idadeTotal/div

print('media das idades: ',media)
'''
#Ex3
'''
num=1
div=1
s=0

while num<100:
    s=s+(num/div)
    num=num+2
    div=div+1
    
print('S= ',s)
'''
#Ex4
'''
import math

s=0
a1=1
a2=0
i=1
x=int(input("Digite o valor de X: "))
s=x/a1
while i<=19:
    a1+=2
    a2+=2
    fat=math.factorial(a1)

    if i%2==0:
        s-=(x**a2)/fat
    else:
        s+=(x**a2)/fat

    i+=1

print(f"{s:.2f}")
'''
#Ex5
'''
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor de c: '))
d=int(input('Digite o valor de d: '))
e=int(input('Digite o valor de e: '))
f=int(input('Digite o valor de f: '))

if a*e-b*d<0:
    print('o valor do divisor deve ser positivo. ')
else:
    z=c*e-b*f
    w=a*e-b*d
    x=z/w
    print('valor de x: ',x)
    k=a*f-c*d
    j=a*e-b*d
    y=k/j
    print('valor de y: ',y)
'''