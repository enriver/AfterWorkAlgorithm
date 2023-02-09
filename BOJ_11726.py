# 2xn 타일링 - S3

import sys

if __name__=="__main__":
    n=int(sys.stdin.readline())
    array=[0 for _ in range(n)]

    array[0]=1

    if n>1: # n이 1보다 클 경우에만
        array[1]=2

        for i in range(2,n):
            array[i]=array[i-1]+array[i-2]

    print(array[-1]%10007)