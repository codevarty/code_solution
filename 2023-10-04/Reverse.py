"""Reverse.py 백준 12605번 https://www.acmicpc.net/problem/12605"""


stack = []
n = int(input())

for i in range(1, n+1):
  st = list(input().split())
  for c in st:
    stack.append(c)
  print(f'Case #{i}:', end=' ')
  while len(stack) > 0:
    if len(stack) == 1:
      print(stack.pop())
    else:
      print(stack.pop(), end=' ')