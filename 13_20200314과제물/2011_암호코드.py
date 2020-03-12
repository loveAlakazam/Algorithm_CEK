import sys
input=sys.stdin.readline

MAX=5000
DP=[0]*MAX
PW=[0]*MAX
DIVIDER=10**6

# password=25
# dp[1]=1 (2=>'B')
# dp[2]=2
## (과거문자그대로+현재알파벳 문자 그대로 붙일 때, 2+5=>BE)
## (과거문자+현재문자=> 새로운문자, 25=>Y)

# password=100
# dp[1]=1(1=>'A')
# dp[2]= (현재 숫자가0이면 앞의숫자가 1,2만 가능하다. 10 => 'J')
def solution(LEN):
    global PW,DP

    #현재 암호의 길이가 존재하지 않을 때
    #첫번째 비밀번호가 0일때
    if PW[1]==0 or LEN==0:
        return 0
    
    #첫번째 암호 숫자가 0이 아니라면
    #해석되는 암호개수는 dp[1]=1개이다.
    DP[0]=1
    for i in range(1, LEN+1):
        #현재 숫자가 1~9인가?
        if 1<=PW[i]<=9:
            DP[i]=(DP[i]+DP[i-1])%DIVIDER
        
        tmp=(PW[i-1]*10)+PW[i]
        if 10<=tmp<=26:
            DP[i]=(DP[i]+DP[i-2])%DIVIDER
        
    answer=DP[len(PASSWORD)]
    return answer

def main():
    global PW, DP
    PASSWORD=input().strip()

    #비밀번호 배열에 넣는다.
    for i in range(1, len(PASSWORD)+1):
        PW[i]=int(PASSWORD[i-1])
        
    result=solution(len(PASSWORD))
    print(result)
    
if __name__=='__main__':
    main()
