# 이친수 - S3

import sys

if __name__=="__main__":
    N=int(sys.stdin.readline())
    array=[0 for _ in range(90)] # N은 90 이하이므로, MAX_LIMIT 으로 90설정
    array[0]=1
    array[1]=1

    for i in range(2,len(array)): # 피보나치와 같음
        array[i]=array[i-1]+array[i-2]

    print(array[N-1])