# -*- coding: utf-8 -*-
#9935.문자열폭발 (시간초과)
#replace를 사용하면 O(s)의 복잡도가 생기므로 시간 초과
import sys
import re
def main():
    s=sys.stdin.readline().strip() #문자열
    e=sys.stdin.readline().strip() #폭발문자열(같은문자2개이상 포함x)
    while e in s:
        s=re.sub(e,'',s)
        
    if not s:
        print('FRULA')
    else:
        print(s)
        
if __name__=='__main__':
    main()
