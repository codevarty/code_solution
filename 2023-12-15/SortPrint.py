""" SortPrint.py 특강 문제 7 """

if __name__ == '__main__':
    a, b, c = map(int, input('세 정수 입력 : ').split())
    lst = []
    lst.append(a)
    lst.append(b)
    lst.append(c)

    lst.sort()

    for item in lst:
        print(item, end=' ')
