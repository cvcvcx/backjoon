import java.util.*;
class Solution {
    // 1. 의상의 부위가 나눠져있음
    // 2. 오늘 입은 의상과는 다르게 입어야함
    // 3. 중복이 없는 조합이여야하는데, 순서는 필요없음
    // 4. 같은 부위의 의상은 하나밖에 입지 못함
    // 완전 단순하게, 상의 3개와 하의 2개가 있을 때, 상의를 입지 않을 경우를 포함해 4가지 경우의 수, 하의를 입지 않을 경우를 포함해 3가지 경우의 수가 나온다.
    // 4*3 = 12 에서 상하의를 모두 입지 않은 경우를 제외한 11이 정답이 됨
    // 예시에서는 머리부위 2개 눈 1개이므로
    // 3*2 = 6 6-1 = 5 5가 나오게 된다.
    public int solution(String[][] clothes) {
        
        Map<String, Integer> map = new HashMap<>();
        
        for(String[] cloth : clothes){
            map.put(cloth[1],map.getOrDefault(cloth[1],0)+1);
        }
        int answer = 1;
        for(Integer n : map.values()){
            answer *= (n+1);
        }
        
        return answer-1;
    }
}