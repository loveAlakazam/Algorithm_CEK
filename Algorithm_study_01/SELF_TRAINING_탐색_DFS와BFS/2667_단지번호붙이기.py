# -*- coding: utf-8 -*-
import sys

class Maps:
    def __init__(self, N):
        self.N= N
        self.maps=[] #지도(0과 1로 이루어져있다)
        self.visited=[[False]*self.N for _ in range(self.N)] #방문리스트

        self.group_cnt=0 #'1'로 구성된 그룹의 개수
        self.result=[] #그룹당 '1'로된 셀 개수를 나타낸 리스트
        self.directions= [(-1,0), (1,0), (0,-1), (0,1)] #현위치의 상/하/좌/우 를 나타낸다.
        

    #현재위치가 N행N열 배열 안에 있는 원소인지 확인
    def isRange(self, y,x): 
        if (y<0 or y>=self.N) or (x<0 or x>=self.N):
            return False
        return True

    #깊이 탐색
    def dfs(self, y,x, cnt):
        #print('now: self.maps[{}][{}]={}'.format(y,x,self.maps[y][x]))
        #현재노드가 방문안한 상태라면
        if self.visited[y][x] is False:
            self.visited[y][x]=True #현재노드 방문한다
        
            #현재노드의 상하좌우 노드를 탐색한다
            for dy, dx in self.directions:
                nexty=dy+y
                nextx=dx+x
                
                #근처 노드가 적절한 N*N 배열의 원소에 해당하는가?
                if self.isRange(nexty, nextx):
                    #근처노드가 방문하지 않은 상태이고
                    #'0'이 아닌 '1'이라면.
                    if (self.visited[nexty][nextx] is False) and (self.maps[nexty][nextx]!='0'):
                        #근처노드 1개 카운트하고, 재탐색..
                        cnt= 1+self.dfs(nexty, nextx, cnt)
        return cnt
        
        
        
def main():
    N= int(sys.stdin.readline()) #행/열 입력
    m= Maps(N) #객체 생성

    #지도그리기
    for _ in range(N):
        tmp= sys.stdin.readline().strip() #문자열 1111-> ['1','1','1','1']로 분리
        m.maps.append(tmp)
    
    #깊이 탐색
    for y in range(N):
        for x in range(N):
            if m.maps[y][x]=='0':
                continue
            else:
                #방문했는지 확인
                if m.visited[y][x] is False:
                    m.group_cnt+=1 #그룹카운트 +1
                    #print('\n현재 그룹카운트: ', m.group_cnt)
                    cnt=m.dfs(y=y, x=x, cnt=1) #dfs탐색을하여 현재 그룹에 속한 '1'개수 리턴받는다.
                    #print('개수: ', cnt,'\n')
                    m.result.append(cnt) #m.result에 추가
                    
    #결과 출력
    print(m.group_cnt)
    
    #각 그룹의 '1'원소의개수 출력
    #오름차순으로 정렬
    m.result=sorted(m.result)
    for e in m.result:
        print(e)

if __name__=='__main__':
    main()
