def main():
    my_list = [1, "Hola", True, 4.1]
    my_dict = {"Nombre": "Fernando", "Apellido": "Mavec"}
    

    super_list = [
        {"Nombre": "Fernando", "Apellido": "Mavec"},
        {"Nombre": "Chapis", "Apellido": "Caracas"},
        {"Nombre": "Orphen", "Apellido": "Barroso"},
        {"Nombre": "Charz", "Apellido": "Spectrum"},
        {"Nombre": "Axian", "Apellido": "Barroso"}
    ]


    super_dict = {
        "natural_nums" : [1, 2, 3, 4, 5],
        "integer_nums" : [-1, -2, 0, 1, 2],
        "floating_nums" : [1.1, 2.2, 6.6]
    }


    for key, value in super_dict.items():
        print(key, "-", value)
    

    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')


if __name__ == '__main__':
    main()