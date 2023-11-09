#11) Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta
#será determinado pela média dos cinco saltos. Você deve fazer um programa que receba o nome e as cinco
#distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. 

nome = input("Digite o nome do atleta: ")
saltos = []

for i in range(5):
    distancia = float(input(f"Digite a distância do salto {i + 1}: "))
    saltos.append(distancia)

soma_saltos = 0
for salto in saltos:
    soma_saltos += salto

media = soma_saltos / 5

print("Nome do atleta:", nome)
print("Saltos:", saltos)
print("Média dos saltos:", media)
