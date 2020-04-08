import sys
input=sys.stdin.readline

def solution(genres, plays):
    G={}
    PSUM={}
    for idx, (g,p) in enumerate(zip(genres, plays)):
        #장르별 재생횟수 구하기
        if g not in PSUM:
            PSUM[g]=0
        PSUM[g]+=p
        
        #장르에 있는 노래 (재생횟수, 고유번호) 정보 넣기
        if g not in G:
            G[g]=[]
        G[g].append((p,idx)) #(재생횟수, 고유번호)
    
    #먼저 PSUM을 내림차순 정렬 :정렬기준(장르별 재생횟수)
    PSUM=sorted(PSUM.items() , key=lambda x: -x[1])
    
    answer = []
    total_cnt=2*len(PSUM) #최대 len(PSUM)*2번
    for psum in PSUM:
        if total_cnt==0:
            return answer
        
        g=psum[0] #g: 장르
        cnt=2
        while total_cnt>0 and cnt>0 and len(G[g])>0:
            G[g]=sorted(G[g], key=lambda x: (x[0], -x[1]))
            _, idx= G[g].pop()
            answer.append(idx)
            cnt-=1
            total_cnt-=1
            
    return answer        

def main():
    genres=input().strip().split()
    plays=[* map(int, input().strip().split())]
    print(solution(genres, plays))

if __name__=='__main__':
    main()
