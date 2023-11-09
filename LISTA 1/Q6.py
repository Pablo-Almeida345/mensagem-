#6) Implementar um programa que recebendo uma lista de números inteiros(quantidade de números
#informada pelo usuário), retorne uma lista com o dobro de cada elemento.

numero = int(input("Digite a quantidade de numeros da lista:"))
lista = []

for quantidade in range(numero):
    n1 = int(input("digite o indice"))
    lista.append(n1*2)
print(lista)