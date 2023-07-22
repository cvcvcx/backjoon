import java.util.*;
class Solution {
    class Point{
        public final long x;
        public final long y;
        
        public Point(long x, long y){
            this.x = x;
            this.y = y;
        }
    }
    
    private Point intersection(long A,long B, long E, long C, long D, long F){
        double x = (double)(B*F - E*D)/(A*D - B*C);
        double y = (double)(E*C - A*F)/(A*D - B*C);
        
        if(x % 1 != 0 || y % 1 != 0){
            return null;
        }
        return new Point((long) x,(long) y);
    }
    
    private Point getMinValue(List<Point> points){
        long x = Long.MAX_VALUE;
        long y = Long.MAX_VALUE;
        for(Point p: points){
            x = p.x<x ? p.x : x;
            y = p.y<y ? p.y : y;
        }
        
        return new Point(x,y);
    }
    
    private Point getMaxValue(List<Point> points){
        long x = Long.MIN_VALUE;
        long y = Long.MIN_VALUE;
        for(Point p: points){
            x = p.x>x ? p.x : x;
            y = p.y>y ? p.y : y;
        }
        
        return new Point(x,y);
    }
    
    public String[] solution(int[][] line) {
        List<Point> points = new ArrayList<>();
        for(int i = 0; i<line.length; i++){
            for(int j =i+1; j<line.length; j++){
                Point intersection = intersection(line[i][0],line[i][1],line[i][2],line[j][0],line[j][1],line[j][2]);
                if(intersection!=null){
                    points.add(intersection);
                }
            }
        }
        
        Point minimum = getMinValue(points);
        Point maximum = getMaxValue(points);
        
        int width = (int)(maximum.x-minimum.x+1);
        int height = (int)(maximum.y-minimum.y+1);
        
        char[][] arr = new char[height][width];
        
        for(char[] row: arr){
            Arrays.fill(row,'.');
        }
        
        for(Point p : points){
            int x = (int) (p.x - minimum.x);
            int y = (int) (maximum.y - p.y);
            arr[y][x] = '*';
        }        
        
        String[] answer = new String[arr.length];
        for(int i =0; i<answer.length; i++){
            answer[i] = new String(arr[i]);
        }
        
        return answer;
    }
}