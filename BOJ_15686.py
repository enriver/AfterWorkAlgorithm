# 치킨 배달 - G5

import sys
from itertools import combinations

def findChickenDistance(house,chicken):
    chickenDistance=list()
    for h in house:
        distance=int(1e9)
        for chkn in chicken: # 집에서 치킨집 까지의 최소거리 구하기
            distance=min(distance,abs(h[0]-chkn[0])+abs(h[1]-chkn[1]))

        chickenDistance.append(distance)

    # 치킨 거리의 합 반환
    return sum(chickenDistance) 


if __name__=="__main__":
    N,M = map(int,sys.stdin.readline().split())
    house=list()
    chicken=list()

    for i in range(1,N+1):
        for j,v in enumerate(list(map(int,sys.stdin.readline().split()))):
            if v==1: # 집의 좌표 저장
                house.append((i,j+1))
            elif v==2: # 치킨집의 좌표 저장
                chicken.append((i,j+1))

    minChickenDistance = int(1e9)
    for chickenComb in combinations(chicken,M): # 치킨집 중에서 M개를 뽑아서 최소값 구하기 (순열)
        minChickenDistance=min(minChickenDistance,findChickenDistance(house,chickenComb))

    print(minChickenDistance)