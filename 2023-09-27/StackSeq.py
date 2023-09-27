"""StackSeq.py 백준 1874번 https://www.acmicpc.net/problem/1874"""

# 오늘 배운점 python보다 pypy가 더 빠르다.
# 이유: python은 인터프리터 언어이고 pypy는 컴파일 언어이기 때문

n = int(input()) # 수열의 길이가 입력된다. 
stack = []
result = [] # 결과를 저장하는 배열
max_v = 1
check = False

for _ in range(n):
  el = int(input())

  if el not in stack:
    for j in range(max_v, el+1):
      stack.append(j)
      result.append('+')
    max_v = el+1
  if el != stack.pop():
    check = True

  result.append('-')

if check:
  print('NO')
else:
  for v in result:
    print(v)