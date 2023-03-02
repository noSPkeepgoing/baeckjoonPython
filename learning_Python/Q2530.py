A, B, C = map(int, input().split())
D = int(input())

H = ((((C + D) // 60 + B) // 60) + A) % 24
M = ((C + D) // 60 + B) % 60
S = (C + D) % 60

print(H, M, S)