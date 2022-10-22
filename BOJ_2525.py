# 오븐 시계 - B3

import sys

if __name__ =="__main__":
    A, B = map(int,sys.stdin.readline().split()) # A 시간, B 분

    C = int(sys.stdin.readline()) # C : 요리하는 데 필요한 시간

    m = (B+C)%60  # 최종 분
    h = A+(B+C)//60 # 최종 시

    if h >= 24 :
        print(h-24,m)
    else:
        print(h,m)