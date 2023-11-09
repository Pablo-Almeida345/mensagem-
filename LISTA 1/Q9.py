#9) Faça um Programa que leia uma quantidade números inteiros(informado pelo usuário) e armazene-os em
#uma lista. Armazene os números pares em uma lista PAR e os números ÍMPARES em uma lista ímpar.
#Imprima as três listas.

quantidade = int(input("Digite a quantidade de números inteiros: "))
numeros = []

for i in range(quantidade):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

pares = [x for x in numeros if x % 2 == 0]
impares = [x for x in numeros if x % 2 != 0]

print("Números:", numeros)
print("Números Pares:", pares)
print("Números Ímpares:", impares)
