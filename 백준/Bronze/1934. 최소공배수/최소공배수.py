T = int(input())
def gcd(n,m):
    while m > 0:
        n,m = m, n%m
    return n
for i in range(T):
    N,M = map(int,input().split())
    gcd_num=gcd(N,M)
    lcm_num = (N*M)//gcd_num
    print(lcm_num)
    