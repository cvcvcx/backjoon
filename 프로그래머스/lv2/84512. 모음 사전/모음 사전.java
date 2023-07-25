import java.util.*;
class Solution {
    
    private static final char[] aeiou = "AEIOU".toCharArray();
    
    private void makeDictionary(String word, List<String> words){
        words.add(word);
        
        if (word.length() == 5) return;
        
        for(char c : aeiou){
            makeDictionary(word+c,words);
        }
        return;
    }
    
    public int solution(String word) {
        List<String> words = new ArrayList<>();
        makeDictionary("",words);
        return words.indexOf(word);
    }
}