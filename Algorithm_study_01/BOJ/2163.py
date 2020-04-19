import sys
input = sys.stdin.readline
# 참고: https://seonkyu.tistory.com/9

def solution():
    N,M= map(int,input().split())
    # N-1번을 자르고 -> N개의 도막이 생김
    # 1개의 도막에서 M-1번 자름
    print((N-1)+N*(M-1))

if __name__=='__main__':
    solution()
