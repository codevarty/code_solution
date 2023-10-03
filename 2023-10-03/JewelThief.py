"""JewelThief.py 백준 1202번 https://www.acmicpc.net/problem/1202"""
import sys
import heapq

# 가격의 합을 저장하는 변수 생성
sum = 0
# N과 K를 입력 받는다.
N, K = map(int, input().split())
# N개의 줄에는 보석에 대한 정보가 입력된다. (무게, 가격)
data = []
for _ in range(N):
  a, b = map(int, sys.stdin.readline().split())
  # tuple(무게, 가격)
  data.append((a, b))

# 무게 기준으로 정렬한다.
data.sort(key=lambda x: (x[0]))

# 가방에 대한 정보(무게 한도)를 입력한다. 그 후 바로 오름차순으로 정렬한다.
bag = sorted(int(sys.stdin.readline()) for i in range(K))


tmp = []
for weight in bag:
  while data and data[0][0] <= weight:
    heapq.heappush(tmp, -data[0][1])
    heapq.heappop(data)
  if tmp:
    sum += -heapq.heappop(tmp)

# 보석 총합 출력
print(sum)