# 평균은 넘겠지 - B1

import sys

if __name__=="__main__":
    C = int(sys.stdin.readline()) # 테스트 케이스 수

    for _ in range(C):
        scores = list(map(int, sys.stdin.readline().split()))
        
        # scores[0] : 학생 수, scores[1:] : 점수
        avg = sum(scores[1:])/scores[0] # 평균값

        over_avg=list(filter(lambda x : x > avg, scores[1:])) # 평균보다 높은 점수
        percentile = (len(over_avg)/scores[0])*100

        print('{0:0.3f}%'.format(percentile))