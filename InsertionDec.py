def insere_elemento_decrescente(lista, i):
    elemento = lista[i]
    j = i - 1
    while j >= 0 and lista[j] < elemento:
        lista[j + 1] = lista[j]
        j -= 1
    lista[j + 1] = elemento
    return lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 8
lista[i] = 6
print(insere_elemento_decrescente(lista, i))  