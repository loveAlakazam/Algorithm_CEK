import java.util.*;

public class Main
{
	public static int N,M;
	public static int map[][]=new int[500][500];
	public static Queue q= new LinkedList<Element>();
	public static int maximum=0;
	
	//1: ㅁ
	//2: L
	//3: ㅡ
	//4: 번개
	//5: ㅗ
	public static int shapey[][][]= {
			{{0,1,1}},
			{{1,2,2}, {1,2,2},  {0,0,1},  {0,0,1}, {1,1,1}, {1,1,1}, {0,1,2}, {0,1,2} },
			{{0,0,0}, {1,2,3}},
			{{1,1,2}, {1,1,2},   {0,1,1},  {0,1,1}}, 
			{{0,0,1}, {1,1,1},  {1,1,2}, {1,1,2}}
	};
	
	public static int shapex[][][]= {
			{{1,0,1}},
			{{0,0,1}, {0,0,-1}, {1,2,2}, {1,2,0}, {0,1,2}, {0,-1,-2}, {1,1,1}, {1,0,0}},
			{{1,2,3}, {0,0,0}},
			{{0,1,1}, {0,-1,-1}, {1,0,-1}, {1,1,2}},	
			{{1,2,1}, {-1,0,1}, {0,1,0}, {-1,0,0}}
	};
	
	public static boolean isRange(int y, int x) {
		if((y>=0&& y<N)&&(x>=0 && x<M))	return true;
		return false;
	}
	
	
	public static class Element{
		int y,x;
		Element(int y, int x){
			this.y=y;
			this.x=x;
		}
	}
	
	public static int bfs(int y, int x) {
		int max_now=0;
		Element e= new Element(y,x);
		q.add(e);
		
		//큐가 비어있지 않으면
		while(!q.isEmpty()) 
		{
			
			Element now= (Element)q.poll();
			for(int i=0; i<5; i++) //테트로미노 블록 종류
			{
				
				for(int j=0; j<shapey[i].length; j++)  //블록i의 대칭/회전 모양까지 고려.
				{
					int tmp=map[now.y][now.x];
					boolean isOkay=true;
					
					for(int k=0; k<shapey[i][j].length; k++) //나머지 블록3개
					{
						int nexty=now.y+shapey[i][j][k];
						int nextx=now.x+shapex[i][j][k];
                        
						if(isRange(nexty, nextx))
						{
							tmp+=map[nexty][nextx];
						}
						else{
							isOkay=false; //이 테트로미노에서는 적용안됨.
						}
						
					}
					
					//isOkay가 true인것만 max_now와 tmp를 비교할 수 있다.
					if(isOkay) 
					{
						max_now=Math.max(max_now, tmp);
					}
					
				}
			}
			
		}
		return max_now;
	}
	
	public static void main(String[] args) {
		//입력//
		Scanner sc= new Scanner(System.in);
		N=sc.nextInt();
		M=sc.nextInt();
		for(int y=0; y<N; y++) {
			for(int x=0; x<M; x++) {
				map[y][x]=sc.nextInt();
			}
		}
		
		//테트로미노의 최댓값을 찾는다.
		for(int y=0;y<N;y++) 
			for(int x=0; x<M; x++) 
				maximum=Math.max(maximum, bfs(y,x));
		
		System.out.println(maximum);
	}
}
