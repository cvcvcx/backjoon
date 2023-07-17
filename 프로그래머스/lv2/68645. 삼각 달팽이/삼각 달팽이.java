/*
코드 흐름
1. n*n의 배열을 생성
2. 1씩 값을 늘려가며 아래, 오른쪽 왼쪽위 방향으로 값을 채워나감
3. 값을 더이상 채울 수 없을 때 방향을 전환
4. 배열을 순회하며 일차원배열에 값을 담음
*/
class Solution {
    private final int[] dx = {0,1,-1};
    private final int[] dy = {1,0,-1};
    public int[] solution(int n) {
        int v = 1;
        int x = 0;
        int y = 0;
        int d = 0;
        int[][] triangle = new int[n][n];
        while (true){
            triangle[y][x] = v;
            v++;
            int nx = x+dx[d];
            int ny = y+dy[d];
            if(nx == n || ny == n ||nx == -1 || ny == -1 ||triangle[ny][nx] != 0){
                d = (d+1)%3;
                nx = x+dx[d];
                ny = y+dy[d];
                if(nx == n || ny == n ||nx == -1 || ny == -1 ||triangle[ny][nx] != 0){
                    break;
                }
            }
            x = nx;
            y = ny;
        }
        
        int[] result = new int[v-1];
        int index = 0;
        for (int i = 0; i<n; i++){
            for (int j = 0; j<=i; j++){
                result[index] = triangle[i][j];
                index++;
            }
        }
        
        
        return result;
    }
}