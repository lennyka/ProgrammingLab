def funzione(lista):
    somma = 0
    for item in lista:
        somma = somma + item
    print("La somma è: {}".format(somma))

def funz_sum(lista):
    print("La somma è sum: {}".format(sum(lista)))

number_list = [13,12,34,4,51,8,27,18]
funzione(number_list)
funz_sum(number_list)
