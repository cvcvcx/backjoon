class Solution {
    private static final int[] dx = {0,1,-1,0};
    private static final int[] dy = {1,0,0,-1};
    private boolean isNextPeople(char[][] room, int x, int y, int exclude){
        // x,y좌표의 사방중 exclude를 제외하고, 나머지 방향에 사람이 있는지 확인
        
        for(int d = 0; d<4; d++){
            if (d == exclude) continue;
            
            int nx = x+dx[d];
            int ny = y+dy[d];
            
            if(ny >= room.length|| ny<0 || nx>=room[ny].length || nx<0){
                continue;
            }
            if(room[ny][nx] == 'P') return true;
        }
        return false;
    }
    
    private boolean isDistance(char[][] room, int x ,int y){
        //방의 x, y좌표에있는 사람이 거리두기를 지키고 있는지 확인
        for(int d = 0; d<4; d++){
            int nx = x+dx[d];
            int ny = y+dy[d];
            if(ny >= room.length||ny<0 || nx>=room[ny].length || nx<0){
                continue;
            }
            switch(room[ny][nx]){
                case 'P': return false;
                case 'O':
                    if(isNextPeople(room,nx,ny,3-d)) return false;
                    break;
            }
        }
        return true;
        
    }
    
    
    private boolean isDistance(char[][] room){
        for(int i =0; i<room.length; i++){
            for (int j =0; j<room[i].length; j++){
                if(room[i][j] != 'P') continue;
                if(!isDistance(room,j,i)){
                    return false;
                }
            }
        }
        return true;
    }
    
    public int[] solution(String[][] places) {
        int[] answer = new int[places.length];
        //거리두기 판별을 위해 맵을 생성
        for(int i = 0; i<answer.length; i++){
            String[] place = places[i];
            char[][] room = new char[place.length][];
            for(int j = 0; j<room.length; j++){
                room[j] = place[j].toCharArray();
            }
            if(isDistance(room)) {
                answer[i] = 1;
            }else{
                answer[i] = 0;
            }
        }
        //생성한 맵을 가지고 거리두기에 적합한지 확인
        return answer;
    }
}