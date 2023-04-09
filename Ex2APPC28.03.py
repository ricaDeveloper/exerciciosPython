while True:

    numExt=''
    N=int(input("Digite um numero de 0 a 999 = "))

    while N<0 or N>999:
        print("digite um numero valido")
        N = int(input("Digite um numero de 0 a 999= "))

    dec=N%1
    uni=N%10-dec
    dez=N%100-uni
    cen=N-dez-uni-dec

    if N==0:
        numExt+="zero"

    if cen==100 and (dez or uni!=0):
        numExt+="cento "

    elif cen==100:
        numExt+="cem "
    elif cen==200:
        numExt+="duzentos "
    elif cen==300:
        numExt+="trezentos "
    elif cen==400:
        numExt+="quatrocentos "
    elif cen==500:
        numExt+="quinhentos "
    elif cen==600:
        numExt+="seiscentos "
    elif cen==700:
        numExt+="setecentos "
    elif cen==800:
        numExt+="oitocentos "
    elif cen==900:
        numExt+="novecentos "

    if cen!=0 and (dez or uni!=0):
        numExt+="e "

    if N%100>=10 and N%100<20:
        dez=N%100
        unidade=0

        if dez==10:
            numExt+="dez"
        elif dez==11:
            numExt+="onze"
        elif dez==12:
            numExt+="doze"
        elif dez==13:
            numExt+="treze"
        elif dez==14:
            numExt+="quatorze"
        elif dez==15:
            numExt+="quinze"
        elif dez==16:
            numExt+="dezesseis"
        elif dez==17:
            numExt+="dezessete"
        elif dez==18:
            numExt+="dezoito"
        elif dez==19:
            numExt+="dezenove"

    if dez>=20:
        if dez== 20:
            numExt+="vinte "
        elif dez==30:
            numExt+="trinta "
        elif dez==40:
            numExt+="quarenta "
        elif dez==50:
            numExt+="cinquenta "
        elif dez==60:
            numExt+="sessenta "
        elif dez==70:
            numExt+="setenta "
        elif dez==80:
            numExt+="oitenta "
        elif dez==90:
            numExt+="noventa "

    if uni!=0 and (dez!=0):
        numExt+="e "

    if uni==1:
        numExt+="um "
    elif uni==2:
        numExt+="dois "
    elif uni==3:
        numExt+="três "
    elif uni==4:
        numExt+="quatro "
    elif uni==5:
        numExt+="cinco "
    elif uni==6:
        numExt+="seis "
    elif uni==7:
        numExt+="sete "
    elif uni==8:
        numExt+="oito "
    elif uni==9:
        numExt+="nove "

    print(numExt.upper())
    print("____MENU____\n")
    print("1- Dar continuidade.\n")
    print("2- Parar\n")
    menu=int(input("Digite uma opção: "))

    if menu==2:
        break