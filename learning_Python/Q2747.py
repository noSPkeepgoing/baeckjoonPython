n = int(input())
fibonacci = [0, 1]
while True:
    if len(fibonacci) > n :
        break
    fibonacci.append(sum(fibonacci[-1:-3:-1]))
print(fibonacci[n])