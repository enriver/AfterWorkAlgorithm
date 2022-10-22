# 행렬 덧셈 - B5

import sys

if __name__=="__main__":
    n,m = map(int, sys.stdin.readline().split())

    result = [[0 for _ in range(m)] for _ in range(n)] # 결과를 담을 2차원 배열

    for _ in range(2):
        for i in range(n):
            v = list(map(int, sys.stdin.readline().split())) # 행렬 값 받기

            for j in range(m):
                result[i][j] += v[j]
            
    for i in range(n):
        for j in range(m):
            print(result[i][j],end=' ')
        print()
