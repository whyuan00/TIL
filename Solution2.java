import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution2 {
    static int N, arr[][], pop[], popSum, ans;
    
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(bf.readLine());

        for (int tc = 1; tc <= t; tc++) {
            sb.append("#" + tc + " ");
            N = Integer.parseInt(bf.readLine());
            arr = new int[N][N];
            pop = new int[N];
            popSum = 0;
            ans = Integer.MAX_VALUE;

            // Reading adjacency matrix
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(bf.readLine());
                for (int j = 0; j < N; j++) {
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            // Reading population array and calculating total population
            st = new StringTokenizer(bf.readLine());
            for (int i = 0; i < N; i++) {
                pop[i] = Integer.parseInt(st.nextToken());
                popSum += pop[i];
            }

            // Start DFS from city 0
            dfs(0, 1, 0);

            sb.append(ans + "\n");
        }

        System.out.print(sb);
    }

    // DFS to explore all possible partitions of cities
    static void dfs(int city, int visitedCount, int city2Pop) {
        // If all cities are visited, update the answer with the population difference
        if (visitedCount == N) {
            int city1Pop = popSum - city2Pop;
            ans = Math.min(ans, Math.abs(city1Pop - city2Pop));
            return;
        }

        // Try visiting each unvisited city
        for (int i = 0; i < N; i++) {
            if (arr[city][i] == 1 && visitedCount < N && i != city && pop[i] != 0) {
                // Mark city as visited and update city2Pop
                int temp = pop[i];
                pop[i] = 0; // Mark population as 0 to avoid revisiting
                dfs(i, visitedCount + 1, city2Pop + temp);
                // Restore population value after DFS call
                pop[i] = temp;
            }
        }
    }
}
