import java.util.Arrays;
import java.util.Scanner;

public class Main{

	static int N;
	static int ropes[];
	static int result[][];
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		N=sc.nextInt();
		ropes=new int[N];
		result=new int[N][2]; 
		
		//로프 입력
		for(int n=0; n<N; n++)
			ropes[n]=sc.nextInt();
		
		//로프 오름차순 정렬
		Arrays.sort(ropes);
		
		//result
		result[0][0]=ropes[0];
		result[0][1]=N*ropes[0];
		
		int result_length=1;
		int i=1;
		while(i<N) 
		{
			if(ropes[i]!=ropes[i-1]) {
				result[result_length][0]=ropes[i];
				result[result_length][1]=(N-i)*ropes[i];
				result_length++;
			}
			i++;
		}
		
		//result를 1번째 원소값 중 가장 큰값을 탐색
		int answer=result[0][1];//맨앞로프로 설정..
		for(int n=result_length-1; n>=1; n--) {
			if(result[n][1]>answer)
				answer=result[n][1];
		}
		System.out.println(answer);
	}
}
