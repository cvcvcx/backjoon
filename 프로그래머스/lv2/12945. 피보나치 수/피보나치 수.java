class Solution {
    private static int[] data = new int[1000001];
    private static int fib(int n){
        if(n == 0){
            return 0;
        }else if(n==1){
            return 1;
        }
        if(data[n] != 0) return data[n]%1234567;
        
        return data[n] = ((fib(n-1))+(fib(n-2)))%1234567;
    }
    
    public int solution(int n) {
        
        int number = fib(n);
        int answer = number;
        return answer;
    }
}