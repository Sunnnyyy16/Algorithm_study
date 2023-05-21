import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
goods = list(map(int,input().split()))
goods.sort()

count = 0
i = 0
j = N-1

while i<j:
    if goods[i]+goods[j]<M:
        i+=1
    elif goods[i]+goods[j]>M:
        j -=1
    else:
        count+=1
        i+=1
        j-=1
        
print(count)