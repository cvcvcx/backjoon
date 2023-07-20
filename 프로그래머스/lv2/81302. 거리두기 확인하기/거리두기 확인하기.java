class Solution {
    private static final int[] dx = {0,1,-1,0};
    private static final int[] dy = {1,0,0,-1};
    
    //좌표의 사방에 사람이 있는지 확인한다.
    private boolean isNextToVolunteer(char[][] room, int x, int y, int exclude){
        for(int d = 0; d<4; d++){
            if(d == exclude) continue;
            
            int nx = x+dx[d];
            int ny = y+dy[d];
            
            if(ny<0||ny>=room.length||nx<0||nx>=room[ny].length){
                continue;
            }
            
            if(room[ny][nx] == 'P'){
                return true;
            }
        }
        return false;
    }
    
    //방의 x,y좌표에 있는 사람이 거리두기를 지키고 있는지 판단한다.
    private boolean isDistanced(char[][] room, int x, int y){
        // x, y좌표에서 사방에 사람이 있는지 확인을 해야한다.
        // 사람이 있으면 바로 false를 반환하고, 사람이 없고 빈자리인 경우 그 사방에 사람이 존재하는지 확인해야함
        for(int d = 0; d<4; d++){
            int nx = x+dx[d];
            int ny = y+dy[d];
            if(ny<0||ny>=room.length||nx<0||nx>=room[ny].length){
                continue;
            }
            switch(room[ny][nx]){
                case 'P': return false;
                case 'O': 
                    if(isNextToVolunteer(room,nx,ny,3-d)){
                        return false;
                    }
                    break;
            }
            
        }
        return true;
    }
    
    //room을 받아서, 그 방이 거리두기를 지키고 있는지 판단
    private boolean isDistanced(char[][] room){
        //방의 거리두기를 판단한다.
        //판단하기 위해서 각 좌표에 사람이 있는 경우에, 거리두기를 지키고 있는지 판단해야한다.
        for(int y = 0; y<room.length; y++){
            for(int x = 0; x<room[y].length; x++){
                if(room[y][x] != 'P') continue;
                if(!isDistanced(room,x,y)) return false;
            }
        }
        //모두 검사했는데 거리두기를 지키지 않은 사람이 나오지 않으면 true를 반환하게 된다.;
        return true;
    }
    
    public int[] solution(String[][] places) {
        int[] answer = new int[places.length];
        for (int i =0; i<answer.length; i++){
            String[] place = places[i];
            char[][] room = new char[place.length][];
            for(int j = 0; j<room.length; j++){
                room[j] = place[j].toCharArray();
            }
            if(isDistanced(room)){
                answer[i] = 1;
            }else{
                answer[i] = 0;
            }
        }
        
        return answer;
    }
}