# 효율적인 해킹 - S1

import sys
from collections import deque

def dfs(key):
    global N
    global computer

    visit=[False for _ in range(N+1)]
    visit[key]=True

    cnt = 0
    que=deque()
    que.append(key)

    while que:
        key = que.popleft()
        cnt+=1 # 신뢰 대상 컴퓨터가 등장할 때마다 cnt 1씩 증가

        # key computer를 신뢰하는 value computer 목록 탐색
        for comp in computer[key]:
            if not visit[comp]:
                visit[comp]=True
                que.append(comp)

    return cnt


if __name__=="__main__":
    N,M = map(int,sys.stdin.readline().split())

    computer=[list() for _ in range(N+1)]
    for _ in range(M):
        A,B = map(int,sys.stdin.readline().split()) # A가 B를 신뢰한다

        computer[B].append(A) # B를 해킹하면 A도 해킹할 수 있다

    result=[0 for _ in range(N+1)]
    
    for i in range(1,N+1):
        result[i]=dfs(i)

    maxVal = max(result)
    for i in range(1,N+1):
        if result[i]==maxVal:
            print(i,end=' ')