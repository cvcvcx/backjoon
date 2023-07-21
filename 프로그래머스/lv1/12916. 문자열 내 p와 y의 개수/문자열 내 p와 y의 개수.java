class Solution {
    boolean solution(String s) {
        s = s.toLowerCase();
        String yString = s.replace("p","");
        String pString = s.replace("y","");
        if (yString.length() == pString.length()){
            return true;
        }else{
            return false;
        }
    }
}