// 백준 1303번 - 전쟁 전투 
// https://www.acmicpc.net/problem/1303
// 기본적인 DFS/BFS 문제

import java.io.*;
import java.util.*;
import java.awt.*;

public class bj_1303 {
    static int N, M;
    static char[][] map;
    static boolean[][] isVisited;
    static int sumW, sumB;
    static Queue<Point> queue;
    static int[][] dir = {
        {-1,0}, // up
        {1,0},  // down
        {0,-1}, // left
        {0,1}   // right
    };
    static Point pt, newPt;

    public static void main(String[] args) throws IOException {
        // input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        sumW = 0;
        sumB = 0;
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new char[M][N];
        isVisited = new boolean[M][N]; // 기본적으로 false로 들어감

        for (int m = 0; m < M; m++){
            st = new StringTokenizer(br.readLine());
            String temp = st.nextToken();
            for (int n = 0; n < N; n++){
                char c = temp.charAt(n);
                map[m][n] = c;
            }
        }

        // algorithm
        char target = 'a';
        int groupCount = 0; 
        for (int r = 0; r < M; r++){
            for (int c = 0; c < N; c++){
                groupCount = 0;
                if (!isVisited[r][c]){
                    queue = new LinkedList<Point>();
                    queue.add(new Point(r, c));
                    isVisited[r][c] = true;

                    while (!queue.isEmpty()){
                        pt = queue.poll();
                        groupCount++;
                        target = map[pt.x][pt.y];

                        for (int i = 0; i < 4; i++){
                            newPt = new Point(pt.x + dir[i][0], pt.y + dir[i][1]);
                            if (checkCell(newPt)){
                                if (!isVisited[newPt.x][newPt.y] && Character.compare(map[newPt.x][newPt.y],target) == 0){
                                    queue.add(newPt);
                                    isVisited[newPt.x][newPt.y] = true;
                                }
                            }
                        }
                    }
                }

                if (Character.compare(target, 'W') == 0){
                    sumW += groupCount * groupCount;
                }else {
                    sumB += groupCount * groupCount;
                }
            }
        }

        System.out.printf("%d %d\n", sumW, sumB);

        // output
        br.close();
    }

    static boolean checkCell(Point p){
        if (p.x < 0){
            return false;
        }
        if (p.y < 0){
            return false;
        }
        if (p.x >= M){
            return false;
        }
        if (p.y >= N){
            return false;
        }
        return true;
    }
}
