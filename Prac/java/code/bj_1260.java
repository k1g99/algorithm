// 백준 1260번 - DFS와 BFS
// https://www.acmicpc.net/problem/1260

import java.io.*;
import java.util.*;

public class bj_1260 {
    static int[][] graph; // edges를 2d array로 구현
    static Queue<Integer> queue = new LinkedList<>(); // java에서 queue는 linkedlist 사용
    static Deque<Integer> stack = new ArrayDeque<>(); // java에서 stack은 ArrayDeque 사용
    static int N, M, V;
    static boolean[] isVisited;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        // input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        // N M V (정점, 간선, 탐색 시작 node)
        // 간선 (1 2)
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        graph = new int[N+1][N+1];

        for (int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            
            // 양방향 간선
            graph[start][end] = 1;
            graph[end][start] = 1;
        }

        // algorithm
        dfs(V);
        sb.append("\n");
        bfs(V);
        System.out.println(sb);
        br.close();
    }

    static void dfs(int startNode){
        isVisited = new boolean[N+1]; 
        stack.addFirst(startNode);
        
        while (!stack.isEmpty()){
            int cur = stack.removeLast();
            if (isVisited[cur]) continue;
            sb.append(cur + " ");
            isVisited[cur] = true;

            for (int i = N; i > 0; i--){
                if (graph[cur][i] == 1 && !isVisited[i]){
                    stack.add(i);
                }
            }
        }

    }

    static void bfs(int startNode){
        isVisited = new boolean[N+1]; 
        queue.add(startNode);
        isVisited[startNode] = true;
        
        while (!queue.isEmpty()){
            int cur = queue.poll();
            sb.append(cur + " ");

            for (int i = 1; i <= N; i++){
                if (graph[cur][i] == 1 && !isVisited[i]){
                    queue.add(i);
                    isVisited[i] = true;
                }
            }
        }

    }
}