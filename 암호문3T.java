package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class 암호문3T {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st;
		LinkedList<String> password = new LinkedList<>();
		for (int t=1; t<=10; t++) {
			
		int N = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine(), " "); 
		
//		토큰한개씩 넣기 
		while (st.hasMoreTokens()) {
			password.add(st.nextToken());
		}
		
		// 삽입/삭제할 명령어도 토크나이저로 받기
		int M = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine(), " "); 
		int x,y;
		while(st.hasMoreTokens()) {
			//st의 첫번째 토큰 가져오기 
			switch (st.nextToken()) {
			// SWITCH 문 하나데 CASE 전부 들어감
			case "I":
				x = Integer.parseInt(st.nextToken());
				y = Integer.parseInt(st.nextToken());
				// x 뒤에 y번 토큰 넣기 
				for (int i=0; i<y; i++) {
					password.add(x++, st.nextToken());
				}
			break; //case I 끝나면 break 
			
			case "D":
				x = Integer.parseInt(st.nextToken());
				y = Integer.parseInt(st.nextToken());
				// x 뒤에 y번 토큰 넣기 
				for (int i=0; i<y; i++) {
					password.remove(x);
				}
			break; //case I 끝나면 break 
				
			case "A":
				y = Integer.parseInt(st.nextToken());
				// x 뒤에 y번 토큰 넣기 
				for (int i=0; i<y; i++) {
					password.add(st.nextToken());
					
				} break; //case I 끝나면 break 
				
		
			}
		}
			
		System.out.print("#" + t);
		for (int i = 0; i < 10; i++) {
			System.out.print(" " + password.get(i));
		}
		System.out.println();
		}
		
	}
}
