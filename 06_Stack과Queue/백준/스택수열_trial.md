# 시도1
- 결과: 실패
- now=1로 초기화하고
- t가 now보다 크거나 같으면 -> now부터 t까지 계속 push()
- t가 stack리스트의 마지막 원소(stack[-1])와 같다면 -> pop()
- pop()연산을 할때 나온 수를 더한뒤에 10을 곱한다.
- 그런데 마지막 pop()연산을 한 뒤에도 10을 곱하게되므로, 반복문이 종료되면 10을 나눈다.

- 코드
```python
# -*- coding: utf-8 -*-
import sys

def main():
    N=int(sys.stdin.readline())
    targets=[]
    for _ in range(N):
        targets.append(int(sys.stdin.readline()))

    # 1부터 N까지의 수열
    process=[]
    stack=[]
    result=0
    now=1
    for t in targets:
        #now가 t보다 작거나 같으면..
        if now<=t:
            # stack에 now부터 t까지의 원소들을 stack에 차례대로 넣는다.
            for i in range(now,t+1):
                stack.append(i)
                process.append('+')
                now+=1
        # stack에 맨마지막에 들어온원소가(stack[-1]) t와 같다면
        if stack[-1]==t:
            result+=stack.pop()
            process.append('-')
            result*=10 #다음에 pop해서 들어올수를 더하기위해서..
        print(now, stack, result)
        
    #pop할때마다 result에 10을 곱했으므로
    # 그런데 마지막 하나를 pop()할때도 10을 곱하게됨
    # 그래서 for문을 거친뒤에 result에 10을 나눠야함.
    result=result//10
    print(result)
    #리스트-> 문자열 -> 숫자: [1,2,3] ->['1','2','3'] ->'123'->123
    #target_number: target의 원소들을 이어붙인 숫자 [1,2,3] -> 123
    target_number=int(''.join(map(str,targets)))
    if target_number==result:
        for p in process:
            print(p)
    else:
        print('NO')
        
if __name__=='__main__':
    main()
```

<hr>

#시도2
- 코드
