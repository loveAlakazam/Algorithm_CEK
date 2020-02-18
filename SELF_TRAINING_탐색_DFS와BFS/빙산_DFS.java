/*
에이 나이제 자바할래....ㅡㅡ;;
python... dfs에선.. 개같은...
*/
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.Math;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main
{
	public static int ROW;
	public static int COL;
	public static int[][] iceBerg;
	public static int[][] tmp;
	public static int[] dy= {-1,1,0,0};
	public static int[] dx= {0,0,-1,1};
    
    
    public static boolean isRange(int y, int x) {
		if ((y>=0 && y<ROW) && (x>=0 && x<COL))
			return true;
		return false;
	}
    
    public static void dfs(int y, int x, boolean[][] visited) 
	{
		visited[y][x]=true; //방문한다
		//현위치의 상/하/좌/우
		for(int i=0; i<4; i++) {
			int nexty=dy[i]+y;
			int nextx=dx[i]+x;
			if (isRange(nexty, nextx)) {
				if((iceBerg[nexty][nextx]>0) && (!visited[nexty][nextx]))
					dfs(nexty, nextx, visited);
			}
				
		}
	}
	
	public static int getLinkedCnt() 
	{
		boolean visited[][]=new boolean[ROW][COL];
		int cnt=0;
		for(int y=0; y<ROW; y++) {
			for(int x=0; x<COL; x++) {
				if ( (iceBerg[y][x]!=0)&&(!visited[y][x]) ) {
					dfs(y,x,visited);
					cnt++;
				}
			}
		}
		return cnt;
	}
	
	public static int nextYear(int y, int x) {
		int water_cnt=0;
		for(int i=0; i<4; i++) {
			int nexty=dy[i]+y;
			int nextx=dx[i]+x;
			if(isRange(nexty, nextx)) {
				if(iceBerg[nexty][nextx]==0)
					water_cnt++;
			}
		}
		return water_cnt;
	}

	public static void main(String[] args)
    	{
		Scanner sc= new Scanner(System.in);
		ROW=sc.nextInt();
		COL=sc.nextInt();
		
		iceBerg=new int[ROW][COL];
		tmp=new int[ROW][COL];
		
		//배열만들기
		for(int y=0; y<ROW; y++) {
			for(int x=0; x<COL; x++) {
				iceBerg[y][x]=sc.nextInt();
			}
		}
		
		int year=0; //분리되는데 걸린시간
		int linkedCnt=0; //연결된 빙하개수
		while((linkedCnt=getLinkedCnt())<2)
        	{
			//연결된 빙하가 없다면, 빙하가 없다
			if (linkedCnt==0){
				year=0;
				break;
			}
			year++;
			
			//빙하를 녹인다.
			for(int y=0; y<ROW; y++) 
			{
				for(int x=0; x<COL; x++) {
					if(iceBerg[y][x]!=0) {
						tmp[y][x]=Math.max(iceBerg[y][x]-nextYear(y,x), 0);
					}
				}
			}
			
			//결과를 복사한다.
			for(int y=0; y<ROW; y++) {
				for(int x=0; x<COL; x++)
					iceBerg[y][x]=tmp[y][x];
			}
			
		}
		System.out.println(year);	
	}
}
