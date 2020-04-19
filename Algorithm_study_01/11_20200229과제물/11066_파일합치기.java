import java.util.Scanner;
public class Main{
	//최대 500개..
	static int dp[][];
	static int sum[];
	static int cost[];
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int T= sc.nextInt();
		int K;
		for(int t=0; t<T; t++) 
		{
			//K입력(K: 소설을 구성하는 장의 수)
			K=sc.nextInt();
			
			//초기화
			dp= new int[501][501];
			sum= new int[501];
			cost= new int[501];
			for(int i=0; i<K; i++)
				cost[i]=sc.nextInt();
			
			//0부터 0까지의 합
			sum[0]=cost[0];
			
			//0부터 i까지의 합
			for(int i=1; i<K; i++)
				sum[i]+=sum[i-1]+cost[i];
			
			//초기값저장
			for(int i=0; i<K-1; i++)
				dp[i][i+1]=cost[i]+cost[i+1];
			
			for(int gap=2; gap<K; gap++)//i와 j간 gap이 3이상일때 
			{
				for(int i=0; i+gap<K; i++) 
				{
					int j=i+gap;
					dp[i][j]=Integer.MAX_VALUE; //무한대
					
					for(int mid=i; mid<j; mid++)//i~j 사이의 k값
						dp[i][j]=Math.min(dp[i][j], dp[i][mid]+dp[mid+1][j]+sum(sum,i,j));
				}
			}
			System.out.println(dp[0][K-1]);
		}
	}
	
	public static int sum(int sum[], int i, int j) 
	{
		if(i==0)
			return sum[j];
		else
			return sum[j]-sum[i-1];
	}
}
