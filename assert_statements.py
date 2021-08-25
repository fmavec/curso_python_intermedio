def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = int(input("Ingresa un numero: "))
    #assert num.isnumeric(), "Debe ser un numero"
    #Tendrias que quitar el int y agregarlo en el print
    assert num >= 0, "Debe ser positivo"
    print(divisors(num))
    print("Terminó el programa")
    

if __name__ == '__main__':
    run()