"""CardSort.py 백준 1715번 https://www.acmicpc.net/problem/1715"""
# 두 묶음을 합쳐서 한다는 것이다.
# 4 값 넣는 횟수
# 5
# 6
# 7
# 8
# => 52
# 5 + 6 = 11
# 7, 8, 11
# 11, 15
# 26 + (11 + 15)
# 값을 더하고 그 더한 값을 다시 넣고 
# sum 두 값을 더한다.
import sys
import heapq
n = int(input())

data = [int(sys.stdin.readline()) for i in range(n)]
heap = []
sum = 0
for d in data:
  heapq.heappush(heap, d)

while len(heap) >1:
  temp = 0
  for _ in range(2): # 두 덩어리를 합친다.
    temp += heapq.heappop(heap) 
  sum += temp
  heapq.heappush(heap, temp)

print(sum)
