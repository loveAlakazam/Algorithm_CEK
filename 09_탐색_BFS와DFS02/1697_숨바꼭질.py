import sys
class Find:
    def __init__(self):
        self.visited=200001*[False] #0~200000
        self.q=[]
        
    def bfs(self, start, cnt, target):
        if start>=target:
            return start-target
        
        self.q.append( (start, cnt))
        while self.q:
            now ,cnt= self.q.pop(0)
            
            #현위치가 0보다 크거나 같고, 100001보다 작은가?
            if (now>=0) and (now<100001):
                #현위치 now가 아직 방문안되어있는가?
                if self.visited[now] is False:
                    self.visited[now]=True #현위치 now 방문
                    
                    #현위치가 target(K)인가?
                    if now==target:
                        return cnt
                
                    if now>0:
                        self.q.append((now-1, cnt+1)) #걷기
                    self.q.append((now+1, cnt+1)) #걷기
                    self.q.append((now*2, cnt+1)) #순간이동
        return cnt
        
def main():
    f=Find() #객체 생성
    N,K= map(int, sys.stdin.readline().split())
    print(f.bfs(start=N,cnt=0,target=K))

if __name__=='__main__':
    main()
