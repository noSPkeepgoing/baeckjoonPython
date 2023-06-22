import sys

S = sys.stdin.readline().rstrip()
alphabet = [-1] * 26

for s in S:
    alphabet[ord(s)-97] = S.index(s)

print(*alphabet)
