
import java.util.*;
class Solution {
    private static class Point{
        public final long x;
        public final long y;
        
        public Point(long x, long y){
            this.x = x;
            this.y = y;
        }
    }
    // 1. 두 직선의 교점을 구한다. - 공식에 맞춰서 변수를 지정해서 헷갈림이 덜하도록 한다.
    private Point intersection(long A, long B, long E, long C, long D, long F){
        double x = (double) (B*F - E*D)/(A*D - B*C);
        double y = (double) (E*C - A*F)/(A*D - B*C);
        // 정수만 값을 가지게 한다.
        if (x % 1 != 0 || y % 1 != 0){
            return null;
        }
        
        return new Point((long) x, (long) y);
    }
    // 3. 최고점 최저점을 구한다. 아직까진 변환되지 않았으니까, long자료형을 써야한다.
    private Point getMinPoint(List<Point> points){
        long x = Long.MAX_VALUE;
        long y = Long.MAX_VALUE;
        
        for (Point p : points){
            x = p.x < x ? p.x : x;
            y = p.y < y ? p.y : y;
        }
        return new Point(x,y);
    }
    
    private Point getMaxPoint(List<Point> points){
        long x = Long.MIN_VALUE;
        long y = Long.MIN_VALUE;
        
        for (Point p : points){
            x = p.x > x ? p.x : x;
            y = p.y > y ? p.y : y;
        }
        return new Point(x,y);
    }
    
    public String[] solution(int[][] line) {
        List<Point> points = new ArrayList<>();
        // 2.정수를 저장한다. 두 개의 직선을 모두 점검해야하므로, 이 패턴이 등장한다.
        // 경우의 수를 따질 때 등장하는 패턴(조합? 순열?)
        for (int i = 0; i<line.length; i++){
            for (int j = i+1; j<line.length; j++){
                Point intersection = intersection(line[i][0],line[i][1],line[i][2],line[j][0],line[j][1],line[j][2]);
                if (intersection != null){
                    points.add(intersection);
                }
            }
        }
        // 3.최고점과 최저점을 구한다. 실제로 있는 좌표를 구하는 것이 아니라, x의 최고점, 최저점, y의 최고점 최저점을 구해서 좌표로 받는것이다.
        
        Point minimum = getMinPoint(points);
        Point maximum = getMaxPoint(points);
        // 4. 최고점 최저점을 이용해서 맵을 만든다. 이때부터 int로 변환된다.
        // 배열의 크기를 반환하는 것이므로, +1을 해주는 것을 잊지말자!
        int width = (int)(maximum.x - minimum.x+1);
        int height = (int)(maximum.y - minimum.y+1);
        
        char[][] arr = new char[height][width];
        // .으로 모든 좌표를 채워넣는다.
        for (char[] row : arr){
            Arrays.fill(row,'.');
        }
        
        // 5. 교점과 최고점, 최저점을 이용해서 맵에 맞는 좌표에 *을 찍는다.
        for (Point p : points){
            int x = (int)(p.x - minimum.x);
            int y = (int)(maximum.y - p.y);
            
            arr[y][x] = '*';
        }
        // 6. String 배열타입으로 char배열을 변환한다.
        String[] answer = new String[arr.length];
        
        for (int i = 0; i<arr.length; i++){
            answer[i] = new String(arr[i]);
        }
        return answer;
    }
}