import sys
input = sys.stdin.readline
N,M = map(int, input().split())
nums = list(map(int, input().split()))

sum_list = [0]
temp = 0

for i in nums:
    temp = temp + i
    sum_list.append(temp)

for i in range(M):
    a,b = map(int,input().split())
    print(sum_list[b]-sum_list[a-1])