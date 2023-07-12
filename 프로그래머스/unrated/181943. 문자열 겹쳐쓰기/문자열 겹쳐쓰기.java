class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer  = "";
        for (int i = 0; i<s; i++){
            answer += my_string.charAt(i);
        }
        for (int j = 0; j<overwrite_string.length(); j++){
            answer += overwrite_string.charAt(j);
        }
        for (int k = s+overwrite_string.length(); k<my_string.length(); k++){
            answer += my_string.charAt(k);
        }
        return answer;
    }
}