texto = input("Digite o texto que desejar")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")

print("\n")
for numero in range(0, 140, 14):
    print(numero, end=" ")