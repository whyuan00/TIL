package Solution;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class solution {

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("src/input.txt"));
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc<T+1; tc++ ) {
			
		int N = Integer.parseInt(br.readLine()); 
		StringTokenizer st; 
		
		int[] p = new int[N+1];
		int[] c1 = new int[N+1];
		int[] c2 = new int[N+1];
		
		st = new StringTokenizer(br.readLine());
		
		/// 1 1 3 ... -> i=2부터 i번째 c1[] c2[] 
		for (int c=2; c<2+N; c++) {
			int idx = Integer.parseInt(st.nextToken());
			
			//i의 부모가 p-> p의 c1과 c2 -> c1이 차있으면 c2가 i  
			
			
		}
		
			
			
		System.out.printf("#%tc",tc);
		System.out.print(' ');
//		System.out.print();
		System.out.println();
		}
		
		
	}
	
}
