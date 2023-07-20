class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        boolean isUpper = true;
        for(char c : s.toCharArray()){
            char addChar = ' ';
            if(!Character.isAlphabetic(c)){
                isUpper = true;
            }else{
                if(isUpper){
                    addChar = Character.toUpperCase(c); 
                    isUpper = false;
                }else{
                    addChar = Character.toLowerCase(c);
                    isUpper = true;
                }
            }
            sb.append(addChar);
        }
        
        return sb.toString();
    }
}