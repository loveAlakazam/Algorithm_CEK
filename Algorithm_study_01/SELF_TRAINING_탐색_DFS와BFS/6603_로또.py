# -*- coding: utf-8 -*-
import sys
#from itertools import combinations
def dfs(start, depth):
    if depth==6:
        print(' '.join(case[:6]))

    for i in range(start,k):
        case[depth]=S[i]
        dfs(i+1, depth+1)
        

def main():
    while True:
        global S,k, case
        case=[0]*13
        S=list(sys.stdin.readline().split())
        if S[0]=='0':
            break
        k=int(S.pop(0))
        if (k>6) and (k<13):
            dfs(0,0)
            print()
##def main():
##    while True:
##        S=list(sys.stdin.readline().split())
##        if S[0]=='0':
##            break
##        k=int(S.pop(0))
##        if (k>6 and k<13):
##            result=combinations(S,6)
##            for r in result:
##                print(' '.join(r))
##        print()
            
if __name__=='__main__':
    main()
