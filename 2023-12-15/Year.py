""" Year.py 특강 문제 2 """

if __name__ == '__main__':
    year = int(input("년도 입력: "))

    if year % 4 == 0 and year % 100 != 0:
        print('366년')
    elif year % 400 == 0:
        print('366년')
    else:
        print('365년')
