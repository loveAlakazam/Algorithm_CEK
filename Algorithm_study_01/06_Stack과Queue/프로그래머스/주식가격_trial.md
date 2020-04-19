# 시도1 
- 결과: 실패 
- 정확성 테스트 모두 통과
- 효율성 테스트 모두 시간초과
- 코드
```python
def solution(prices):
    answer=[]
    while len(prices)>1:
        now=prices.pop(0)
        cnt=0
        for price in prices:
            cnt+=1
            if now>price:#가격이 떨어지는 순간
                break
        answer.append(cnt)
    answer.append(0)
    return answer


```
<hr>

# 시도2
- 결과: 성공
- 2중 for문으로 풀었습니다.
- 코드
```python
def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            answer[i]+=1
            if prices[i]>prices[j]:
                break
    return answer
```
