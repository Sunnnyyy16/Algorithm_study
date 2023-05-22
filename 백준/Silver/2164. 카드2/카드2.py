from collections import deque

n = int(input())
queue = deque()

# queue 만들기
for i in range(1,n+1):
    queue.append(i)

while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])
    