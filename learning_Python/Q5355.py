T = int(input())
oper = []
for i in range(T):
    oper = input().split()
    for j in range(len(oper)):
        if j == 0:
            n = float(oper[j])
        elif oper[j] == '@':
            n = n * 3
        elif oper[j] == '%':
            n = n + 5
        elif oper[j] == '#':
            n = n - 7
    print("{:.2f}".format(n))

    