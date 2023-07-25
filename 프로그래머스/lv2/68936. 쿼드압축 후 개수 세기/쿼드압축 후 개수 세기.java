class Solution {
    public class Count{
        public final int zero;
        public final int one;
        
        public Count(int zero, int one){
            this.zero = zero;
            this.one = one;
        }
        
        public Count add(Count other){
            return new Count(this.zero+other.zero, this.one+other.one);
        }
    }
    
    private Count count(int x, int y, int[][] arr, int size){
        
        for(int i = y; i<y+size; i++){
            for (int j = x; j<x+size; j++){
                if(arr[i][j] != arr[y][x]){
                    return count(x,y,arr,size/2)
                        .add(count(x+size/2,y,arr,size/2))
                        .add(count(x,y+size/2,arr,size/2))
                        .add(count(x+size/2,y+size/2,arr,size/2));
                }
            }
        }
        if(arr[y][x] == 1){
            return new Count(0,1);
        }else{
            return new Count(1,0);
        }
        
    }
    
    public int[] solution(int[][] arr) {
        
        Count count = count(0,0,arr,arr.length);
        
        int[] answer = {count.zero,count.one};
        return answer;
    }
}