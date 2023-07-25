import java.util.stream.*;

class Solution {
    private static final int[][] RULES = {
        {1,2,3,4,5},
        {2,1,2,3,2,4,2,5},
        {3,3,1,1,2,2,4,4,5,5}
    };
    
    private int getPicked(int people, int problem){
        int[] rule = RULES[people];
        int index = problem % rule.length;
        return rule[index];
    }
    
    public int[] solution(int[] answers) {
        
        int[] corrects = new int[3];
        int max = 0;
        
        for(int problem = 0; problem<answers.length; problem++){
            int answer = answers[problem];
            for(int people = 0; people<3; people++){
                if(answer == getPicked(people,problem)){
                    corrects[people]++;
                    max = corrects[people]> max ? corrects[people] : max;
                }
            }
        }
        
        final int maxCorrects = max;
        
        
        return IntStream.range(0,3)
            .filter(i->corrects[i] == maxCorrects)
            .map(i -> i+1)
            .toArray();
    }
}