# 퇴사 - S3

import sys

if __name__ == "__main__":
    N=int(sys.stdin.readline())
    dp=[0 for _ in range(N+1)]  # N일차에 받을 수 있는 가장 큰 금액
    T=list()
    P=list()

    for _ in range(N):
        t,p=map(int,sys.stdin.readline().split())
        T.append(t)
        P.append(p)

    for i in range(N):
        if i+T[i]<=N: # i일차에 시작하는 작업을 했을 때 N일을 넘어가는지
            dp[i+T[i]]=max(dp[i+T[i]], dp[i]+P[i])
        dp[i+1]=max(dp[i+1],dp[i]) # 가장 큰 금액 가져가기 / N+1 일의 값 계산

    print(dp[N])