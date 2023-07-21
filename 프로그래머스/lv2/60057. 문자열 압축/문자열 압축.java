import java.util.*;
class Solution {
    
    private List<String> split(String s, int length){
        List<String> tokens = new ArrayList<>();
        for(int i =0; i<s.length(); i+=length){
            int endIndex = i+length;
            if(endIndex>s.length()) endIndex = s.length();
            tokens.add(s.substring(i,endIndex));
        }
        return tokens;
    }
    
    private int compress(String s, int length){
        
        StringBuilder sb = new StringBuilder();
        String last = "";
        int count = 0;
        
        for(String str : split(s,length)){
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
        //단위별로 자른 문자배열을 만든다.
        //단위별로 자른 문자배열을 가지고, 압축된 단어를 만든다.
        //압축된 단어의 길이를 지금까지의 최소값과 비교한다.
        //압축된 단어가 더 짧으면, 최소값으로 친다.
        //1~s.length()까지를 돌면서, 단위를 새로 설정하면서 반복한다.
        //substring에서는 (startIndex에서,endIndex의 -1인덱스까지 잘라서 반환하게되므로, s.length()까지 돌아야함)
        
        int min = Integer.MAX_VALUE;
        for (int length = 1; length<=s.length();length++){
            int compressed = compress(s,length);
            min = min>compressed ? compressed : min;
        }
        return min;
    }
}