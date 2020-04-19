# -*- coding: utf-8 -*-
import sys
input= sys.stdin.readline

def find_red_wh(red):
    r_widths=[]
    r_heights=[]
    for x in range(red, 0, -1):
        if red%x==0: #x는 red에 나누어떨어지는가?
            y=red//x
            if x>=y: #너비가 높이보다 길거나 같은가?
                r_widths.append(x)
                r_heights.append(y)
    return r_widths , r_heights

def solution(brown, red):
    answer = []
    #너비가 red가 나올수 있는 x,y값 집합
    #단, x가 y보다 길다.
    r_widths, r_heights= find_red_wh(red)
    for rw, rh in zip(r_widths, r_heights):
        width=rw
        height=rh
        now_cnt= 0
        while now_cnt<brown:
            now_cnt+=2*(width+height)+4
            width+=2
            height+=2            
        if now_cnt==brown:
            answer.extend((width,height))
    return answer

########## 여기부분은 생략####################
def main():
    test_case= int(input())
    for _ in range(test_case):
        brown,red=map(int, input().split())
        ans=solution(brown, red)
        print(ans)
    
if __name__=='__main__':
    main()
    
