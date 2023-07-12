class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        StringBuilder sb = new StringBuilder();
        
        sb.append(Integer.toString(a));
        sb.append(Integer.toString(b));
        
        int aFirst = (Integer.parseInt(sb.toString()));
        
        sb.setLength(0);
        
        sb.append(Integer.toString(b));
        sb.append(Integer.toString(a));
        
        int bFirst = (Integer.parseInt(sb.toString()));
        
        if (aFirst >= bFirst){
            answer = aFirst;
        }else{
            answer = bFirst;
        }
        
        
        return answer;
    }
}