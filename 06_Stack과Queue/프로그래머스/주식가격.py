def solution(prices):
    answer=len(prices)*[0]
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            answer[i]+=1
            if prices[i]<=prices[j]:
                break
    return answer
