def menor_elemento(lista, i):
    menor = i
    for j in range(i+1, len(lista)):
        if lista[j] < lista[menor]:
            menor = j
    return menor

def bubbleSort(lista):
    n = len(lista)
    for i in range(n):
        menor = menor_elemento(lista, i)
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista

lista = [12, 98, 45, 68, 25, 71, 39]
print(bubbleSort(lista))  