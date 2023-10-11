"""GoodWord.py 백준 3986번 https://www.acmicpc.net/problem/3986"""

import sys

n = int(sys.stdin.readline())
stack = []
result = 0  # 결과 값 저장

# 입력 받은 값 만큼 반복한다.
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    for c in s:
        # 문자가 연속적으로 나올 경우 스택에서 제거한다.
        if stack and stack[-1] == c:
            stack.pop()
            continue
        # 값을 스택에 넣는다.
        stack.append(c)
    # 스택의 길이가 1인 경우는 한 글자가 짝을 지을 수 없기 때문 => X
    if len(stack) == 1:
        stack.clear()
        continue
    # 스택의 길이가 0이거나 양쪽의 값이 같으면 좋은 단어이다.
    if (len(stack) == 0) or (stack[0] == stack[-1]):
        result += 1
    stack.clear()

# 결과값 출력
print(result)
