# 연속합 - S2

import sys

if __name__=="__main__":
    n = int(sys.stdin.readline())
    array = list(map(int,sys.stdin.readline().split()))

    # 입력받은 array를 answer를 구하는 저장소로 사용
    for i in range(1,n):
        array[i]=max(array[i-1]+array[i], array[i]) # 해당 인덱스 값까지 진행했을 때 최대값을 저장

    print(max(array))