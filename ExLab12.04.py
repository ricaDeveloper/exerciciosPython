'''
nome=[]

nome=input('digite uma palavra: ')

numLetras=0
vogais=0
consoantes=0

tam=len(nome)

for i in range(0,tam):
    if nome[i]=='a' or nome[i]=='e' or nome[i]=='i' or nome[i]=='o' or nome[i]=='u':
        vogais=vogais+1
    else:
        consoantes=consoantes+1
numLetras=vogais+consoantes

       
print('numero de letras: ',numLetras)
print('numero de vogais: ',vogais)
print('numero de consoantes: ',consoantes)
'''
'''
n=[]

while True:
    valorN=input('digite uma nota: ')
    n.append(float(valorN))
    opc=input('deseja digitar outra nota? <S/N>: ')
    if opc=='n':
        break
tam=len(n)
soma=0
media=0
for i in range(0,tam):
    soma=soma+n[i]
   
maior=0
menor=10000

for i in range(0,tam):
    if n[i]>maior:
        maior=n[i]
    if n[i]<menor:
        menor=n[i]
   
   
media=soma/tam

print('media: ',media)
'''

n=[0,0,0,0]

for i in range (0,4):
    valorN=input('digite a nota: ')
    n[i]=float(valorN)
   
soma=0
media=0
for i in range(0,4):
    soma=soma+n[i]
   
maior=0
menor=10000

for i in range(0,4):
    if n[i]>maior:
        maior=n[i]
    if n[i]<menor:
        menor=n[i]
   
   
media=soma/4

print('media: ',media)
print('maior: ',maior)
print('menor: ',menor)