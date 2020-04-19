def solution(array, commands):
    answer=[]
    for i,j,k in commands:
        #array의 i(인덱스: i-1)번째수부터 j번째 숫자까지만 자른배열을 tmp라 한다.
        # 인덱스는 0부터 시작
        tmp=array[(i-1):j]
        #오름차순으로 정렬
        tmp=sorted(tmp) 
        #tmp에서 k번째숫자(인덱스:k-1)
        answer.append(tmp[k-1])
    return answer
