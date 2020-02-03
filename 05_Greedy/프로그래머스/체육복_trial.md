# 시도1 (테스트 1, 6, 7 에서 실패)
-코드
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
