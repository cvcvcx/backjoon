class Solution {
    //0의 개수와 1의 개수를 가진 객체 클래스 (압축된 범위의 1과 0의 개수를 세기 위한 클래스)
    private static class Count{
        public final int zero;
        public final int one;
        
        public Count(int zero, int one){
            this.zero = zero;
            this.one = one;
        }
        public Count add(Count other){
            return new Count(this.zero+other.zero,this.one+other.one);
        }        
    }
    //재귀함수 count arr의 범위에 있고, offsetX, offsetY,size를 압축하는 점화식과 종료조건을 표현해야함
    private Count count(int[][] arr,int offsetX,int offsetY, int size){
        int h = size/2;
        for(int y = offsetY; y<offsetY+size; y++){
            for(int x = offsetX; x<offsetX+size; x++){
                if(arr[y][x]!=arr[offsetY][offsetX]){
                    //사등분한 범위의 Count를 모두 합친 값을 반환
                    return count(arr,offsetX,offsetY,h)
                        .add(count(arr,offsetX+h,offsetY,h))
                        .add(count(arr,offsetX,offsetY+h,h))
                        .add(count(arr,offsetX+h,offsetY+h,h));
                }
            }
        }
        if(arr[offsetY][offsetX] == 0){
            return new Count(1,0);
        }else{
            return new Count(0,1);
        }
    }
    
    
    
    public int[] solution(int[][] arr) {
        Count count = count(arr,0,0,arr.length);
        return new int[] {count.zero,count.one};
        
    }
}