#4) Implementar um programa que recebendo um número de início e fim, retorne uma lista contendo uma
#sequência do número de início até o número final.

inicio = int(input("Digite o inicio:"))
fim = int(input("fim:"))
lista = []

for numero in range(inicio,fim+1):
    lista.append(numero)
print(lista)