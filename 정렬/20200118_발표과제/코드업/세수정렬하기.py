# code-up 1172: 세수정렬하기
import sys
input= sys.stdin.readline

def solution():
    arr= map(int,input().split())
    result= ' '.join(str(r) for r in sorted(arr))
    #result= sorted(arr).join(' ')
    print(result)
    
if __name__=='__main__':
    solution()
