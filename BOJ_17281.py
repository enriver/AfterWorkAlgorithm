# 야구공 - G4

import sys
from itertools import permutations

'''
안타 :1
2루타:2
3루타:3
홈런 :4
아웃 :0
'''
def calcScore(b1,b2,b3,hit): # 점수 및 1루/2루/3루 상황 계산
    score=0
    
    if hit==1:
        score+=b3
        b1,b2,b3 = 1,b1,b2
    
    elif hit==2:
        score+=(b2+b3)
        b1,b2,b3 = 0,1,b1
    
    elif hit==3:
        score+=(b1+b2+b3)
        b1,b2,b3 = 0,0,1

    else:
        score+=(1+b1+b2+b3)
        b1,b2,b3 = 0,0,0
        
    return score,b1,b2,b3


def game(order,innings):
    n=len(innings)

    score=0
    now=0

    inning=1
    while inning <=n:
        b1,b2,b3 = 0, 0, 0
        outCnt=0

        # 3아웃이 아니라면
        while outCnt<3: # 해당 이닝의 선수 타석 결과
            cur = innings[inning-1][order[now]-1]
            if cur==0: # 아웃 -> 아웃카운트++
                outCnt+=1
            else:
                s,b1,b2,b3=calcScore(b1,b2,b3,cur)
                score+=s

            now+=1
            if now>8: # 9번타자까지 친 경우, 1번 타자부터 재시작
                now=0

        inning+=1
        
    return score

if __name__=="__main__":
    N = int(sys.stdin.readline())
    innings=list()

    for _ in range(N):
        innings.append(list(map(int,sys.stdin.readline().split())))

    maxScore=0
     # 2번타자부터 9번타자까지 나열 (순열)
    for comb in permutations([2,3,4,5,6,7,8,9],8):
        comb=list(comb)
        comb.insert(3,1) # 4번타자 자리에 1번 선수 지정
    
        maxScore = max(maxScore,game(comb,innings))

    print(maxScore)