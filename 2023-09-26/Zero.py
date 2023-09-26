"""Zero.py 백준 10773문제: https://www.acmicpc.net/problem/10773"""

N = int(input())

stack = [] # stack 저장
for _ in range(N):
  a = int(input())
  if a ==0:
    stack.pop()
  else:
    stack.append(a)

print(sum(stack))