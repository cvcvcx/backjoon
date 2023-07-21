import java.util.*;
class Solution {
    
    private List<String> split(String source, int length){
        List<String> tokens = new ArrayList<>();
        for(int i = 0; i<source.length(); i+=length){
            int endIndex = i + length;
            if(endIndex > source.length()){
                endIndex = source.length();
            }
            tokens.add(source.substring(i,endIndex));
        }
        return tokens;
    }
    
    private int compress(String source, int length){
        String last = "";
        StringBuilder sb = new StringBuilder();
        int count = 0;
        List<String> tokens = split(source,length);
        for(String str : tokens){
            if(str.equals(last)){
                count++;
            }else{
                if(count>1){
                    sb.append(count);
                }
                sb.append(last);
                last = str;
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
        int min = Integer.MAX_VALUE;
        
        for(int length = 1; length<=s.length(); length++){
            int compressed = compress(s,length);
            if (compressed<min) {
                min = compressed;
            }
        }
        return min;
    }
}