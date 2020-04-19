import java.util.*;

class Solution {
    //상하좌우
    static int dy[]={-1,1,0,0};
    static int dx[]={0,0,-1,1};
    static Queue q= new LinkedList<Element>();
    
    
    static class Element{
        int y, x, val;
        Element(int y, int x, int val){
            this.y=y;
            this.x=x;
            this.val=val;
        }
    }
    
    public static int BFS(int y, int x, int val, int m, int n, int [][]picture, boolean [][]visited){
        int cnt=0; //영역개수
        
        //객체를 만들어서 큐에 넣는다.
        Element e= new Element(y,x,val); 
        q.add(e);
        
        while(!q.isEmpty())
        {
            Element now= (Element) q.poll();
            
            if(!visited[now.y][now.x])
            {
                //현재위치를 아직 방문하지 않았다면-> 방문을 한다.
                visited[now.y][now.x]=true;
                
                cnt++; //영역개수 카운트
                
                for(int i=0; i<4; i++)
                {
                    //현위치의 상하좌우가 m행n열인지 확인
                    int nexty=now.y+dy[i];
                    int nextx=now.x+dx[i];
                    if((nexty>=0&&nexty<m)&&(nextx>=0&&nextx<n))
                    {
                        //현위치 상하좌우가 현위치의 값과 같고 아직 방문안한상태라면
                        if((picture[nexty][nextx]==now.val)&&(!visited[nexty][nextx])){
                            Element next=new Element(nexty,nextx,now.val);
                            q.add(next);
                        }      
                    }
                }
            }
        }
        return cnt;
    }
    
    
  public int[] solution(int m, int n, int[][] picture) {
      
      int numberOfArea = 0;
      int maxSizeOfOneArea = 0;
      int[] answer = new int[2];
      boolean visited[][]=new boolean[100][100]; //방문리스트 //신기한게 visited를 지역변수로 하면 된다!->전역변수로하면 실패뜸.
      
      for(int y=0; y<m; y++){
          for(int x=0; x<n; x++){
              if((picture[y][x]!=0) && (!visited[y][x])){
                  
                  maxSizeOfOneArea=Math.max(maxSizeOfOneArea, BFS(y, x, picture[y][x], m, n, picture, visited));
                  numberOfArea++;
              }
          }
      }
      answer[0] = numberOfArea;
      answer[1] = maxSizeOfOneArea;
      return answer;
  }
}
