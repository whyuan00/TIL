## 스트링, 리스트 (시퀀스)

# 튜플(시퀀스)
my_tuple = (1,) -> 정수를 하나 가진 튜플이다
my_tuple3 = (1, 'a', 2, 'b')

- 인덱싱, 슬라이싱, 길이 동일 
- 튜플은 변경이 불가능
    - my_tuple3[3] = 'z' 이런거x

- 불변 특징 있어서 파이썬 내부동작에서 주로 사용.
    - x,y = (10,20) 한번에 할당 
    - 쉼표가 생성자라 괄호 생략 가능 x,y = 10, 20

# range(시퀀스)
정수 시퀀스 ***생성***하는 변경 불가능한 자료형 

- range(0,n)은 n개 만들기때문에 n_1까지만 생성됨
- print(my_range)하면 range(0,5) 로 출력
    - 활용법1. print(list())로 바꿔서 데이터 확인


# dict(딕셔너리)
key와 value 쌍. 
- 시퀀스가 아니라 순서 없음
    - ***순서 없기때문에 인덱스가 안됨***. key와 value로 접근 
- 중복 없음
    - 같은 key에 값이 두개인경우 뒷값이 할당되어 출력됨
- 변경가능 자료형. key는 안되지만 value는 재할당 가능
    - key는 변경 불가능한 자료형만 사용(str, int, float, tuple, range...)
    - value는 모든값


# set(세트)
set은 중괄호 {}로 표기
단 빈세트는 set() 내장함수로 만듦. dict={} 가 기본값이기 때문. 

- 순서 없음
- 중복 없음
    - 중복 없애기 위해 set로 변환하면 순서가 바뀌는 문제 있음
- 변경 가능 
- 계산 가능
    - 합집합(|), 교집함(&), 차집합(-) 있음. 

## None
값이 없음을 표현하는 자료형, 값이자 타입
- variable = None, print(variable) = None (***N***)
## Boolean
참거짓 표현 

---

# colleciton 

시퀀스&논시퀀스 중 여러개의 항목or요소 담는 구조
- 순서 있으면 시퀀스(str,list,tuple) 
- 불변(str) 과 가변(list)

# type conversion(형변환)
1. 암시적 형변환_파이썬이 자동변환
    - print(3+5.0)=8.0, print(True +3)=4
2. 명시적 형변환_개발자가 변환
    - print(str(1)+'등') 

<<<<<<< HEAD
# 비교연산자
|기호 |내용|
|----|-----|
|is |같음|
|is not|같지 않음|
 
- ==는 데이터 값을 비교 
- is는 ***주소를 비교*** 주로 None, True, False 비교 
    - ex 3 is 3.0 = false
- print(1==True) = True(암시적 형변환)
- print(1 is True) = False

# 논리연산자(and or not )

- vowels = 'aeiou' / print(('b'and'a') in vowels) : True 
- print(0 and 3) : 0=false 암시적형변환, 바로 0
- print(0 and 0) : 0=false, 암시적형변환, 단축평가 앞0
- print(0 or 0) : 0, false, 뒤까지 가봐야함, 뒤 0

# 멤버십 연산자
- in
- not in ex. print(4 not in numbers) = false

# 시퀀스형 연산자 
- '+' , '*'
=======
>>>>>>> 83c4d331969febca2789199bb760f4f577624f5f
