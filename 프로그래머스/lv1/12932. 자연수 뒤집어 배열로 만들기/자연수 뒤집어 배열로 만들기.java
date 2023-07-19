class Solution {
    public int[] solution(long n) {
        String str = Long.toString(n);
        String reversed = new StringBuilder(str).reverse().toString();
        int[] answer = new int[str.length()];
        for (int i = 0; i<answer.length; i++){
            char c = reversed.charAt(i);
            answer[i] = c-'0';
        }
        
        
        return answer;
    }
}