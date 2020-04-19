class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int answer;
        int dp[][]= new int[101][101];
        int maps[][]=new int[101][101];
        
        //물웅덩이 => -1로 한다.
        //(px,py)
        for(int y=0; y<puddles.length; y++)
            maps[puddles[y][1]][puddles[y][0]]=-1;
        
        dp[1][0]=1;
        for(int y=1; y<=n; y++){
            for(int x=1; x<=m; x++){
                if (maps[y][x]==-1){
                    dp[y][x]=0;
                }
                    
                else{
                    dp[y][x]=(dp[y-1][x]+dp[y][x-1])%1000000007;
                }
            }
        }
        return dp[n][m];
    }
}
