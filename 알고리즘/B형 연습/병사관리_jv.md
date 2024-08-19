발상
 - 순회를 최소화하기 위해 team 기준으로 병사들을 묶어 저장하기(파이썬과 동일)

구현
 - 링크드리스트? 

```java


class UserSolution
{
// 링크드리스트 노드 클래스 정의
    public class Node {
        int id;
        int v;
        Node nxt;
        Node(){}

        // id, v 넣었을때의 노드
        Node(int id, int v){
            this.id = id;
            this.v = v;
            this.nxt = null;
        }
        // nxt 넣었을때의 노드
        Node(int id, int v, Node nxt){
            this.id = id;
            this.v = v;
            this.nxt = nxt;
        }

}
    public Node[] node = new Node[200055];
    public int cnt =0;
    // 해당 id의 병사 정보 확인할 어레이
    public int[] version = new int[100055]; // 등록 여부
    public int[] num = new int[100055]; // 팀번호

    // id랑 노드 넣으면
    public Node getNewNode(int id, Node nxt){
        Node ret = node[cnt++]; // 노드 배열에서 하나 가져옴
        ret.id = id; // id
        ret.nxt = nxt; // 포인터
        ret.v = ++version[id];// version배열에서 +1해서 버전업데이트
        return ret;
    }
    public class Team {
        // head배열은 첫번쨰 병사, tail은 마지막 가리키는 노드 될것
        Node[] head = new Node[6];
        Node[] tail = new Node[6];
    }
    public Team[] t = new Team[6];

    public void init()
    {
        cnt = 0;
        for (int i=0;i<200055;i++){
            if (node[i] == null)
            // 빈 노드 배열에 대해
            // 200055개의 새로운 노드 객체 생성
            // 인덱스로 노드에 접근가능
            {node[i] = new Node();}
        }
        // 5개의 새로운 팀배열 생성
        // 각 팀의 tail = head =getNewNode?
        for (int i = 1; i <= 5; i++) {
            // 팀배열에 각각의 팀객체 저장
            t[i] = new Team();
            // 각 팀의 head노드와 tail노드 초기화
            for (int j = 1; j <= 5; j++) {
                t[i].tail[j] = t[i].head[j] = getNewNode(0, null);
            }
        }
        // 인원수만큼 version과 num 배열 초기화
        for (int i = 0; i <= 100000; i++) {
            version[i] = 0;
            num[i] = 0;
        }

    }

    public void hire(int mID, int mTeam, int mScore)
    {
        // 새로운 노드 생성
        Node newNode = getNewNode(mID, null);
        // 현재 팀노드의 tail.nxt 에 다음노드로 연결해주기
        t[mTeam].tail[mScore].nxt = newNode;
        // tail(마지막노드)가 새로 생성된 노드 가리키게 업데이트
        t[mTeam].tail[mScore] = newNode;
        num[mID] = mTeam; // num 에 병사의 팀번호 저장
    }

    public void fire(int mID)
    {
        version[mID] = -1; /// 해고당하면 -1값 저장
    }

    public void updateSoldier(int mID, int mScore)
    {   // 새로 고용하는 것과 동일.
        hire(mID, num[mID], mScore);
        // 단 versio에 의해 최신값이 업데이트 안돼서 최신정보 아닌걸로 간주
    }

    public void updateTeam(int mTeam, int mChangeScore)
    {
        if (mChangeScore < 0) {
            for (int j = 1; j <= 5; j++) {
                int k = j + mChangeScore;
                // k가 1보다 작과 5큰 일때 삼항연산자
                k = k < 1 ? 1 : (k > 5 ? 5 : k);
                if (j == k) continue;
                //j에 병사가 없으면 넘어감
                if (t[mTeam].head[j].nxt == null) continue;

                // j의 두번쨰를 k의 두번째에 연결 (즉 j의 첫번쨰 사라짐)
                t[mTeam].tail[k].nxt = t[mTeam].head[j].nxt;
                // k의 마지막도 j의 마지막으로 대체
                t[mTeam].tail[k] = t[mTeam].tail[j];

                t[mTeam].head[j].nxt = null;
                t[mTeam].tail[j] = t[mTeam].head[j];
            }
        }
        if (mChangeScore > 0) {
            for (int j = 5; j >= 1; j--) {
                // 새로운 점수그룹 k
                int k = j + mChangeScore;
                k = k < 1 ? 1 : (k > 5 ? 5 : k);
                if (j == k) continue;
                if (t[mTeam].head[j].nxt == null) continue;
                // k끝내 j새로 연겲
                t[mTeam].tail[k].nxt = t[mTeam].head[j].nxt;
                t[mTeam].tail[k] = t[mTeam].tail[j];
                t[mTeam].head[j].nxt = null;
                t[mTeam].tail[j] = t[mTeam].head[j];
            }
        }
    }

    public int bestSoldier(int mTeam)
    {
        // 점수 높은 그룹부터 탐색
        for (int j = 5; j >= 1; j--) {
            Node node = t[mTeam].head[j].nxt;
            if (node == null) continue;

            int ans = 0;
            while (node != null) {
                // 병사 정보 최실이때 가장 큰값 저장 
                if (node.v == version[node.id]) {
                    ans = ans < node.id ? node.id : ans;
                }
                node = node.nxt;
            }
            if (ans != 0) return ans;

        }
        return 0;
    }
}
```