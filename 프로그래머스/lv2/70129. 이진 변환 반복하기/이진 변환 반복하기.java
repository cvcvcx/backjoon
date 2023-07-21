class Solution {
    public int[] solution(String s) {
        
        int zeroCount = 0;
        int count = 0;
        while(!s.equals("1")){
            count++;
            String temp = s.replace("0","");
            zeroCount += s.length() - temp.length();
            s = Integer.toString(temp.length(),2);
        }
        int[] answer = {count,zeroCount};
        return answer;
    }
}