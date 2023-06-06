N = int(input())
A = list(map(int, input().split()))
M = int(input())
x = list(map(int, input().split()))
A.sort()			

for i in x:
    start, end = 0, N - 1		
    finding = False		

    # 이분탐색 시작
    while start <= end:		
        mid = (start + end) // 2	
        if i == A[mid]:	
            finding = True	
            print(1)		
            break		
        elif i > A[mid]:	
            start = mid + 1	
        else:			
            end = mid - 1	

    if not finding:		
        print(0)		