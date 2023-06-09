N,K = map(int,input().split())
money = [0]*N

for i in range(N):
    money[i] = int(input())

money.sort(reverse=True)
count = 0

for m in money:
    if m <= K:
        count += K//m
        K = K%m

print(count)