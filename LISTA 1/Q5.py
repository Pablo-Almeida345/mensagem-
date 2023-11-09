#5) Implementar um programa que recebendo um número de início e fim, retorne uma lista contendo uma
#sequência do número final até o número inicial.

inicio = int(input("Digite o inicio:"))
fim = int(input("fim:"))
lista = []

for numero in range(fim, inicio-1,-1):
    lista.append(numero)
print(lista)