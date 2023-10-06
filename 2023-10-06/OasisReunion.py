"""OasisReunion.py 백준 3015번 문제 https://www.acmicpc.net/problem/3015"""

# 상대방과 서로 볼 수 있는 경우는 큰 사람이 가운데 없다.
# 크게 2가지 경우
# 1. 다음 사람이 나와 키가 같다.
# 2. 다음 사람이 나와 크기가 다른 경우
# 아래는 2번의 세부 사항
# 2-1 다음 사람이 나보다 키가 큰 경우
# 2-2 다음 사람이 나보다 키가 작은 경우
import sys
# 줄을 서는 사람의 수 입력
num = int(sys.stdin.readline())

line = []
# # 줄을 서는 사람의 크기가 리스트에 저장된다.
for _ in range(num):
  line.append(int(sys.stdin.readline()))

stack = []
count = 0

# 줄을 선 사람들 만큼 반복 한다.
for v in line:

  # 다음 사람이 나보다 키가 큰 경우
  while stack and stack[-1][0] < v:
    print(*stack)
    count += stack.pop()[1]

  if not stack:
    stack.append((v,1))
    continue

  # 크기가 같은 경우
  if stack[-1][0] == v:
    cnt = stack.pop()[1]
    count += cnt
    if stack: count +=1
    stack.append((v, cnt+1))
  # 상대방과 크기가 다른 경우
  else:
    print('크기가 다릅니다.')
    stack.append((v,1))
    print(*stack)
    count +=1
print(count)