import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        //서로 다른 종류의 수를 최소화 하고싶음
        //6개의 귤을 팔고싶은데, 크기가 최대한 같은 수를 구해야 함
        //같은 크기를 제일 많이 지닌 수부터 빼서, 만약 제일 많은 수에서 k의 개수가 다 빠진다면 result는 1
        //그 다음부터 1씩 증가함
        Map<Integer,Integer> map = new HashMap<>();
        //HashMap에서 Value를 기준으로 정렬하는 방법을 사용해야함
        for(int i = 0; i<tangerine.length; i++){
            map.put(tangerine[i],map.getOrDefault(tangerine[i],0)+1);
        }
        List<Integer> keyset = new ArrayList<>(map.keySet());
        keyset.sort((o1,o2) -> map.get(o2).compareTo(map.get(o1)));
        
        for(int i = 0; i<keyset.size(); i++){
            k -= map.get(keyset.get(i));
            answer++;
            if(k<=0){
                break;
            }
            
        }
        
        
        return answer;
    }
}