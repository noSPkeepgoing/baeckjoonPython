N = int(input())
dot = 0

for i in range(1, N + 1) :
    dot += (i + 1) * (i + i / 2)
print(int(dot))