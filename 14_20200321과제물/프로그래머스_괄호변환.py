def recursion(p):
    #p가 비어있있는 문자열이라면
    if len(p)==0:
        return p

    #p를 균형잡힌 두 문자열로 분리한다.
    num=0
    for i in range(len(p)):
        if p[i]=='(':
            num+=1
        else:
            num-=1

        if num==0:
            u=p[:i+1]
            v=p[i+1:]
            break
        
    #u가 올바른 문자열이라면
    if isCorrect(u):
        return u+recursion(v)
    
    #u가 올바른 문자열이 아니라면
    #4-1. 비어있는 문자열에 ( 를 붙인다.
    #4-2. 문자열 v에 대해 1단계로부터 재귀적 수행한 결과 문자열을 이어붙인다.
    #4-3. )을 다시 붙인다.
    tmp='('+recursion(v)+')'
    
    #4-4. u의 첫번째와 마지막 문자를 제거하고 나머지 문자열의 괄호방향을 뒤집어서 뒤에 붙인다.
    #길이가 2보다 크다면
    if len(u)>2:
        for i in range(1,len(u)-1):
            if u[i]=='(':
                tmp+=')'
            else:
                tmp+='('
        
    return tmp

#올바른 괄호문자인지 확인해주는 함수이다.
#빈문자열도 올바른 괄호문자열로 체크된다.
def isCorrect(input_str):
    left_cover=[]
    for i in input_str:
        if i=='(':
            left_cover.append(i)
        else:#i==')'
            if len(left_cover)==0:
                return False
            left_cover.pop()
    if len(left_cover)>0:
        return False
    return True
            
            
def solution(p):
    #p는 올바른 문자열이다.
    if isCorrect(p):
        return p
    #p는 올바른 문자열이 아니라면
    return recursion(p)

