# 잃어버린 괄호 - S2

import sys


if __name__=="__main__":
    # 빼기를 기준으로 괄호를 치는 것이 가장 작은 수를 만들 수 있음
    expression = sys.stdin.readline().rstrip().split('-')

    result=0
    for i,e in enumerate(expression):
        for v in e.split('+'): # 괄호안의 합을 구한 후 빼줌
            if i==0: # 첫 식은 무조건 더함
                result+=int(v)
            else: # 첫 식이 아닌 경우 마이너스
                result-=int(v)

    print(result)
        