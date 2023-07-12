class Solution {
    public int solution(int n) {
        int answer = 0;
        int startIdx = n % 2 == 0 ? 0 : 1;
        for (int i = startIdx; i <= n; i+=2){
            if (startIdx == 1){
                answer += i;
            }else{
                answer += i * i;
            }
        }
        return answer;
    }
}