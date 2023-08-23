import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())

tree = [[] for _ in range(N+1)]
visited = [False]*(N+1)
ans = [0]*(N+1)

for _ in range(1,N):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
def dfs(num):
    visited[num] = True
    for i in tree[num]:
        if not visited[i]:
            ans[i] = num
            dfs(i)

dfs(1)

for i in range(2,N+1):
    print(ans[i])
    
    