n=int(input()) 
v=int(input()) 
graph = [[] for i in range(n+1)] 
visited=[0]*(n+1) 

for i in range(v): 
    a,b=map(int,input().split())
    graph[a].append(b) 
    graph[b].append(a)
    
def dfs(start):
    visited[start]=1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            
dfs(1)
print(sum(visited)-1)