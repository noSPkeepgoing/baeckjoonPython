import sys

str = sys.stdin.readline().rstrip()
result = []

for i in range(len(str)):
    result.append(str[i:])

result.sort()
for _ in result:
    print(_)
