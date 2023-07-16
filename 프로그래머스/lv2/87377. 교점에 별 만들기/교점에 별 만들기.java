import java.util.*;
class Solution {
    /*
    1. 아이디어
        - 교점을 구한다.
        - 교점에서 정수로 나타낼 수 있는 수만 리스트에 추가한다.
        - 리스트에서 가장 큰 수와 가장 작은 수를 이용해 맵 배열의 크기를 구한다. +1하는거 조심
        - 맵 배열을 채운다.
        - 가장 큰 수와 가장 작은 수, 교점을 이용해서 새로운 배열에 교점을 찍는다.
        - String배열로 만들어 반환한다.
    
    2. 자료구조
    
        Point 클래스 생성 - long타입 x, y를 가진 Point클래스를 생성
        PointList 생성 - List<Point>를 통해 새로운 리스트를 생성
        맵 배열 생성 - char[][]를 통해 문자열을 구성할 맵 생성
        String answer - char[][]를 통해 String[]을 생성
    */
    private static class Point{
        public final long x, y;
        
        public Point(long x, long y){
            this.x = x;
            this.y = y;
        }
    }
    private Point intersection(long A, long B, long E, long C, long D, long F){
        double x = (double) (B*F - E*D)/(A*D - B*C);
        double y = (double) (E*C - A*F)/(A*D - B*C);
        
        if (x % 1 != 0 || y % 1 != 0){
            return null;
        }
        return new Point((long) x,(long) y);
    }
    
    private Point getMinValue(List<Point> points){
        long x = Long.MAX_VALUE;
        long y = Long.MAX_VALUE;
        
        for (Point p : points){
            x = p.x < x ? p.x : x;
            y = p.y < y ? p.y : y;
        }
        return new Point(x,y);
        
    }
    private Point getMaxValue(List<Point> points){
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
        for (int i = 0; i<line.length; i++){
            for (int j = i+1; j<line.length; j++){
                Point intersection = intersection(line[i][0],line[i][1],line[i][2],line[j][0],line[j][1],line[j][2]);
                if (intersection != null){
                    points.add(intersection);
                }
            }
        }
        Point minimum = getMinValue(points);
        Point maximum = getMaxValue(points);
        
        int width = (int)(maximum.x - minimum.x + 1);
        int height = (int)(maximum.y - minimum.y + 1);
        
        char[][] arr = new char[height][width];
        for (char[] row : arr){
            Arrays.fill(row,'.');
        }
        
        for (Point p : points){
            int x = (int)(p.x - minimum.x);
            int y = (int)(maximum.y - p.y);
            arr[y][x] = '*';
        }
        
        String[] answer = new String[arr.length];
        for (int i = 0; i<arr.length; i++){
            answer[i] = new String(arr[i]);
        }
        
        return answer;
    }
}