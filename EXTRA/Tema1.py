# De generat 5 liste cu elemente random.

# Se cere:
# Suma elementelor listelor individuale
# Care este lungimea fiecarei liste ?
# Incearca sa combini toate cele liste intr-o lista mai mare
# Suma totala a listelor ( trebuiie sa fii atent la numele ca sunt generate random )
# Cauta numerele pare din acea lista mare
# Cauta numerele divizibile cu 3 daca nu sunt atunci sa afisezi un mesaj de eroare.


import random

list1 = random.sample(range(0, 9), random.randint(4, 4))
list2 = random.sample(range(0, 9), random.randint(1, 4))
list3 = random.sample(range(0, 9), random.randint(1, 4))
list4 = random.sample(range(0, 9), random.randint(1, 4))
list5 = random.sample(range(0, 9), random.randint(1, 4))

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)

# Suma elementelor listelor individuale

print(f"Suma listelor individuale este:\n{sum(list1)}\n"
      f"{sum(list2)}\n{sum(list3)}\n{sum(list4)}\n{sum(list5)}\n")

# Care este lungimea fiecarei liste ?

print(f"Lungimea listelor este:\n{len(list1)}\n"
      f"{len(list2)}\n{len(list3)}\n{len(list4)}\n{len(list5)}\n")

# Incearca sa combini toate cele liste intr-o lista mai mare

lista_totala = [list1, list2, list3, list4, list5]

list_tmp = []
list_tmp.extend(list1)
list_tmp.extend(list2)
list_tmp.extend(list3)
list_tmp.extend(list4)
list_tmp.extend(list5)

print(lista_totala)
print(list_tmp)

sumi=sum(list1) +sum(list2)+sum(list3)+sum(list4)+sum(list5)
print(sumi)


# Cauta numerele pare din acea lista mare
lista_new =[]
lista_div3 =[]
# for i in range(0, 5):
#     for j in range(0,len(list1)-1):
#         if lista_totala[i][j] % 2 ==0:
#             lista_new += lista_totala[i][j]
#     for j in range(0, len(list2)-1):
#         if lista_totala[i][j] % 2 == 0:
#             lista_new += lista_totala[i][j]
#     for j in range(0,len(list3)-1):
#         if lista_totala[i][j] % 2 ==0:
#             lista_new += lista_totala[i][j]
#     for j in range(0,len(list4)-1):
#         if lista_totala[i][j] % 2 ==0:
#             lista_new += lista_totala[i][j]
#     for j in range(0,len(list5)-1):
#         if lista_totala[i][j] % 2 ==0:
#             lista_new += lista_totala[i][j]
#     print(lista_new)

for i in list_tmp:
    if i % 2 == 0:
        print("Numarul este par", i)
        lista_new.append(i)
    if i % 3 == 0:
        print("Numarul este divizibil cu 3", i)
        lista_div3.append(i)
    else:
        print("Numarul nu este divizibil")
print(lista_new, lista_div3)

print(f"Asta este tmp\n {list_tmp}")
list_tmp.sort()
print(list_tmp)

list_tmp = list(dict.fromkeys(list_tmp))
print(list_tmp)

ooo = [1]
for k in list_tmp:
    if k in ooo:
        ooo.append(k)
print(ooo)
