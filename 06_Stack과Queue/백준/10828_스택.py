import sys
class Stack:
    #비어있는 스택
    def __init__(self):
        self.stack=[]
        self._top=-1
        
    def push(self, val):
        #val을 stack에 넣는다.
        self.stack.append(val)
        self._top+=1
        
    # 맨위에 있는 정수를 출력
    def top(self):
        #스택이 비어있다.
        if self.empty()==1:
            return -1
        else:
            return self.stack[self._top]
        
    def empty(self):
        # 스택이 비어있다
        if self._top==-1:
            return 1
        else:
            return 0
            
    def pop(self):
        # 스택이 비어있지 않다
        if self.empty()!=1:
            self._top-=1
            return self.stack.pop()
        #스택이 비어있다
        else:
            return -1
        
    #size: 스택이 들어있는 정수의 개수 출력
    def size(self):
        # 스택이 비어있다
        if self.empty()==1:
            return 0
        #스택이 비어있지 않다면
        else:
            return len(self.stack)
            
def main():
    s=Stack() #스택객체를 만든다.
    N=int(sys.stdin.readline())
    for _ in range(N):
        commands=sys.stdin.readline().split()
        if commands[0]=='push':
            s.push(commands[1])
            
        elif commands[0]=='top':
            print(s.top())
            
        elif commands[0]=='empty':
            print(s.empty())
            
        elif commands[0]=='pop':
            print(s.pop())
            
        elif commands[0]=='size':
            print(s.size())
        

if __name__=='__main__':
    main()
