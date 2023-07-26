class Solution {
    private int noOneCount(int n){
        String nStr = Integer.toString(n,2);
        int cnt = 0;
        for(char c : nStr.toCharArray()){
            if(c=='1') cnt++;
        }
        return cnt;
    }
    
    public int solution(int n) {
        int answer = 0;
        int oneCount = noOneCount(n);
        int number = n;
        while(true){
            number++;
            int numberOneCount = noOneCount(number);
            if(numberOneCount == oneCount){
                answer = number;
                break;
            }
        }
        
        return answer;
    }
}