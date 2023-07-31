class Solution {
    
    public int gcd(int x,int y){
        while(y != 0){
            int tmp = x;
            x = y;
            y = tmp%y;
        }
        return x;
    }
    
    public int lcm(int x, int y){
        int gcd = gcd(x,y);
        return x*y/gcd;
    }
        
    public int solution(int[] arr) {
        int answer = arr[0];
        for(int i = 1; i<arr.length; i++){
            answer = lcm(answer,arr[i]);
        }
        return answer;
    }
}