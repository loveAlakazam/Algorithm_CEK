# 시도1 (실패: 틀렸습니다 6%)
-예시1 맞음<br>
1 4<br>
3 5<br>
0 6<br>
5 7<br>
3 8<br>
5 9<br>
6 10<br>
8 11<br>
8 12<br>
2 13<br>
12 14<br>
답: 4<br>

-예시2 맞음<br>
8 8<br>
5 8<br>
3 4<br>
2 5<br>
2 7<br>
8 8<br>
1 10<br>
3 3<br>
10 10<br>
답: 6<br>

- 반례<br>
1 3 <br>
1 2 <br>
답: 1, 나: 2<br>

- 코드
```python

# -*- coding: utf-8 -*-
# 1931. 회의실 배정
import sys

def solution(times,start, end):    
    for i in range(start+1, end):
        # 이전 회의의 end타임이 현재회의의 start라면..
        # 이전회의끝나고 바로 시작할 수 있으므로.
        # 시작과 끝 중간에 times[start+1]~ times[end-1]
        # 하나라도 1이 있다면 회의가 겹치므로 False를 리턴
        if times[i]==1:
            return False
    return True

def main():
    N= int(sys.stdin.readline())
    starts=[]
    ends=[]
    result=0
    
    for _ in range(N):
        #시작시간: start
        #끝나는 시간: end
        start, end= map(int, sys.stdin.readline().split())
        starts.append(start)
        ends.append(end)

    # ends에서 가장 큰값을 찾는다.
    # times의 길이는 0부터 max(ends) 까지,  ends+1로 한다.
    length= max(ends)+1
    times=[0]*length
    
    for start, end in zip(starts, ends):
        # 현재하는 회의가 이전에 했던 회의와 겹치는지 확인
        ans= solution(times, start, end)
        if ans is True:
            result+=1
            for i in range(start, end+1):
                times[i]=1
    print(result)

```
