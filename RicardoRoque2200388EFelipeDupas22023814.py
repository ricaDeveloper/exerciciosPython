#PROJETO DO CAIXA

SenhaCaixa = 1234

#Entrada Para O Menu

while True:
    print("---------------------------")
    print("MENU DO SISTEMA")
    print("1 - Para Abrir o Caixa")
    print("2 - Para Trocar a Senha")
    print("3- Para Sair Do Sistema")
    print("---------------------------")
    menu = int(input("DIGITE A OPÇÃO DESEJADA = "))
    
    #Acesso Ao Caixa
    
    if menu==1:
        Senha=int(input("Digite a senha para ter acesso ao CAIXA = "))
        if Senha == SenhaCaixa:
            print("CAIXA ABERTO, ACESSO PERMITIDO")
            
            ValorProduto=0
            SaldoInicialCaixa=0
            Vendas=0
            troco=0
            opc=1 
            qtdItem=0
            qtdVendas=0
            valorTotalVendas=0
            saldoCaixa=0
            #Registro de vendas
            SaldoInicialCaixa = int(input("Qual o Saldo DISPONIVEL no Caixa? = "))

            while opc==1:
                while SaldoInicialCaixa>Vendas:
                    
                    ValorProduto = float(input("DIGITE O VALOR DO ITEM: "))
                    qtdItem=qtdItem+1
                    Vendas=Vendas+ValorProduto
                    if Vendas>=SaldoInicialCaixa or ValorProduto>SaldoInicialCaixa:
                        print('Você não tem saldo suficiente para continuar comprando.')
                        if Vendas==SaldoInicialCaixa:
                            print('Saldo disponivel no caixa: ',SaldoInicialCaixa-Vendas)
                        elif Vendas>SaldoInicialCaixa:
                            print('Você está devendo: ',Vendas-SaldoInicialCaixa)
                        break

                    else:    
                        opc=int(input('Realizar outra compra? 1-SIM // 2-NÃO   ')) 
                        qtdVendas=qtdVendas+1
                        if opc==2:
                            valorPago=float(input('Valor pago: '))
                            troco=valorPago-Vendas   
                            saldoCaixa=(SaldoInicialCaixa+Vendas)-troco 
                            print('Troco: ',troco)  
                            print('Vendas realizadas: ',qtdVendas)
                            print('Itens comercializados: ',qtdItem)
                            print('Valor das vendas: ',Vendas)
                            print('Saldo final do caixa',saldoCaixa)
                            break
        else:
            print("ACESSO NEGADO CAIXA BLOQUEADO")
            break
        
        #Troca de Senha
        
    if menu == 2:
        SenhaAntiga = int(input("Digite A Senha Antiga Para Efetuar A Troca = "))
        if SenhaAntiga == SenhaCaixa:
            NovaSenha = int(input("Digite A NOVA Senha = "))
            SenhaCaixa = NovaSenha
            
        else:
            print("SENHA INCORRETA!!!!!")
            break
        
    if menu == 3:
        print("SISTEMA ENCERRADO")
        break



