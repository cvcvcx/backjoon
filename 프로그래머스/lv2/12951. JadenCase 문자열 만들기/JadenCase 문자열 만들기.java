class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        String[] stringArr = s.split("");
        boolean isUpper = true;
        for(String w : stringArr){
            if(isUpper){
                sb.append(w.toUpperCase());
                isUpper = false;
            }else{
                sb.append(w.toLowerCase());
            }
            if(w.equals(" ")){
                isUpper = true;
            }
        }
        
        return sb.toString();
    }
}