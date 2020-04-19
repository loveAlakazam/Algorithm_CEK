# 단어 수학 재도전 -> greedy를 이용해서 풀이
import sys
input = sys.stdin.readline

N= int(input())
words=[ input().strip() for _ in range(N)]

#문자열 길이대로 정렬
words=sorted(words)

alpha=[0]*26
for word in words:
    for idx, w in enumerate(word):
        alpha[ord(w)-ord('A')]+=10**(len(word)-1-idx)

#alpha를 내림차순으로 정렬한다.
alpha=sorted(alpha, reverse=True)

ans=0
for i in range(9,0,-1):
    ans= ans+ (i * alpha[9-i])
print(ans)
