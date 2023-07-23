import java.util.*;
class Solution {
    
    private List<String> split(String s, int length){
        List<String> result = new ArrayList<>();
        for(int startIdx = 0; startIdx<s.length(); startIdx += length){
            int endIdx = startIdx + length;
            if(endIdx > s.length()){
                endIdx = s.length();
            }
            result.add(s.substring(startIdx,endIdx));
        }
        return result;
    }
    
    private int compress(List<String> words){
        StringBuilder sb = new StringBuilder();
        String last = "";
        int count = 0;
        for(String word: words){
            if(last.equals(word)){
                count++;
            }else{
                if(count>1){
                    sb.append(count);    
                }
                sb.append(last);
                last = word;
                count = 1;
            }
        }
        if(count>1){
            sb.append(count);    
        }
        sb.append(last);
        return sb.length();
    }
    
    public int solution(String s) {
        
        //s를 정해진 숫자대로 나누는 함수
        int min = Integer.MAX_VALUE;
        
        for(int i = 1; i<=s.length();i++){
            List<String> words = split(s,i);
            int compressed = compress(words);
            min = compressed < min ? compressed : min;
        }
        //나눈 리스트를 가지고 압축된 문자열을 만들어 개수를 반환하는 함수
        
        
        
        return min;
    }
}