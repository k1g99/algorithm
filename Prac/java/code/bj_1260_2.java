// 백준 1260번 - DFS와 BFS
// https://www.acmicpc.net/problem/1260

import java.io.*;
import java.util.*;

public class bj_1260_2 {
    static ArrayList<Integer>[] graph;
    static ArrayList<Integer>[] graph2;
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

        graph = new ArrayList[N+1];
        graph2 = new ArrayList[N+1];
        for (int i = 0; i <= N; i++){
            graph[i] = new ArrayList<>();
            graph2[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            
            // 양방향 간선
            graph[start].add(end);
            graph2[start].add(end);
            graph[end].add(start);
            graph2[end].add(start);
        }
        // 입력된 간선들 정렬
        for (int i = 1; i <= N; i++){
            graph[i].sort(Comparator.naturalOrder());
            graph2[i].sort(Comparator.reverseOrder());
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

            for (Integer it : graph2[cur]){
                if (!isVisited[it]){
                    stack.addLast(it);
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

            for (Integer it : graph[cur]){
                if (!isVisited[it]){
                    queue.add(it);
                    isVisited[it] = true;
                }
            }
        }
    }
}