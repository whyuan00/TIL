import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Solution1 {
	static int N, arr[][], pop[], popSum, visited[], ans, checkCnt, city2Hap;
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int t = Integer.parseInt(bf.readLine());
		
		
		
		for(int tc = 1; tc <= t; tc++) {
			sb.append("#"+tc+" ");
			N = Integer.parseInt(bf.readLine());
			arr = new int[N][N]; pop = new int[N]; popSum = 0; ans = Integer.MAX_VALUE; visited = new int[N];
			
			for(int i=0;i<N;i++) {
				st = new StringTokenizer(bf.readLine());
				for(int j=0;j<N;j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			st = new StringTokenizer(bf.readLine());
			for(int i=0;i<N;i++) {
				pop[i] = Integer.parseInt(st.nextToken());
				popSum += pop[i];
			}

			//무조건 0네 도시와 나머지네 로 나누면 됨.
			ArrayList<Integer> city = new ArrayList<>();
			city.add(0);
			visited[0] = 1;
			Geri(city, 0);
			

			sb.append(ans+"\n");
		}
		
		System.out.print(sb);
	}
	
	static void Geri(ArrayList<Integer> city, int num) {
		int city1Size = city.size(), city2Size = N - city1Size;
		int mainNum = -1;
		for(int i=0;i<N;i++) {
			if(visited[i] != 1) {
				mainNum = i; break;
			}
		}
		for(int i=0;i<N;i++) {
			if(visited[i] == 2) {
				visited[i] = 0;
			}
		}
		if(mainNum == -1) return;
		checkCnt = 1; city2Hap = pop[mainNum]; visited[mainNum] = 2;
		
		isCity2Available(mainNum);
		if(checkCnt == city2Size) {
//			System.out.println(Arrays.toString(visited)+" "+Math.abs(popSum - 2*city2Hap));
			
			ans = Math.min(ans, Math.abs(popSum - 2*city2Hap));
		}
		
		for(int i=0;i<N;i++) {
			if(arr[num][i] == 1 && visited[i] != 1) {

				visited[i] = 1;
//				System.out.println(Arrays.toString(visited));
				city.add(i);
//				System.out.println();
				Geri(city, i);
//				Geri(city, 0);
				visited[i] = 0;
				city.remove((Integer) i);
			}
		}
		
	}

	static void isCity2Available(int mainNum) {
		for(int i=0;i<N;i++) {
			if(arr[mainNum][i] == 1 && visited[i] == 0) {
				visited[i] = 2;
				checkCnt++; city2Hap += pop[i];
				isCity2Available(i);
			}
		}
		
	}
	

}
