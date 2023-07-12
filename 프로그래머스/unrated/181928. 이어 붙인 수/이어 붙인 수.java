class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        
        //정수형으로 변환한 뒤 짝수인지 검증하고, 홀수면 sb1에 짝수면 sb2에 할당
        for (int i = 0; i<num_list.length; i++){
            int num = num_list[i];
            if (num % 2 == 0){
                sb2.append(Integer.toString(num));
            }else{
                sb1.append(Integer.toString(num));
            }
        }
        
        int a = Integer.parseInt(sb1.toString());
        int b = Integer.parseInt(sb2.toString());
        return a+b;
    }
}