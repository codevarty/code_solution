"""MinHeap.py 백준 1927문제 https://www.acmicpc.net/problem/1927"""
import heapq
n = int(input())

heap = []
result = []
for _ in range(n):
  a = int(input())
  if len(heap) == 0 and a ==0:
    result.append(0)
  elif a ==0:
    result.append(heapq.heappop(heap))
  else:
    heapq.heappush(heap, a)


for v in result:
  print(v)