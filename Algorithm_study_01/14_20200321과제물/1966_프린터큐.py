import sys
input=sys.stdin.readline

def find_bigger(now, que):
    for e in que:
        if e[1]>now:
            return True
    return False

def solution(N,M,nums):
        #N: 문서개수
        #M: 몇번째로 인쇄됐는지 궁금한 문서 번호
        if N==1: #문서개수가 1개인경우
            return 1
            
        else:
            #중요도 idx는 1~9이다.
            que=[(idx, val) for idx, val in enumerate(nums)]        
            printer=[]
            while len(que)>0:
                now=que.pop(0)
                #now[1]보다 큰 값이 que에 존재한다면-> 맨앞값을 큐에넣는다.
                if find_bigger(now[1], que):
                    que.append(now)
                else:#now[1]보다 큰값이 존재하지 않으면 -> 맨앞값을 프린터에 넣는다.
                    printer.append(now)
     
            for idx,p in enumerate(printer):
                if p[0]==M:
                    return idx+1
                    

def main():
    T=int(input()) #테스트케이스 개수
    for _ in range(T):
        N, M=map(int, input().strip().split())
        nums=[*map(int, input().strip().split())]
        print(solution(N,M,nums))

if __name__=='__main__':
    main()
                
