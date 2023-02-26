def initialization(size):
    spiral = []
    for i in range(size):
        x = []
        for j in range(size):
            x.append(0)
        spiral.append(x)

    return spiral


def printm(spiral):
    global size
    for i in range(size):
        for j in range(size):
            print(spiral[i][j], end="\t")
        print()


def transponition():
    global spiral
    global size
    x = []
    for i in range(size):
        x1 = []
        for j in range(size):
            x1.append(0)
        x.append(x1)
    for i in range(size):
        for j in range(size):
            x[i][j] = spiral[j][i]
    spiral = x


def reflection():
    global spiral
    global size
    spiral2 = []
    for i in range(size):
        m = []
        for j in range(size):
            m.append(0)
        spiral2.append(m)
    for i in range(size):
        for j in range(size):
            spiral2[i][j] = spiral[i][size - j - 1]
    spiral = spiral2
while True:
    size = int(input("Введите число N или -1 для выхода\n-> "))
    if(size == -1):
        break
    spiral = initialization(size)
    summa = 1
    ind = 0
    start = 0
    stop = size - 1
    if start == stop:
        spiral[0][0] = 1
    else:
        while summa <= size * size:
            for h in range(4):
                for i in range(start, stop):
                    spiral[ind][i] = summa
                    summa += 1
                reflection()
                transponition()

            ind += 1
            start += 1
            stop -= 1
            if start == stop:
                spiral[start][stop] = summa
                summa += 1
    printm(spiral)
    print()
