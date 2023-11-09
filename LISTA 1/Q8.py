#8) Faça um Programa que leia peça a quantidade de notas, mostre as notas(lista) e a média na tela.

quantidade = int(input("Digite a quantidade de notas: "))
notas = []
soma = 0

for i in range(quantidade):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)
    soma += nota

media = soma / quantidade

print("Notas:", notas)
print("Média:", media)
