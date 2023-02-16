# 적록색약 - G5

import sys
from collections import deque



# array   : RGB영역
# visit   : 해당 지점을 체크했는지 여부
# x, y    : 좌표 [x][y]
# colorDV : 적록 구분 여부 ('Y':구분 가능, 'N':구분 불가능-> 적록색약 )

def bfs(array,visit,x,y,colorDV):
    que=deque()
    que.append((x,y))

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    color = array[x][y]

    while que:
        x,y=que.popleft()

        for i in range(4):
            nx, ny =x+dx[i], y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                # 적록색약이 아니라면
                if colorDV=='Y':
                    if not visit[nx][ny] and array[nx][ny]==color:
                        visit[nx][ny]=True
                        que.append((nx,ny))
                # 적록색약이라면
                else:
                    if not visit[nx][ny]:
                        if color=='B': # 파란색 끼리만 영역 공유
                            if array[nx][ny]==color:
                                visit[nx][ny]=True
                                que.append((nx,ny))
                        else: # 파란색이 아니면 색 구분 x
                            if array[nx][ny]!='B':
                                visit[nx][ny]=True
                                que.append((nx,ny))

    return 1



if __name__=="__main__":
    N = int(sys.stdin.readline())
    visitColorDVyes=[[False for _ in range(N)] for _ in range(N)]
    visitColorDVno=[[False for _ in range(N)] for _ in range(N)]

    picture = list()

    for _ in range(N):
        rgb = sys.stdin.readline().rstrip()
        picture.append(rgb)

    colorDVyes=0 # 적록색약이 아닌 경우
    colorDVno=0 # 적록색약인 경우 (빨강==파랑)

    for i in range(N):
        for j in range(N):
            # 적록색약이 아닌 경우
            if not visitColorDVyes[i][j]:
                visitColorDVyes[i][j]=True
                colorDVyes+=bfs(picture,visitColorDVyes,i,j,'Y')

            # 적록색약인 경우
            if not visitColorDVno[i][j]:
                visitColorDVno[i][j]=True
                colorDVno+=bfs(picture,visitColorDVno,i,j,'N')

    print(colorDVyes,colorDVno)