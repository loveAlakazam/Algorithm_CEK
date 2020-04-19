import sys
input= sys.stdin.readline

def sol():
    N,M=map(int, input().split())
    pm_num={}
    pm_name=[]
    for n in range(N):
        name=input().rstrip()
        pm_name.append(name)
        pm_num[name]=n+1

    for _ in range(0,M):
        m=input().rstrip()
        if m.isdigit():# m(number) -> pokemon name
            print(pm_name[int(m)-1])
        else: #m(pokemon name) -> number
            print(pm_num[m])   

if __name__=='__main__':
    sol()
