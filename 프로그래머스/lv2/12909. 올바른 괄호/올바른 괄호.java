import java.util.*;
class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        boolean answer = true;
        for(char c: s.toCharArray()){
            if(c == '('){
                stack.push(c);
            }else{
                if(stack.empty()){
                    answer = false;
                    break;
                }else{
                    stack.pop();
                }
            }
        }
        if(!stack.empty()){
            answer = false;
        }

        return answer;
    }
}