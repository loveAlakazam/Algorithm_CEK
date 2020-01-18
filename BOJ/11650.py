import sys
input = sys.stdin.readline

def solution():
    N= int(input()) #점의개수
    points=[]
    for _ in range(N):
        # x,y 좌표 입력
        x,y= map(int, input().split())
        points.append((x,y))

    #print(points) #N개의 점 정렬
    points=sorted(points)
    for x, y in points:
        print(x,y)

if __name__=='__main__':
    solution()
