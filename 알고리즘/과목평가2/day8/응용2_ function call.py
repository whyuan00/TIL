#function call: 프로그램에서 호출과 복귀에 따른 수행순서 관리

#함수호출시 수행에 필요한 지역변수, 매개변수, 수행후 복귀주소 등을 스택프레임에 저장, 시스템 스택에 삽입

#함수 실행 끝나면 스택 프레임이 삭제됨, 복귀주소 바탕으로 복귀
# 호출과 복귀에 따라 반복, 전체 수행 끝나면 시스템 스택은 공백 스택이 됨

def f2(n):
    n *= 2
    print(n)
def f1(c,d):
    e= c+d
    f2(e)


a = 10
b = 20
c = a+b
f1(a,b)

