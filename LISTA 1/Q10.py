#10) Faça um programa que peça quantidade de elementos, e retorne os elementos(lista), a soma dos valores
#dos valores da lista e a multiplicação dos elementos da lista.

quantidade = int(input("Digite a quantidade de elementos: "))
elementos = []

for i in range(quantidade):
    elemento = int(input(f"Digite o elemento {i + 1}: "))
    elementos.append(elemento)

multiplicacao = 1
for elemento in elementos:
    multiplicacao *= elemento

print("Elementos:", elementos)
print("Multiplicação:", multiplicacao)
