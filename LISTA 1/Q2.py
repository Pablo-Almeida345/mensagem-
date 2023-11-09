#2) Implementar um programa que recebendo um número limite, retorne uma lista contendo uma sequência
#de 1 até o número limite.

limite = int(input("Digite o limite"))
lista = []
for numeros in range(1,limite+1):
    lista.append(numeros) #n acresenta ao final da lista 
print(lista)