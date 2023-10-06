"""ATM.py 백준 11399번 https://www.acmicpc.net/problem/11399"""
# ATM을 하는데 시간의 합 최소 값을 구하는 문제

n = int(input())
# 시간이 최소가 되기 위해서는 오름 차순으로 정렬한다.
lst = sorted(list(map(int, input().split())))

sum =0
for i in range(1, n+1):
  # 각 사람이 기다리는 시간을 더한다
  for v in lst[:i]:
    sum +=v

# 시간을 출력한다.
print(sum)