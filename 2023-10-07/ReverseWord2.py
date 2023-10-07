"""ReverseWord2.py 백준 17413번 https://www.acmicpc.net/problem/17413"""
# 1. <> 안에 있는 글자는 reverse 하지 않는다.
# 2. 나머지는 상관 없음 그리고 공백을 기준으로 단어를 구분하지 않는다.
import sys

S = sys.stdin.readline().strip() + ' '
stack = []  # 스택
inWord = False  # 괄호 안의 단어인지 판단하는 변수
result = ''  # 결과를 저장하는 변수

for c in S:
    # <를 만나면 이전에 문자들을 모두 뒤집는다.
    if c == '<':
        inWord = True
        for _ in range(len(stack)):
            result += stack.pop()

    stack.append(c)
    # >를 만나면 그 이전에 문자는 뒤집지 않고 넣는다.
    if c == '>':
        inWord = False
        for _ in range(len(stack)):
            result += stack.pop(0) # stack의 1번째 원소를 반환하고 제거한다.

    if c == ' ' and not inWord:
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '

# 결과 출력
print(result)
