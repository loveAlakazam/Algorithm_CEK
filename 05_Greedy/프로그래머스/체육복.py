# -*- coding: utf-8 -*-
# 그리디- 프로그래머스- 체육복
import sys
def solution(n, lost, reserve):
    #lost와 reserve를 오름차순으로 정렬
    lost=set(lost)
    reserve=set(reserve)
    
    # 옷을 도난당한 학생을 제외한 나머지 학생만 카운트
    answer=n-len(lost)

    # 여벌의 옷을 갖고 있는 학생이
    # 다른학생에게 체육복을 빌릴 수 있는지 확인
    # is_reserve[i]=1  : i-1번째, i+1번째 학생이 잃어버렸다면, 빌려줄 수 있다.
    # is_reserve[i]=0 : 빌려줄 수 없다.
    is_reserve=[0]*(n+1)

    #both : 여벌의 옷을 갖고 있는 학생이 도난 당한경우
    both=lost & reserve
    #여벌의 옷을 갖고 있는 학생은
    #빌려줄수 없지만 체육수업은 들을 수 있다.
    answer+=len(both)
    print('both: ', both ,len(both))
    
    for r in reserve:
        if not(r in both):
            is_reserve[r]=1

    #도난당한 학생 : 체육복도난 + 체육수업 못들음
    #전체 lost에서 both에 해당하는 학생을 빼야함.
    # 전체 reserve에서 both에 해당하는 학생을 빼야함
    lost= lost-both
    reserve= reserve-both
    print('lost-both=',lost)
    print('reserve-both=',reserve)
    
    for l in lost:
        print('now: ', l,'\nis_preserve: ', is_reserve)
        print('answer: ', answer,'\n')
        sizedown=l-1
        sizeup=l+1
        if (sizedown>=1) and (is_reserve[sizedown]==1):
            answer+=1
            is_reserve[sizedown]=0
            
        elif (sizeup<=n) and (is_reserve[sizeup]==1):
            answer+=1
            is_reserve[sizeup]=0
            
    print('is_reserve: ', is_reserve)
    return answer

def main():
    test_case= int(sys.stdin.readline())
    for t in range(test_case):
        n= int(sys.stdin.readline())
        lost=list(map(int, sys.stdin.readline().split()))
        reserve=list(map(int, sys.stdin.readline().split()))
        print(solution(n, lost, reserve))

if __name__=='__main__':
    main()
