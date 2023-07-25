class Solution {
    public int[] solution(int brown, int yellow) {
        
        for(int width = 3; width<=5000; width++){
            for(int height = 3; height<=width; height++){
                int tmpBrown = width*2 + (height-2)*2;
                int tmpYellow = width*height-tmpBrown;
                
                if(tmpBrown == brown && tmpYellow == yellow){
                    return new int[] {width,height};
                }
                
            }
        }
        
        return null;
    }
}