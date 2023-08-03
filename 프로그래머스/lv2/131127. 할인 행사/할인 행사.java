import java.util.*;

class Solution {
    // 1.일정금액 지원 -> 10일동안 회원자격
    // 2.회원 대상 매일 한가지 제품을 할인하는 행사
    // 3.할인 대상 상품은 하루에 하나
    // 4.원하는 제품과 수량이 할인하는 날짜가 10일이상 연속으로 일치할 경우에 맞춰 회원가입예정
    // 원하는 제품과 제품의 개수를 Map형태로 저장
    // 일자를 돌면서, 10일동안의 제품개수를 가지고 새로운 맵을 작성;
    // 맵을 for문을 돌려서, 원하는 상품 개수와, 새로 작성된 맵의 상품개수가 일치하면 통과 아니면 flag를 false로 하고 break;
    // flag를 통해 flag가 true라면 result++; 아니라면 다음 일자로 넘어감
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        Map<String,Integer> wantMap = new HashMap<>();
        for(int i=0; i<want.length; i++){
            wantMap.put(want[i],number[i]);
        }
        for(int i =0; i<=discount.length-10; i++){
            Map<String,Integer> discountMap = new HashMap<>();
            for(int j = i; j<i+10;j++){
                discountMap.put(discount[j],discountMap.getOrDefault(discount[j],0)+1);
            }
            boolean flag = true;
            for(String s : want){
                if(wantMap.get(s) != discountMap.get(s)){
                    flag = false;
                }
            }
            if(flag == true){
                answer++;
            }
        }
        
        return answer;
    }
}