import sys
input=sys.stdin.readline

#input_str이 올바른 괄호일때-> 변환값
def get_val(input_str):
    left_cover=[]
    pair={')':'(', ']':'['}
    result=0
    last_left=-1
    for s in input_str:
        #left_cover의 맨앞값이 숫자인가?
        if len(left_cover)==1:
            if left_cover[-1]!='(' and left_cover[-1]!='[':
                result+=left_cover.pop()
                last_left=-1
            
        #왼쪽괄호
        if s=='(' or s=='[':
            left_cover.append(s)
            last_left+=1

        #오른쪽괄호
        elif s==')' or s==']':
            val=1
            flag=False
            while left_cover[last_left]!=pair[s]:
                if not flag:
                    val*=left_cover.pop()
                    flag=True
                else:
                    val+=left_cover.pop()
                last_left-=1
                
            left_cover.pop()
            if s==')':
                val*=2
            else:#s==']'
                val*=3

            left_cover.append(val)
    return result
                
def isRight(input_str):
    result=0
    left_cover=[]
    
    for s in input_str:
        #s가 왼쪽 괄호인가?
        if s =='(' or s=='[':
            result+=1
            left_cover.append(s)
            
        #s가 오른쪽 괄호라면
        elif s==')' or s==']':
            #left_cover에 아무것도 없다면:
            if not left_cover:
                return False

            #s가 ')'이고, left_cover의 마지막값이 '(' 이라면?
            #s가 ']'이고, left_cover의 마지막값이 '['이라면?
            if (s==')' and left_cover[-1]=='(') or (s==']' and left_cover[-1]=='['):
                result-=1
                left_cover.pop()
                
            else:
                return False

    #result가 0이 아니라면?
    if result!=0 and not left_cover:
        return False
    return True
            

def main(input_str):
    #올바른 괄호인지 확인
    if isRight(input_str) and 1<=len(input_str)<=30:
        return get_val(input_str) #괄호열값을 나타낸 정수를 리턴
        
    #올바른 괄호가 아니라면
    return 0

if __name__=='__main__':
    input_str=input().strip()
    print(len(input_str))
    print(main(input_str))
