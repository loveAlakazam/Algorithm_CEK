import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N=int(input()) #지원자 수
    score=[]
    
    #각지원자의 서류성적/ 면접 성적 순위
    for i in range(N):
        score.append([*map(int, input().split())])
    
    #x[0]을 기준으로 오름차순정렬
    score=sorted(score, key=lambda x: x[0])
    min_speech=score[0][1]
    result=1
    
    for i in range(1,N):
        flag=True
        #면접
        if min_speech>score[i][1]:
            min_speech=score[i][1]
        else:
            flag=False
            
        #flag가 True이면 채용이됨.
        if flag:
            result+=1
    print(result)     
