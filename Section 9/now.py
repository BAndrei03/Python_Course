# travel_log ={
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"],
#               "total_visits": 12,
#                },
#     "Germany": {"cities_visited":["Berlin", "Frankfurt", "Hamburg"],
#                 "total_visits": 5, "carnati": "da"},
# }
#
# # print(travel_log.keys())
# #
# # travel_log["Spania"]="Orice"
# # print(travel_log.keys())
#
# dict_gol = {}
#
# lista = ['Andrei', 'Irina', 'Adi', 'Gay', 'Tu']
# var = 0
# for i in lista:
#     dict_gol[i] = var
#     var += 1
# print(dict_gol)

def suma_numere(a, b):

    print("caca maca", a + b)

def suma_numere_lista(lista_a):
    suma = sum(lista_a)
    print(suma)

def suma_dictionar(dictionar_a):
    aux = 0

    for k in dictionar_a:
        if k == 'Andrei':
            print(sum(dictionar_a[k]))
        elif k == 'Irina':
            for w in dictionar_a[k]:
                if w % 2 != 0:
                    aux += w
            print(aux)
        elif k == 'Adi':
            for o in dictionar_a[k]:
                if o == 0:
                    print("Suma nu poate fi realizata")
        elif k == 'Gay':
            for o in dictionar_a[k]:
                if o % 3 == 0:
                    print(f"Numarul {o} este divizibil cu 3")



if __name__ == "__main__":
    lista_numere=[]
    x = 5
    # print(x)
    # for i in range(0, 10):
    #     suma_numere(x,i)
    #
    # suma_numere(x,subreddits)
    for j in range(0, 10):
        lista_numere.append(j)

    # suma_numere_lista(lista_numere)
    lista = ['Andrei', 'Irina', 'Adi', 'Gay', 'Tu']
    dictionar_gol = {}

    for i in lista:
        dictionar_gol[i] = lista_numere
    suma_dictionar(dictionar_gol)
