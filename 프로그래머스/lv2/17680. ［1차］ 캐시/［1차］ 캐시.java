import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        if(cacheSize==0){
            return cities.length*5;
        }
        
        int answer = 0;
        LinkedList<String> queue = new LinkedList<>();        
        for(String s : cities){
            s = s.toUpperCase();
            if(queue.remove(s)){
                answer++;
                queue.add(s);
            }else{
                answer+=5;
                if(queue.size()>=cacheSize){
                    queue.remove(0);
                }
                queue.add(s);
            }
        }       
        
        return answer;
    }
}