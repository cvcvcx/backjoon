import java.util.*;

class Solution
{
    public int solution(String s)
    {
        Stack<Character> stack = new Stack<>();
        
        int answer = -1;
        char[] charArr = s.toCharArray();
        for(char c : charArr){
            if(stack.empty()){
                stack.push(c);
            }else{
                if(stack.peek() == c){
                    stack.pop();
                }else{
                    stack.push(c);
                }
            }
        }
        if(stack.empty()){
            answer = 1;
        }else{
            answer = 0;
        }

        return answer;
    }
}