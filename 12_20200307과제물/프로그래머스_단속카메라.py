def solution(routes):
    # 1. 도착점이 작은 것을 기준으로 정렬
    #    도착점이 같을때 시작점이 작은 것을 우선으로 한다.
    routes= sorted(routes, key=lambda x: (x[1], x[0]))
    
    # 2. 정렬후 첫번째 차량의 도착점을 카메라 위치로 초기화한다.
    # (1) "시작점<= 카메라 위치 <= 도착점" 조건이 만족한지 확인한다. -> 카운트하지 않고 카메라 위치 그대로
    # (2) (1)의 조건이 만족하지 않으면 현재차량의 도착점을 카메라 위치로한다. (필요 카메라 대수 카운트)
    answer = 0
    camera=0 #초기화
    for i, car in enumerate(routes):
        start, end= car
        if i==0:
            answer+=1
            camera=end
        else:
            if not start<=camera<=end:
                answer+=1
                camera=end
            
    return answer
