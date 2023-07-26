class Solution {
    
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        char[] arr = s.toCharArray();
        boolean isUpper = true;
        for(char c : arr){
            if(c == ' '){
                isUpper = true;
                sb.append(c);
            }else{
                if(isUpper == true){
                    sb.append(Character.toUpperCase(c));
                    isUpper = false;
                }else{
                    sb.append(Character.toLowerCase(c));
                }
            }
        }
        
        return sb.toString();
    }
}