# 최소비용 구하기 - G5

import sys
INF = int(1e9)

# 방문하지 않았으며, 최소 cost로 방문할 수 있는 node 찾기
def findMinNode(visit,dist,size):
    node=size
    minVal = INF

    for i in range(1,size+1):
        if visit[i]==False: # 방문하지 않았으며
            if dist[i] <= minVal: # 최소값
                minVal=dist[i]
                node = i # 노드 찾기

    return node

def dijkstra(start,end,graph,size):
    visit=[False for _ in range(size+1)]
    visit[start]=True

    # 해당지점까지 방문할 수 있는 최소거리 초기선언
    distance=graph[start]

    for _ in range(size):
        node = findMinNode(visit,distance,size)
        visit[node]=True

        # 해당 노드에서 출발한 경우, 인접 노드까지의 비용을 통해 distance update
        for i in range(1,size+1):
            if graph[node][i] != INF:
                distance[i] = min(distance[i], distance[node]+graph[node][i])

    return distance[end]


if __name__=="__main__":
    N = int(sys.stdin.readline()) # 도시의 개수
    M = int(sys.stdin.readline()) # 버스의 개수

    bus = [[INF for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        s,e,cost = map(int,sys.stdin.readline().split())
        bus[s][e]=min(bus[s][e],cost)
    
    sCity,eCity = map(int,sys.stdin.readline().split())

    if sCity == eCity:
        print(0)
    else:
        print(dijkstra(sCity,eCity,bus,N))