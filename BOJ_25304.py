# 영수증 B5

import sys



if __name__=="__main__":
    X = int(sys.stdin.readline()) # 영수증에 적힌 총 금액
    N = int(sys.stdin.readline()) # 구매한 물건의 종류 수

    sum_price = 0
    for _ in range(N):
        a, b = map(int,sys.stdin.readline().split()) # 가격, 개수

        sum_price += a*b

    if sum_price == X:
        print('Yes')
    else:
        print('No')