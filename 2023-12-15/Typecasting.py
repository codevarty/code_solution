""" Typecasting.py 특강 문제 1 """


if __name__ == '__main__':
    lm = float(input('실수입력: '))

    inter = int(lm) % 10
    first = int(lm * 10) % 10

    print('정수 첫째 자리 :', inter)
    print('소수 첫째 자리 :', first)
    