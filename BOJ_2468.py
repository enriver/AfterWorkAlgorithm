# 안전 영역 - S1

import sys
from collections import deque

def bfs(area,visit,x,y,size):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    que=deque()
    que.append((x,y))

    while que:
        x,y = que.popleft()

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if 0<=nx<size and 0<=ny<size:
                if not visit[nx][ny] and area[nx][ny]>0:
                    visit[nx][ny]=True
                    que.append((nx,ny))

    return 1

def checkArea(size,area):
    for i in range(size):
        for j in range(size):
            area[i][j]-=1

    visit=[[False for _ in range(size)] for _ in range(size)]

    cnt=0
    for i in range(size):
        for j in range(size):
            if not visit[i][j] and area[i][j]>0:
                visit[i][j]=True
                cnt+=bfs(area,visit,i,j,size)

    return cnt
            


if __name__=="__main__":
    N=int(sys.stdin.readline())
    area=list()
    maxDepth=0
    for _ in range(N):
        row=list(map(int,sys.stdin.readline().split()))
        maxDepth=max(maxDepth, max(row)) # 해당 지역의 최고 높이 저장
        area.append(row)

    safeAreaCnt=1 # 높이는 최소 1이상이므로, 적어도 1개의 안전영역이 보장됨
    for _ in range(maxDepth+1): # 1 최고높이 -> 0 이 될 때 까지 1씩 잠기게하는 작업 반복
        safeAreaCnt=max(safeAreaCnt,checkArea(N,area))

    print(safeAreaCnt)