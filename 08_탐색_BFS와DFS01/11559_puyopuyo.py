# -*- coding: utf-8 -*-
import sys
from collections import deque
global puyo
global d

def main():
    #4개이상 뿌요가 터지는 횟수
    result=BFS()
    print(result)

# 현재뿌요의 위/아래/왼쪽/오른쪽 뿌요가 적절한 위치에 있는지 확인
def isRange(nextY, nextX):
    if nextY<0 or nextY>=12 or nextX<0 or nextX>=6 :
        return False
    return True

def BFS():
    #초기 뿌요콤보 개수
    result=0  
    while True:
        #뿌요 콤보가 더이상 발생하지 않는다면 True로하여
        #무한루프를 벗어난다.
        finished=True
        q=deque() #연결된 뿌요의 위치를 저장하는 큐
        rm_puyo=[] #연결된뿌요가 4개이상일때 없애버릴 뿌요위치를 저장
        
        for r in range(11,-1,-1):
            for c in range(6):
                if puyo[r][c]=='.':
                    continue
                else:
                    #각 뿌요마다 연결된 상/하/좌/우 연결뿌요 확인
                    #뿌요하나하나에서 방문리스트를 새로 갱신.
                    visited=[[False]*6 for _ in range(12)]  #방문리스트
                    
                    cnt=0 #현재 뿌요와 연결된 뿌요개수
                    color=puyo[r][c]#현재뿌요의 컬러
                    q.append((r,c))#현재뿌요의 위치
                    visited[r][c]=True #현재뿌요를 방문함
                    
                    #만일 큐가 비어있지 않는다면
                    while q:
                        curY, curX= q.popleft() #큐의 맨앞을 pop하여 위치를 구한다
                        cnt+=1 #뿌요 카운트
                        
                        #만일 4개이상 연결된뿌요가 생기는 것을 대비하여
                        #지워야할 연결된 뿌요의 위치를 임시로 저장한다.
                        rm_puyo.append((curY,curX))
                        
                        #curY행 curX열의 뿌요위치와
                        #주변뿌요:그 뿌요의 상/하/좌/우에 있는 뿌요
                        #주변뿌요가 서로 연결되어있는지 확인
                        #그리고 그 주변뿌요가 방문을 하지 않은 뿌요여야함.
                        for dy, dx in d:
                            nextY, nextX= curY+dy, curX+dx

                            # 01. 주변뿌요가 0~11행, 0~5열 위치인지 확인
                            # 02. 현재뿌요와 같은 값인지 확인
                            if isRange(nextY,nextX) and (color==puyo[nextY][nextX]):
                                #03. 주변뿌요가 방문하지 않은 상태인지 확인
                                if visited[nextY][nextX] is False:
                                    visited[nextY][nextX]=True #그 주변뿌요를 방문하고
                                    q.append((nextY,nextX)) # 큐에 추가한다.
            
                    #연결된뿌요개수(cnt)가 4개이상이면
                    #그 뿌요들을 '.'으로 바꾼다.
                    if cnt>=4:
                        for y,x in rm_puyo:
                            puyo[y][x]='.'                       
                        finished=False #콤보가 일어났으므로 아직 끝내지 않는다.
                        
                    #연결된뿌요가 4개이상이든, 미만이든.. 상관없이
                    #연결된뿌요(빈공간으로 바꿔야할 뿌요위치 저장원소)들을 없애버린다.
                    rm_puyo=[]
                    
        if finished:
            return result #result값을 리턴한다.
        #콤보카운트 (4개이상의 연결된 뿌요그룹이 2개이상이어도 1콤보로한다.)
        result+=1
        #뿌요를 내린다. '.'위에 있는 뿌요들을 아래로 내린다.
        puyo_down()

# 연결된 뿌요를 없앤 후
# 뿌요밑에 빈공간이 있으면 안되므로
def puyo_down():
    for r in range(11,-1,-1):
        for c in range(6):
            if puyo[r][c]=='.':
                continue
            
            else:
                now_row= r #현재의 뿌요 행위치
                mark=puyo[r][c] #현재 뿌요 값
                puyo[r][c]='.'
                while True:
                    #(now_row+1)행에 있는 뿌요가 0~11행 사이인지 확인 후
                    #(now_row+1)행에있는 뿌요가 '.'이 아니라면
                    #while loop을 벗어난다. 
                    if not isRange(now_row+1, c) or puyo[now_row+1][c]!='.':
                        break
                    now_row+=1
                #빠져나올때 now_row에 위치한 뿌요는 mark가된다.
                #즉.. 빈공간을 모두 내린후를 나타냈다.
                puyo[now_row][c]=mark
                    
if __name__=='__main__':
    #d[0]=현재뿌요위치 아래
    #d[1]=현재뿌요위치 위
    #d[2]=현재뿌요위치 왼쪽
    #d[3]=현재뿌요위치 오른쪽
    d=[ (0,-1), (0,1), (-1,0), (1,0)]

    # 배열 입력 ( puyo를 전역변수로 한다. )
    puyo=[  list(sys.stdin.readline().strip()) for _ in range(12)]
    main()
