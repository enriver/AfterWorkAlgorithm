# 1,2,3 더하기 - S3

import sys

if __name__=="__main__":
    T=int(sys.stdin.readline()) # 테스트케이스
    array=[0 for _ in range(11)] # n은 양수이며 11보다 작다 (MAX :10)

    array[1]=1
    array[2]=2
    array[3]=4

    for i in range(4,11): # i번째 값은 i-1, i-2, i-3 번째 값의 합과 같다
        array[i]=array[i-1]+array[i-2]+array[i-3]

    for _ in range(T):
        n=int(sys.stdin.readline())

        print(array[n])