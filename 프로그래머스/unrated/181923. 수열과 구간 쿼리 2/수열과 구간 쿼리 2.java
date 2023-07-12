import java.util.*;
class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        for(int[] q : queries){
            int s = q[0];
            int e = q[1];
            int k = q[2];
            int tmp = 1000001;
            for (int i = s; i<e+1; i++){
                if (arr[i]>k && arr[i]<tmp){
                    tmp = arr[i];
                }
            }
            if (tmp == 1000001){
                tmp = -1;
            }
            answer.add(tmp);
            
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}