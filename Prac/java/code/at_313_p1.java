
import java.io.*;
import java.util.*;

public class at_313_p1 {
    public static void main(String[] args) throws IOException {
        // input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // algorithm
        int n = Integer.parseInt(st.nextToken());
        
        st = new StringTokenizer(br.readLine());
        int oneNum = Integer.parseInt(st.nextToken());
        int answer = 0;

        for (int i = 1; i < n; i++){
            int next = Integer.parseInt(st.nextToken());

            if(oneNum <= next){
                answer = Math.max(answer, next - oneNum + 1);
            } 
        }

        // output
        System.out.println(answer);
        br.close();
    }
}
