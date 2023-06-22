word = input()
alphabet = [0] * 26

for i in word:
    alphabet[ord(i)-97] += 1

print(*alphabet)
