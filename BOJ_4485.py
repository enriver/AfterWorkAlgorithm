# 녹색 옷 입은 애가 젤다지? - G4

import sys
from collections import deque

INF = int(1e9)

def solve(x,y,cave,cost,N):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    que=deque()
    que.append((x,y))

    cost[x][y]=cave[x][y]

    while que:
        x,y = que.popleft()

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if 0<=nx<N and 0<=ny<N: # 최소 값인 경우 갱신
                if cost[nx][ny] > cost[x][y] + cave[nx][ny]:
                    cost[nx][ny] = cost[x][y] + cave[nx][ny]
                    que.append((nx,ny))

if __name__=="__main__":
    i=0
    while True:
        N = int(sys.stdin.readline()) # 동굴의 크기

        if N==0:
            break

        i+=1
        cave=list()
        cost=[[INF for _ in range(N)] for _ in range(N)]
        for _ in range(N):
            cave.append(list(map(int,sys.stdin.readline().split())))

        solve(0,0,cave,cost,N)

        # [N-1][N-1] 에 도달한 값 print
        print('Problem {0}: {1}'.format(i,cost[N-1][N-1]))