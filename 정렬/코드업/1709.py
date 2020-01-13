import io, sys
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
input=sys.stdin.readline
def solution():
    N=int(input())
    M=list(map(int, input().split()))
    print(' '.join(str(x) for x in sorted(M,reverse=True)))
    
if __name__=='__main__':
    solution()
