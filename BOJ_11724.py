# 연결 요소의 개수 - S2

import sys
from collections import deque,defaultdict

def bfs(graph,visit,x):
    que=deque()
    que.append(x)

    while que:
        k = que.popleft()

        # 연결되어 있는 정점중에
        for v in graph[k]: # 체크하지 않았으며, 또 다른 정점과 연결되어 있는 경우
            if not visit[v]:
                visit[v]=True
                que.append(v)

    return 1
        

if __name__=="__main__":
    #  N:정점의 개수, M:간선의 개수
    N,M = map(int,sys.stdin.readline().split())

    if M==0: # 간선의 개수가 없다면
        print(N) # 정점의 개수를 출력하고
        sys.exit() # 종료
    
    # 서로 연결되어있는 정점을 담기위한 dictionary 선언 (default : list)
    graph=defaultdict(list)
    for _ in range(M):
        u,v = map(int,sys.stdin.readline().split())

        graph[u].append(v)
        graph[v].append(u)

    cnt=0
    visit=[False for _ in range(N+1)] # 해당 정점을 체크했는지 여부 확인
    for i in range(1,N+1):
        if not visit[i] :
            visit[i]=True
            cnt+=bfs(graph,visit,i)

    print(cnt)
    