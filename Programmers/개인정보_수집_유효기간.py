# 프로그래머스 2023 KAKAO BLIND RECRUITMENT
# 개인정보 수집 유효기간 : LEVEL1 

from collections import defaultdict

def solution(today, terms, privacies):
    answer=list()
    
    # . 을 기준으로 연/월/일 구분
    tYear,tMonth,tDay = map(int,today.split('.'))
    
    termDict = defaultdict() # 약관 정보 저장
    for term in terms:
        term = term.split()
        termDict[term[0]] = int(term[1])
    
    i=0
    for privacy in privacies:
        i+=1
        privacy = privacy.split()
        year,month,day = map(int,privacy[0].split('.'))
        
        addedM = termDict[privacy[1]] # 약관 정보를 통해 유효기간 불러오기
        q,r = addedM//12 , addedM % 12
        
        # 유효기간 일자 계산
        year+=q
        month+=r
        
        if month > 12 :
            year+=1
            month-=12
            
        if tYear < year :
            continue
        elif tYear == year:
            if tMonth < month :
                continue
            elif tMonth == month :
                if tDay < day :
                    continue
                else : # tDay >= day
                    answer.append(i)
            else: # tMonth > month :
                answer.append(i)
        else: # tYear > year
            answer.append(i)
        
    return answer