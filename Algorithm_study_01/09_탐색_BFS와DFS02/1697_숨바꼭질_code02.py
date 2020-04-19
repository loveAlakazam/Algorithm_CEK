import sys
class Find:
    def __init__(self):
        self.visited=200001*[False] #0~200000
        self.q=[]
        
    def bfs(self, start, cnt, target):
        self.q.append( (start, cnt))
        while self.q:
            now ,cnt= self.q.pop(0)
            if (now>=0 and now<100001) and (self.visited[now] is False):
                self.visited[now]=True                  
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
    if N>=K:
        print(N-K)
    else:
        print(f.bfs(start=N,cnt=0,target=K))

if __name__=='__main__':
    main()
