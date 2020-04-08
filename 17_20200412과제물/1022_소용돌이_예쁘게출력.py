import sys
input=sys.stdin.readline

def getValue(r,c):
    n=max(abs(r), abs(c))
    last= 2*n+1
    last= last**2

    if r==n:#아래 변
        return last-(n-c)
    elif c==-n:#왼쪽 변
        return last-(2*n)-(n-r)
    elif r==-n:#윗 변
        return last-(4*n)-(n+c)
    else: #오른쪽 변
        return last-(6*n)-(n+r)

#자리수 계산
def getDigit(val):
    return len(str(val))

r1, c1, r2, c2=map(int, input().strip().split())

max_len=0
for y in range(r1, r2+1):
    for x in range(c1, c2+1):
        max_len=max( max_len, getDigit(getValue(y,x)) )

output=[]
for y in range(r1, r2+1):
    for x in range(c1, c2+1):
        output.append(f'{getValue(y,x): >{max_len}} ')
    output.append('\n')
        
#소용돌이 출력
sys.stdout.write(''.join(output))
