menu = '''

['d'] Depositar
['s'] Sacar
['e'] Extrato
['q'] Sair

==>   '''

totalDepositado = 0
totalSacado = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        valorDeposito = float(input("Digite o valor que deseja depositar: R$ "))
        if valorDeposito >0:
            saldo = valorDeposito + saldo
            totalDepositado = valorDeposito + totalDepositado
            print("Deposito feito com Sucesso \n Novo saldo de: R$ {:.2f}".format(saldo))
        else:
            print("Não foi possivel realizar o depósito, por favor insira um valor correto")
    elif opcao == "s":
        print("Saque")
        if numero_saques == LIMITE_SAQUES:
            print("Voce atingiu o numero maximo de saques diarios")
        elif saldo <=0:
            print("Voce nao tem saldo suficiente para realizar um saque")
        else:
            saque = float(input("Digite o valor do saque desejado: "))
            if saque>0:
                if saque>limite:
                    print("Seu limite nao permite saques maiores do que 500 reais")
                elif saque > saldo:
                    print("Voce nao pode fazer um saque maior que o seu saldo")
                else:
                    print("Saque feito com sucesso")
                    numero_saques= numero_saques+1
                    saldo = saldo-saque
                    totalSacado = saque + totalSacado
                    print("Novo saldo de: R${:.2f} \n Numero de saques diarios: {}/{}".format(saldo,numero_saques,LIMITE_SAQUES))
            else:
                print("Voce nao pode fazer um saque com um valor igual a 0")
        
    elif opcao =="e":
        print("extrato")
        print("Saldo: R${:.2f}".format(saldo))
        print("Valor dos saques feitos: R${:.2f}      {}/{}".format(totalSacado,numero_saques,LIMITE_SAQUES))
        print("Valor total depositado: R${:.2f}".format(totalDepositado))
    elif opcao == "q":
        print("Saindo")
        break
    else:
        print("Opcao invalida tente novamente uma opcao valida")
