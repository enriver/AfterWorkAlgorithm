# 영역 구하기 - S1

import sys
from collections import deque

def solve(x,y,paper):
    global M,N

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    que=deque()
    que.append((x,y))

    area=0
    while que:
        x,y=que.popleft()
        area+=1

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if 0<=nx<M and 0<=ny<N:
                if not paper[nx][ny]:
                    paper[nx][ny]=True
                    que.append((nx,ny))

    return area

if __name__=="__main__":
    M,N,K = map(int,sys.stdin.readline().split())

    paper=[[False for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        x1,y1,  x2,y2 = map(int,sys.stdin.readline().split())
        
        for i in range(y1,y2): 
            for j in range(x1,x2):
                paper[i][j]=True # 입력받은 좌표 사이의 모눈종이 채우기

    cnt=0
    area=list()

    for i in range(M):
        for j in range(N):
            if not paper[i][j]:
                paper[i][j]=True
                cnt+=1
                area.append(solve(i,j,paper))

    print(cnt)
    print(*sorted(area))
