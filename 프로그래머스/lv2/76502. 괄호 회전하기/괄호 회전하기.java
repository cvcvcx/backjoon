import java.util.*;

class Solution {
    
    public boolean isRightString(String s){
        Stack<Character> stack = new Stack<>();
        boolean result = true;
        for(char c : s.toCharArray()){
            if(c=='['){
                stack.push(']');
            }else if(c == '{'){
                stack.push('}');
            }else if(c == '('){
                stack.push(')');
            }else{
                if(!stack.empty()){
                    if(stack.peek() == c){
                        stack.pop();
                    }else{
                        return false;
                    }
                }else{
                    return false;
                }
            }
        }
        if(stack.empty()){
            return true;
        }else{
            return false;
        }
    }
    
    public int solution(String s) {
        int answer = 0;
        //substring을 이용해서 새로운 문자열을 만든다음 괄호가 올바른지 아닌지 판단
        //괄호가 올바른지 판단하기위해서는 스택을 사용해야함
        
        
        for(int i = 0; i<s.length(); i++){
            String str = s.substring(i) + s.substring(0,i);
            if(isRightString(str)){
                answer++;
            }
        }
        
        return answer;
    }
}