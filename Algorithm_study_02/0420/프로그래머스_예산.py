def solution(budgets, M):
    budgets=sorted(budgets)
    left=0
    right=budgets[-1]
    
    # 상한액이 right일때의 예산요청보다 M이 더 큰 경우
    if M>= sum(budgets):
        return right
    
    while True:
        mid= int((left+right)//2)
        if left==mid or right==mid:
            break

        result=sum(map( lambda budget: budget if budget<mid else mid, budgets))
        if result==M:
            return mid
        
        elif result<M: #left ~mid-1탐색
            left=mid
            
        else:#result>M => mid+1 ~right 탐색
            right=mid
        
    return mid
