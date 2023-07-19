class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        boolean isUpper = true;
        for (char c : s.toCharArray()){
            if(!Character.isAlphabetic(c)){
                isUpper = true;
                sb.append(c);
            }else{
                if(isUpper){
                    sb.append(Character.toUpperCase(c));
                    isUpper = false;
                }else{
                    sb.append(Character.toLowerCase(c));
                    isUpper = true;
                }    
            }
            
        }
        return sb.toString();
    }
}