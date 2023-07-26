class Solution {
    public int[] solution(String s) {
        
        int zeroCount = 0;
        int count = 0;
        
        while(!s.equals("1")){
            String tmp = s.replace("0","");
            zeroCount += (s.length() - tmp.length());
            s = Integer.toString(tmp.length(),2);
            count++;
        }
        
        
        int[] answer = {count,zeroCount};
        return answer;
    }
}