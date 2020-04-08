import sys
input=sys.stdin.readline

def isAllVisited(visited):
    global ROW, COL
    for y in range(ROW):
        for x in range(COL):
            if not visited[y][x]:
                return False
    return True

def isRange(y,x):
    global ROW, COL
    if (y>=0 and y<ROW) and (x>=0 and x<COL):
        return True
    return False

r1, c1, r2, c2=map(int, input().strip().split())
ROW, COL=r2-r1+1, c2-c1+1

#소용돌이 입력

Round=1 ## 오른쪽/위/왼쪽 : 2*바퀴수-1  , 아래: 2*바퀴수-2
longest_num_len=0

cury, curx= ROW-1-r2, COL-1-c2 #소용돌이 시작위치
last_y, last_x = cury, curx #마지막 위치(배열에 입력한 마지막위치)

visited=[[False]*COL for _ in range(ROW)]
MAP=[ [0]*COL for _ in range(ROW)]

MAP[cury][curx]=1
visited[cury][curx]=True
now=2

while True:
    # visited가 모두 다 채워졌는가?
    if isAllVisited(visited):
        longest_num_len=len(str(MAP[last_y][last_x]))
        break

    #아래방향으로 이동
    for i in range(0,Round*2-2):
        cury=cury+1
        if isRange(cury, curx):
            MAP[cury][curx]=now
            visited[cury][curx]=True
            last_y, last_x= cury, curx
        now+=1
        
    #오른쪽으로 이동
    for i in range(0,Round*2-1):
        curx=curx+1
        if isRange(cury, curx):
            MAP[cury][curx]=now
            visited[cury][curx]=True
            last_y, last_x= cury, curx
        now+=1
               
    #위로 이동
    for i in range(0,Round*2-1):
        cury=cury-1
        if isRange(cury, curx):
            MAP[cury][curx]=now
            visited[cury][curx]=True
            last_y, last_x= cury, curx
        now+=1
        
    #왼쪽으로 이동
    for i in range(Round*2):
        curx=curx-1
        if isRange(cury, curx):
            MAP[cury][curx]=now
            visited[cury][curx]=True
            last_y, last_x= cury, curx
        now+=1

    #다음라운드로 왼쪽으로 이동
    Round+=1


#배열의 숫자의 길이에 따라서 다르게 나타내기
for y in range(ROW):
    for x in range(COL):
        now_len=len(str(MAP[y][x]))
        MAP[y][x]=' '*(longest_num_len - now_len)+str(MAP[y][x])

#소용돌이 출력
for y in range(ROW):
    print(' '.join(MAP[y]))
