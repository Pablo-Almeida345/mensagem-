#3) Implementar um programa que recebendo um número limite, retorne uma lista contendo uma sequência
#do número limite até 1.

limite = int(input("Digite o limite"))
lista = []
#for numeros in range(limite, 0, -1):
#    lista.append(numeros) 
#print(lista)]

for numero in range (limite,0, -1):
    lista.insert(limite,numero)
print(lista)