import java.util.*;

class Solution {
    public Long[] solution(int n, long left, long right) {
        List<Long> numList = new ArrayList<>();
        for(long i = (long)left; i<=(long)right; i++){
            long row = i/n;
            long col = i%n;
            numList.add(Math.max(row,col)+1);
        }
        Long[] answer = numList.toArray(new Long[0]);
        return answer;
    }
}