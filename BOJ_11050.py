# 이항 계수 1 - B1

import sys

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

if __name__=="__main__":
    N, K = map(int, sys.stdin.readline().split())

    print(factorial(N)/(factorial(N-K)*factorial(K)))
