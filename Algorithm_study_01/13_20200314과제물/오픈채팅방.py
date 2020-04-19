def solution(record):
    states=[]
    member=dict() #key:id, value:nick-name
    for r in record:
        info=r.split()
        states.append(info[:2])

        if info[0]=='Leave':
            member[info[1]]
        else:#enter & change
            member[info[1]]=info[2]
    
    answer=[]
    for s in states:
        if s[0]=='Enter':
            answer.append('{}님이 들어왔습니다.'.format(member[s[1]]))
        elif s[0]=='Leave':
            answer.append('{}님이 나갔습니다.'.format(member[s[1]]))
    return answer
