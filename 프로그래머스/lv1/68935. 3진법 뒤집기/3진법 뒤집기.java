class Solution {
    public int solution(int n) {
        
        String s = Integer.toString(n,3);
        String reversed = new StringBuilder(s).reverse().toString();
        int answer = (Integer.parseInt(reversed,3));
        return answer;
    }
}