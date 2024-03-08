import java.io.*;
import java.util.*;

public class at_313_p2 {
    public static void main(String[] args) throws IOException {
        // input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // algorithm
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        int[] cnt = new int[N+1];

        for (int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int to = Integer.parseInt(st.nextToken());
            int from = Integer.parseInt(st.nextToken());

            cnt[from]++;
        }

        int check = 0;
        for (int i = 1; i < N+1; i++){
            if (cnt[i] == 0){
                if (check == 0){
                    check = i;
                }else{
                    check = -1;
                }
            }
        }

        // output
        System.out.println(check);
        br.close();
    }
}
