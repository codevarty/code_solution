""" Root.py 특강 문제 4 """

if __name__ == '__main__':
    a, b = map(int, input('두 정수 입력').split())

    print('산술평균 :', (a + b) / 2)
    print('기하평균 :', (a * b) ** 0.5)
    print('조회평균 :', 2 * a * b / (a + b))
    