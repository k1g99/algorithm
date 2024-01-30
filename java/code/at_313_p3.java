import java.io.*;
import java.util.*;

public class at_313_p3 {
    public static void main(String[] args) throws IOException {
        // input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // algorithm
        long answer = 0;
        int N = Integer.parseInt(st.nextToken());        
        long[] number = new long[N];
        long[] target = new long[N];

        long sum = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++){
            int n = Integer.parseInt(st.nextToken());
            number[i] = (long) n;
            sum += n;
        }

        long x, y = 0;
        x = sum / N;
        y = sum - (N * x);
        for (int i = 0; i < N; i++){
            target[i] = x;
        }

        for (int i = N-1; i >= N-y; i--){
            target[i]++;
        }

        // number sort
        Arrays.sort(number);

        for (int i = 0; i < N; i++){
            long temp = Math.abs(target[i] - number[i]);
            answer += temp;
        } 

        // output
        System.out.println(answer/2);
        br.close();
    }
}