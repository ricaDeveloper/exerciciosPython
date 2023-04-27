dados={
       "ADERBAL":[20,"32183912"],
       "LINDOMAR":[15,"3812903"],
       "ISABELA":[67,"869565"],
       "MATHEUS":[76,"9931293"],
       "CAIO":[76,"9931293"]
       }
opc=1
while True:
    print('1-Cadastrar\n2-Listar\n3-Consultar\n4-Deletar\n0-Sair\n')
    menu=int(input('Escolha sua opção: '))
   
    while opc==1 and menu==1:
        print('Cadastre nomes!')
   
        nome=input('digite um nome para ser cadastrado: ')
        idade=int(input('digite a idade: '))
        cpf=input('digite o cpf: ')
        nome=nome.upper()
        dados[nome]=[idade,cpf]
       
        print('deseja cadastrar outro nome?\n')
        print('1-SIM  // 2-NÃO(retorta ao menu) ')
        opc=int(input('Digite a opção! '))
   
        if opc==2:
            print('\n1-Cadastrar\n2-Listar\n3-Consultar\n4-Deletar\n0-Sair\n')
            menu=int(input('Escolha sua opção: '))  
    if menu==2:
        for i in dados:
            
            print(f'{i} {dados[i]}')     
    if menu==3:
        nome=input('buscar nome: ').upper()
   
        flag=False
        for i in dados:
            if i==nome:
                print(i," ",dados[i])
                flag=True
        if flag==False:
            print("nome nao cadastrado")
    if menu==4:
        delet=input('qual nome voce deseja deletar?: ').upper()
        
        if delet in list(dados.keys()):
            print('Removendo nome')
            del dados[delet]
    if menu==0:
        break 
               