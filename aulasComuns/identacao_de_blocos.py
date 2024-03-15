saldo = 500

def sacar(valor):
    global saldo
    if saldo>=valor:
        print("valor sacado")
        saldo -= valor
        print(f"novo saldo de {saldo} reais")
    else:
        print("valor maior do que saldo")

def depositar(valor):
    global saldo 
    saldo +=valor
    print(f"seu novo saldo é de {saldo} reais")

sacar(200)
