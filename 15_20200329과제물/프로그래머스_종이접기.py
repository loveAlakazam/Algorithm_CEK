def solution(n):
    answer=[0]
    for i in range(n-1):
        answer=answer+[0]+[bit^1 for bit in answer[::-1]]
    return answer
