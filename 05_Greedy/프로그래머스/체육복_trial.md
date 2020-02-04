# 시도1 (테스트 1, 6, 7 에서 실패)
- (반례) 질문 확인결과 n=3, lost=[1,2,3], reserve=[1,2,3]일때 최대 체육수업듣는 학생수: 3명
- 코드
```python
def solution(n, lost, reserve):
    #lost와 reserve를 오름차순으로 정렬
    lost=sorted(lost)
    reserve=sorted(reserve)
    answer=0
    
    # 여벌을 가진 학생이 도난을 당했는지 확인
    for l in lost:
        if l in reserve:
            # 이 학생은 도난당한 학생들에게 옷을 빌려줄수 없다.
            reserve.remove(l)
            
            # 자기자신은 체육복이 있으므로
            lost.remove(l)
            
    answer=n-len(lost)
    # 여벌을 갖지 않는 학생
    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
            answer+=1
            
        elif l+1 in reserve:
            reserve.remove(l+1)
            answer+=1
            
    return answer
```

<hr>


# 시도2 (테스트 5, 7, 12에서 실패)
- 코드
```python
def solution(n, lost, reserve):
    #lost와 reserve를 오름차순으로 정렬
    lost=sorted(lost)
    reserve=sorted(reserve)
    
    #빌려줄 수 있는 학생
    is_reserve=[0]*(n+1)
    for r in reserve:
        is_reserve[r]=1
        
    # 전체학생수-도난당한 학생수
    answer=n-len(lost)
    
    # 여벌을 가진 학생이 도난을 당했는지 확인
    for l in lost:
        if l in reserve:
            # 이 학생은 도난당한 학생들에게 옷을 빌려줄수 없다.
            is_reserve[l]=0
            # 자기자신은 체육복이 있으므로
            answer+=1

    # 여벌을 갖지 않는 학생
    for l in lost:
        # l-1이 reserve에 있고 l-1가 빌려줄수 있다면
        if (l-1 in reserve) and is_reserve[l-1]==1:
            answer+=1
            is_reserve[l-1]=0
            
        elif (l+1 in reserve) and is_reserve[l+1]==1:
            answer+=1
            is_reserve[l+1]=0

    return answer
```

<hr>

# 시도3 (테스트 11번에서 실패!)
- 레벨1도 이렇게 삽질을 하는데 ...ㅠㅠ;;
- 
- 코드
```python
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
    
    for r in reserve:
        if not(r in both):
            is_reserve[r]=1

    #도난당한 학생 : 체육복도난 + 체육수업 못들음
    #전체 lost에서 both에 해당하는 학생을 빼야함.
    # 전체 reserve에서 both에 해당하는 학생을 빼야함
    lost= lost-both
    reserve= reserve-both

    for l in lost:
        sizedown=l-1
        sizeup=l+1
        if sizedown>=1 and sizeup<=n:
            if is_reserve[sizedown]==1:
                answer+=1
                is_reserve[sizedown]=0
            
            elif is_reserve[sizeup]==1:
                answer+=1
                is_reserve[sizeup]=0

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

```
