"""Stack.py 백준 10828번 문제: https://www.acmicpc.net/problem/10828"""
# 이 문제에서 중요한 것은 시간이 0.5초로 짧다는 것
# 여기서 사용한 것이 getattr함수이다.
class StackDef:
    def push(stack, value):
        stack.append(value)
        return stack
    
    def pop(stack, result):
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(int(stack[-1]))
            stack.pop()
        return stack, result
    
    def size(stack, result):
        result.append(len(stack))
        return stack, result

    def empty(stack, result):
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
        return stack, result
    
    def top(stack, result):
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(int(stack[-1]))
        return stack, result


stack = []
result = [] # 결과 값을 저장하는 리스트
for i in range(int(input())):
    inputValue = input().split(" ")
    if len(inputValue) == 1:
        # getattr함수를 사용하여 클래스의 메소드를 동적으로 사용가능
        stack, result = getattr(StackDef, inputValue[0])(stack, result)
    else:
        stack = getattr(StackDef, inputValue[0])(stack, inputValue[1])
    
for j in result: # 결과값을 출력
    print(j)
