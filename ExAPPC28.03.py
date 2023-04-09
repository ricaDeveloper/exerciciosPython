#Ex13
'''
ano=int(input('digite o ano: '))

if (ano<1583) and (ano%4==0):
    print('o ano é bissexto.')
elif (ano>1583) and (ano%4==0) or (ano%400==0) or (ano%100==0):
    print('o ano é bissexto')
else:
    print('o ano não é bissexto')
'''
#Ex14
'''
dia=int(input('digite o dia: '))
mes=int(input('digite o mês: '))
ano=int(input('digite o ano: '))
def main():
    if dia<1 or dia>31:
        print('o dia deve ser entre 1 e 31.')
    else:
        print('dia ',dia)
    if mes==2 and dia<30: 
        print('mes de fev.')
    elif mes==2:
        print('esse dia nao existe em fev')
        return
    if mes<1 or mes>12:
        print('o mes deve ser entre 1 e 12')
    else: 
        print('do mes ',mes)
    if (ano<1583) and (ano%4==0):
        print('o ano é bissexto')
    elif (ano>1583) and (ano%4==0) or (ano%400==0) or (ano%100==0):
        print('o ano é bissexto')
    else:
        print('o ano não é bissexto')
main()
'''