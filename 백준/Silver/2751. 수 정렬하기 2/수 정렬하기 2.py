import sys
input = sys.stdin.readline

N=int(input())
A =[0]*int(N+1)

for i in range(1,N+1):
    A[i]=int(input())

A.pop(0)
A.sort()

for i in range(N):
    sys.stdout.write(str(A[i])+'\n')