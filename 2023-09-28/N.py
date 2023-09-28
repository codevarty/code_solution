""" N.py 백준 2075번 https://www.acmicpc.net/problem/2075"""
# 힙큐 문제
import heapq

n = int(input())

heap = []
# 리스트가 길어지면 메모리가 초과 된다. (메모리가 12MB로 제한)
for _ in range(n):
  for elm in list(map(int, input().split())):
    heapq.heappush(heap, elm)
    if len(heap) > n: # 힙큐는 가장 작은 값을 제거하니 길이를 n까지 고정하면 가장 작은 것이 n번째로 큰 수가 된다.
      heapq.heappop(heap)

print(heapq.heappop(heap))