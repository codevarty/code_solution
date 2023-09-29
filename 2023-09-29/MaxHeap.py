"""MaxHeap.py 백준 11279문제 https://www.acmicpc.net/problem/11279"""

import sys
from queue import PriorityQueue

n = int(input())

myque = PriorityQueue()
data = [int(sys.stdin.readline()) for i in range(n)]

for d in data:
  if d == 0:
    if myque.empty():
      print(0)
    else:
      print(-myque.get())
  else:
    myque.put(-d)
