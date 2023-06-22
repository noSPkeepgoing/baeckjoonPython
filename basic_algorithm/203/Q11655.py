import sys

S = list(sys.stdin.readline().rstrip())

for i in range(len(S)):
    if S[i].isalpha():
        if S[i].isupper():
            s = ord(S[i]) + 13 if ord(S[i]) <= 77 else ord(S[i]) - 13
        else:
            s = ord(S[i]) + 13 if ord(S[i]) <= 109 else ord(S[i]) - 13
        S[i] = chr(s)
print(''.join(S))
