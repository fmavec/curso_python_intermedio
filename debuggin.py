def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input("Ingresa un numero: "))
        if num < 0:
            raise ValueError("Ingresa un numero positivo")
        print(divisors(num))
        print("Terminó el programa")
    except ValueError:
        print("Ingresa numero positivo")


if __name__ == '__main__':
    run()