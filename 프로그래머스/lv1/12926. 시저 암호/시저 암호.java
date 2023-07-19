class Solution {
    
    private char push(char c, int n){
        int offset = Character.isUpperCase(c) ? 'A':'a';
        int num = (c + n - offset)%('Z'-'A'+1);
        return (char)(num+offset);
    }
    
    public String solution(String s, int n) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i<s.length(); i++){
            char c = s.charAt(i);
            if(Character.isAlphabetic(c)){
                sb.append(push(c,n));
            }else{
                sb.append(c);
            }
        }
        
        return sb.toString();
    }
}