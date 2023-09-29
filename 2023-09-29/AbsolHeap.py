"""AbsoleHeap.py 백준 11286번 https://www.acmicpc.net/problem/11286"""
import sys
from queue import PriorityQueue

n = int(input())

myque = PriorityQueue()
data = [int(sys.stdin.readline()) for i in range(n)]

# print(data)
# 튜플로 저장하면 앞의 원소를 기준으로 우선순위가 정해진다.
# 절댓값 기준으로 하면 튜플을 생각하자
for v in data:
  if v == 0:
    if myque.empty():
      print(0)
    else:
      print(myque.get()[1])
  else:
    myque.put((abs(v), v))
