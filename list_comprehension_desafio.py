def run():
    #List Comprehension
    multiples=[i for i in range(0, 10001) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]


    print(multiples)


if __name__ == '__main__':
    run()