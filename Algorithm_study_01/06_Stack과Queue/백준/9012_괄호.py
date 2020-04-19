import sys
def isVPS(ex):
    stack=[]
    #))((가 yes가 되는경우를 막기위해서..
    #ex의 맨 마지막 원소가 ( 라면.. 'NO'이다.
    if ex[-1]=='(':
        return 'NO'
    
    while len(ex)>0:
        # stack이 비어있다면
        # ex의 맨위의 원소(ex[-1])을 넣는다.
        if len(stack)==0:
            # ex[-1]이 ')'라면..
            if ex[-1]==')':
                stack.append(ex.pop())
            #ex[-1]이 '('이라면.. 더이상 못함..
            else:
                return 'NO'
            
        # stack이 비어있지 않다면
        else:
            #stack의 맨 위의 원소(stack[-1])와
            #ex의 맨위의 원소(ex[-1])이 서로 같다면?
            # -> ex를 pop하여 stack에 넣는다.
            if ex[-1]==stack[-1]:
                stack.append(ex.pop())
                
            # 서로다르다면
            # ex와 stack의 맨위의 원소를 버린다.
            else:
                stack.pop()
                ex.pop()

    #stack에 남는가?
    print('stack: ', stack)
    print('ex: ', ex)
    if len(stack)==0:
        return 'YES'
    else:
        return 'NO'
            
def main():
    N=int(sys.stdin.readline())
    for _ in range(N):
        ex=list(sys.stdin.readline().strip())
        print(isVPS(ex))

if __name__=='__main__':
    main()
