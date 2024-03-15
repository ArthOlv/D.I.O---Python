saldo = 500
saque = 50


status = "sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar seu saque")