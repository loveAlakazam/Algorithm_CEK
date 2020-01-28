# -*- coding: utf-8 -*-
import sys
input=sys.stdin.readline

def main():
    #N: 포켓몬 개수
    #M: 다솜이가 풀어야할 문제 개수
    N,M =map(int,input().split())
    poke_nums={}#키값: 포켓몬이름, value값: 포켓몬 도감번호
    poke_names=[] #포켓몬 이름
    
    for i in range(N):
        name=input().strip()
        poke_nums[name]=i+1
        poke_names.append(name)#이름등록

    for _ in range(M):
        quiz=input().strip()
        # 문제가 도감번호일때-> 포켓몬이름 출력
        if quiz.isdigit():
            print(poke_names[int(quiz)-1])
            
        #문제가 이름일때 ->도감번호 출력
        else:
            print(poke_nums[quiz])
            
if __name__=='__main__':
    main()
