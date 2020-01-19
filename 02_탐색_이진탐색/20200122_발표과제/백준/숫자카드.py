import sys
input = sys.stdin.readline

def solution():
    # 상근이가 가지고 있는 숫자카드 개수
    N= int(input())
    # 숫자카드
    cards=list(map(int, input().split()))
    cards.sort() #오름차순 정렬

    M=int(input())
    #구해야할 M개의 정수
    finds=list(map(int, input().split()))

    #상근이가 가지고 있는지 , 아닌지를 구해야함.
    for f in finds:
        left, right=0,N-1
        while(left<=right):
            mid=(left+right)//2
            if f==cards[mid]:
                print(1)
                break
            elif f>cards[mid]:
                left=mid+1
            elif f<cards[mid]:
                right=mid-1
        if(cards[mid]!=f):
            print(0)

if __name__=='__main__':
    solution()
