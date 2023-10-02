"""CallMiddle.py 백준 1655번 문제 https://www.acmicpc.net/problem/1655"""
import sys
import heapq

n = int(input())

max_heap = []
min_heap = []
lst = [] # 결과값을 저장하는 리스트

# max_heap과 min_heap의 첫번째 값을 비교해서 가운데 값을 가져온다.
for _ in range(n):
  v = int(sys.stdin.readline())

  if len(max_heap) == 0 or -max_heap[0] >= v:
    heapq.heappush(max_heap, -v)
  else :
    heapq.heappush(min_heap, v)
  
  if len(min_heap) - len(max_heap) >=2:
    heapq.heappush(max_heap, -heapq.heappop(min_heap))
  elif len(max_heap) - len(min_heap) >=2:
    heapq.heappush(min_heap, -heapq.heappop(max_heap))
  
  if len(min_heap) == 0:
    lst.append(v)
  else:
    if len(max_heap) >= len(min_heap):
      # print(-max_heap[0])
      lst.append(-max_heap[0])
    elif len(min_heap) >=1:
      # print(min_heap[0])
      lst.append(min_heap[0])


for v in lst:
  print(v)