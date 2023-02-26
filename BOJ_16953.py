# A->B - S2

import sys
from collections import deque

def solve(start,goal):
    cnt=0
    que=deque()
    que.append((start,cnt))

    while que:
        value,cnt = que.popleft()

        if value == goal: # 목표로 하는 값과 같으면
            return cnt+1 # 연산횟수에 1을 더하여 리턴

        # 무한루프를 막기 위하여,
        # 목표로 하는 값보다 적을 경우에만 큐에 입력
        if value < goal:

            que.append((value*2,cnt+1))
            value=str(value)+'1'
            que.append((int(value),cnt+1))

    return -1

if __name__=="__main__":
    A,B=map(int, sys.stdin.readline().split())

    print(solve(A,B))