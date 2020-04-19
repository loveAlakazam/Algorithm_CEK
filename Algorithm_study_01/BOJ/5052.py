# -*- coding: utf-8 -*-
# BOJ 5052
# 롯데정보통신 코딩테스트 2번인가 3번에 나옴.
import sys
input=sys.stdin.readline

def find_duplicate(nums):
    #숫자값크기에따라 정렬하고
    #target과 target바로 뒤의 숫자(바로앞 문자열 길이)를
    # 문자열비교하여 있는지 확인
    for idx, target in enumerate(nums[:-1]):
        target_next= nums[idx+1]
        #target뒤에 있는 전화번호가 target보다 짧은경우를 대비..
        target_len= len(target) if len(target)<len(target_next) else len(target_next)
        if target[:target_len]==target_next[:target_len]:
            return 'NO'
    return 'YES'        

def solution():
    # T: 테스트 케이스 개수
    T= int(input())
    
    for t in range(T):
        # n: 전화번호 개수
        n= int(input())
        
        nums=[]
        #n 개의 전화번호를 저장
        for _ in range(n):
            nums.append(input().strip())
                   
        #문자열 정렬
        nums=sorted(nums)
        print(find_duplicate(nums))

if __name__=='__main__':
    solution()
