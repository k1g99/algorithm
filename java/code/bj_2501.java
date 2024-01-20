// 백준 2501번 - 약수 구하기
// https://www.acmicpc.net/problem/2501

import java.io.*;
import java.util.*;

public class bj_2501 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // input
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int cnt = 0;
        int answer = 0;

        for (int i = 1; i <= N; i++) {
            if (N % i == 0) {
                cnt++;
                if(cnt == K) {
                    answer = i;
                    break;
                }
            }
        }

        // output
        System.out.println(answer);
    } 
}
