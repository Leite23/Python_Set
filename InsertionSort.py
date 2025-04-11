def insere_elemento(lista, i):
    elemento = lista[i]
    j = i - 1
    while j >= 0 and lista[j] > elemento:
        lista[j + 1] = lista[j]
        j -= 1
    lista[j + 1] = elemento
    return lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 17]
i = 8
lista[i] = 189
#lista.append(189)  
#i = len(lista) - 1
print(insere_elemento(lista, i)) 