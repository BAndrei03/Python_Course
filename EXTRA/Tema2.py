# Insert CNP

cnp = input("Va rugam sa introduceti CNP-ul: ")

def main():

    if len(cnp) != 13:
        print(f"{cnp} nu este un CNP valid!")
    else:

        cnp_list = [int (i) for i in str(cnp)]
        # print(cnp_list)

        an = str(cnp[1]) + str(cnp[2])
        # print(an)


        if cnp_list[0] == 1:
            print("Sexul dv este masculin")
            an_final = '19' + an
            # print(f"V-ati nascut in anul {an_final}")
        elif cnp[0] == 2:
            print("Sexul dv este feminin")
            an_final = '19' + an
            # print(f"V-ati nascut in anul {an_final}")
        elif cnp[0] == 3:
            print("Sexul dv este masculin")
            an_final = '18' + an
            # print(f"V-ati nascut in anul {an_final}")
        elif cnp[0] == 4:
            print("Sexul dv este feminin")
            an_final = '18' + an
            # print(f"V-ati nascut in anul {an_final}")
        elif cnp[0] == 5:
            print("Sexul dv este masculin")
            an_final = '20' + an
            # print(f"V-ati nascut in anul {an_final}")
        elif cnp[0] == 6:
            print("Sexul dv este feminin")
            an_final = '20' + an
            # print(f"V-ati nascut in anul {an_final}")
        elif cnp[0] == 7:
            print("Sexul dv este masculin si rezident strain in Romania")
            an_final = '19' + an
            # print(f"V-ati nascut in anul {an_final}")
        elif cnp[0] == 8:
            print("Sexul dv este feminin si rezident strain in Romania")
            an_final = '19' + an
            # print(f"V-ati nascut in anul {an_final}")
        elif cnp[0] == 8:
            print("Sunteti strain in Romania")
            an_final = '19' + an
            # print(f"V-ati nascut in anul {an_final}")

        luna = str(cnp[3]) + str(cnp[4])
        lunile = {
            "01": "ianuarie",
            "02": "februarie",
            "03": "martie",
            "04": "aprilie",
            "05": "mai",
            "06": "iunie",
            "07": "iulie",
            "08": "august",
            "09": "septembrie",
            "10": "octombrie",
            "11": "noiembrie",
            "12": "decembrie",
        }
        ziua = str(cnp[5]) + str(cnp[6])
        # print(f"V-ati nascut in data de {ziua} {lunile[luna]} {an_final}")

        judete = {
            "01": "Alba",
            "02": "Arad",
            "03": "Arges",
            "04": "Bacau",
            "05": "Bihor",
            "06": "Bistrita-Nasaud",
            "07": "Botosani",
            "08": "Brasov",
            "09": "Braila",
            "10": "Buzau",
            "11": "Caras-Severin",
            "12": "Cluj",
            "17": "Galati",
        }

        judet = str(cnp[7]) + str(cnp[8])
        print(f"V-ati nascut in data de {ziua} {lunile[luna]} {an_final} in judetul {judete[judet]}.")

        dosar = str(cnp[9]) + str(cnp[10]) + str(cnp[11])
        print(f"Ati avut dosarul cu numarul {dosar}.")

        numar = "279146358279"
        numar_list = [int (i) for i in str(numar)]
        # print(numar_list)

        suma = 0

        for j in range (0,12):
            inmultit = int(cnp_list[j]) * int(numar_list[j])
            suma += inmultit
        rest = suma % 11
        if rest == 10:
            cifra_de_control = 1
        else:
            cifra_de_control = rest
        print(f"Cifra de control este {cifra_de_control}.")

if __name__  == "__main__":
    main()
