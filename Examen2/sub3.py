def readFromTxtFile(file):
    file_products = open(file, "r")
    Lines = file_products.readlines()
    # fiecare linie din fisier este salvata ca element al listei Lines
    all_products = []
    all_products_append = []

    for line in Lines:
        all_products.append(line.strip().split(" "))
        a = line.strip().split(" ")
        arg_names = a[1::2]
        arg_values = a[2::2]
        attrs = {key: val for key, val in zip(arg_names, arg_values)}
        all_products_append.append([a[0], attrs])

    return all_products_append


def rulesForStandardComponents():
    standard = {}
    # creare dictionar pentru a respecta regulile
    standard['placuta_elec'] = {}
    standard["placuta_elec"]["latime"] = 0
    standard["placuta_elec"]["lungime"] = 0
    standard["placuta_elec"]["grosime"] = [0.4, 10]
    standard['microchip'] = {}
    standard["microchip"]["biti"] = 2
    standard["microchip"]["interfata"] = ['Analog', 'Digital']
    standard["microchip"]["memorie"] = [0.1, 3]
    standard['rezistor'] = {}
    standard["rezistor"]["rezistenta"] = 0
    standard["rezistor"]["material"] = ['Carbon', 'Ceramic']
    standard["rezistor"]["capete"] = [2, 9, 18]
    standard['cablu'] = {}
    standard["cablu"]["capat1"] = ['USB-C', 'microUSB']
    standard["cablu"]["capat2"] = ['HDMI/DVI', 'VGA/DVI']
    standard["cablu"]["lungime"] = [3, 5, 10, 15, 20]
    standard["cablu"]["izonare"] = ["Cauciuc", "Textil"]

    return standard


def checkStandard():
    all_products_list = readFromTxtFile("./products.txt")
    standard_rules = rulesForStandardComponents()

    for i in all_products_list:
        for k, v in standard_rules.items():
            # print(k)
            if k == i[0]:
                print(i[0])
    #Comparare cu regulile si afisare in fisiere diferite
    # print(all_products_list)
    # print(standard_rules)


if __name__ == "__main__":
    a = readFromTxtFile("products.txt")
    # print(a)
    checkStandard()
