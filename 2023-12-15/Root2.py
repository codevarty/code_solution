""" Root2.py 특강 문제 5 """

if __name__ == '__main__':
    a, b, c = map(int, input('세 정수 입력 : ').split())

    root = b ** 2 - 4 * a * c

    if root == 0:
        r = -b / 2 * a
        print('중근 :', r)
    elif root < 0:
        print('근이 없음')
    else:
        r1 = (-b + root ** 0.5) / 2 * a
        r2 = (-b - root ** 0.5) / 2 * a
        print('두 실근 :', r1, r2)
