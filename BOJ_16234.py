# 인구 이동 - G5

import sys,math
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def solve(x,y,moved,visit):
    global N,L,R,A

    summation = A[x][y] # 합계
    area=list()

    que=deque()
    que.append((x,y))

    while que:
        x,y = que.popleft()
        area.append((x,y))

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if not visit[nx][ny] and L<=abs(A[nx][ny]-A[x][y])<=R: # 해당 나라에 방문한 적이 없으며, 두 나라의 인구 차이가 L 이상 R이하라면
                    visit[nx][ny]=True
                    summation+=A[nx][ny] # 인구수 더하기
                    que.append((nx,ny))

                    moved+=1 # 인구이동이 있었음을 체크
    
    avg = math.floor(summation/len(area)) # 연합의 인구수 / 연합을 이루고 있는 칸의 개수 , 소수점 버리기

    for idx in area:
        A[idx[0]][idx[1]]=avg # 인구수 분할

    return moved


if __name__=="__main__":
    N,L,R = map(int,sys.stdin.readline().split())
    A=list()
    
    for _ in range(N):
        A.append(list(map(int,sys.stdin.readline().split())))

    day=0
    moved=1
    while True:
        if moved==0: # 이동한 적이 없다면
            break
    
        moved=0
        visit=[[False for _ in range(N)] for _ in range(N)] # 해당 나라 방문 check

        for i in range(N):
            for j in range(N):
                if not visit[i][j]:
                    visit[i][j]=True
                    moved += solve(i,j,moved,visit)
    
        if moved > 0 : # 이동하였다면
            day+=1

    print(day)