import sys

def main():
    N=int(sys.stdin.readline())
    arr=[]
    visited=[]
    for _ in range(N):
        arr.append( list(map(int, sys.stdin.readline().split())))
        visited.append( [0]*N)
    print(arr)
    print(visited)
    #방문한 노드
    order=[]
    order.append((0,0)) #원점 시작
    # 현재 좌표가 N-1보다 작거나 같은가?
    while order[0][0]<N-1 or order[0][1]<N-1:
        r, c=order.pop(0) #맨앞의 점을 pop한다
        visited[r][c]+=1
        tmp=arr[r][c]
        go_right= c+tmp
        go_down= r+tmp
        if go_right<N:
            order.append((r, go_right))
        if go_down<N:
            order.append((go_down, c))
        print(order)
    print(visited[N-1][N-1])
        
if __name__=='__main__':
    main()
