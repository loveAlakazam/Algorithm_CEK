# 시도1 (실패: 틀렸습니다 6%)

- 예시1 맞음<br>
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

- 예시2 맞음<br>
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

<hr>

# 시도2 (실패: 틀렸습니다 0%)
- 반례: left_last<=i<=right_start일때 times[i]=0인 데이터가 존재한다면?
- 코드
```python
# -*- coding: utf-8 -*-
# 1931. 회의실 배정
import sys

def is_available(times, start, end):
    for i in range(start, end):
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

    # 가능한 회의 시간 범위를 나타냄
    # 0~left_last
    # right_start~max(ends)
    # left_last, right_start 초기화
    left_last=length
    right_start=-1
    for start, end in zip(starts, ends):
        # 현재하는 회의가 이전에 했던 회의와 겹치는지 확인
        if (start<=left_last and end<=left_last) or (start>=right_start and end>=right_start):
            ans=is_available(times, start, end)
            if ans is True:
                print(start,end)
                
                left_last=min(left_last, start)
                right_start=max(right_start, end)
                print('left_last: ',left_last, '  right_start: ',right_start)
                result+=1
                for i in range(start, end+1):
                    times[i]=1
    print(result)

if __name__=='__main__':
    main()

```

<hr>

# 시도3 (실패: 틀렸습니다 80%에서...ㅠㅠ)
- 이유: 회의가 끝나는 시간이 서로 같을때 회의시간이 가장 작은값을 우선으로 한다.
- 참고 블로그가 c++로 되어있어서.. 사용자가 만든 함수로 정렬시켰다.
- 그런데 파이썬의 경우에는 사용자 정의함수로 sorted를 적용시킬 수가 없다. -> 왜냐면 에러가 뜬다..
- 직접 정렬을 해야될거 같다는 생각이 들었다.
- 코드
```python
# -*- coding: utf-8 -*-
# 1931. 회의실 배정
# 참고url: https://kim6394.tistory.com/67
import sys
   
def main():
    points=[]
    N= int(sys.stdin.readline())
    for n in range(N):
        points.append(tuple(map(int,sys.stdin.readline().split())))

    #회의끝나는 시간을 기준으로 오름차순 정렬    
    print(points)
    points=sorted(points, key=lambda x:x[1])
    print(points)

    result=0
    last=0
    for idx, p in enumerate(points):
        s,e= map(int, p)
        if idx==0:
            last=e
        else:
            if last<=s:
                last=e
                result+=1
                
    print(result+1)#맨처음 회의시간 덧셈고려.         

if __name__=='__main__':
    main()

```
