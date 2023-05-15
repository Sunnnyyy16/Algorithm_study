n = input()
score_list = list(map(int,input().split()))

max_score = max(score_list)
sum_score = sum(score_list)

print(sum_score*100/max_score/int(n))