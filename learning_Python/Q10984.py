T = int(input())

for i in range(T) :
    N = int(input())
    c_sum = g_sum = 0
    for j in range(N) :
        c, g = input().split()
        c_sum += int(c)
        g_sum += float(g) * int(c)
    print(c_sum, '%.1f' % (g_sum / c_sum))
