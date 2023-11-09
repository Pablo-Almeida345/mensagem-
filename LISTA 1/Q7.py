#7) Implementar um programa que recebendo um número, retorne uma lista com a tabuada desse número.

nt = int(input("Digite um numero da tabuada"))
lista=[]

for fim in range(10+1):
    lista.append(nt*fim)
print(lista)