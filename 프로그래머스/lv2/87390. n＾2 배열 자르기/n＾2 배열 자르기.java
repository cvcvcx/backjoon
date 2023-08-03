import java.util.*;

class Solution {
    public int[] solution(int n, long left, long right) {
        List<Integer> numList = new ArrayList<>();
        for(long i = (long)left; i<=(long)right; i++){
            int row = (int)(i/n);
            int col = (int)(i%n);
            numList.add(Math.max(row,col)+1);
        }
        int[] answer = numList.stream().mapToInt(i->i).toArray();
        return answer;
    }
}