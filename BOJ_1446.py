# 지름길 - S1

import sys

if __name__=="__main__":
    # 지름길의 개수 N, 고속도로의 길이 D
    N,D = map(int,sys.stdin.readline().split())

    # 해당 지점에 도착할 수 있는 최단 거리
    dp=[i for i in range(D+1)]

    road=dict()
    for _ in range(N):
        # 시작지점 s, 도착지점 e, 지름길의 길이 l
        s,e,l = map(int,sys.stdin.readline().split())
        if s not in road.keys():
            road[s]=list()

        road[s].append([e,l])

    for i in range(D+1):
        if i!=0: # 해당 지점까지의 최단 거리를 업데이트 하기위해, 이전 지점+1 과 비교
            dp[i]=min(dp[i],dp[i-1]+1)

        # 해당 지점에서 시작되는 지름길이 있다면
        if i in road.keys():
            for v in road[i]:
                # 도착지점 v[0] - 시작지점 i >= 지름길의 길이 v[1] 라면
                if v[0]-i >= v[1]:
                    if v[0]>D: # 도착지점이 목표지점보다 멀면 continue
                        continue
                    # 해당지점에 지름길을 통해서 간 것과, 기존의 값 비교
                    dp[v[0]]=min(dp[v[0]], dp[i]+v[1])

    print(dp[D])