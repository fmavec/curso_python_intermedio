def run():
    squares=[]
    for i in range(0, 101):
        if i % 3 != 0:
            squares.append(i**2)

    
    print(squares)


if __name__ == '__main__':
    run()