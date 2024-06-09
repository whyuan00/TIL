
# result = 0
# def add_cal(num):
#     global result 
#     result = result +num
#     return result

# result = add_cal(3)
# print(result)

# print(add_cal(4))



# class add_cal:

#     def __init__(self,start):  # add_cal(start) 스타트 인자 넣어주기
#         self.go = start  #오른쪽 sta
#         rt값을 왼쪽에 할당. go 는 인스턴스 변수
#         print(f'init 함수 수행')

#     def add(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#         return self.num1 + self.num2 
    
# cal_1 = add_cal(0)
# print(cal_1.go)
# # add_cal.add(cal_1,0,3) 원래 이렇게 써야함


# 어카운트 클래스. 인스턴스에 오너 네임받기. 
# 어카운트 클래스 기능은 한사람이 새로 가입할때마다 모두 몇개인지 값을 저장. 변수 만들기

class Account:
    total_account = 0

    @classmethod
    def show_total_account(cls):
        print(Account.total_account)
    
    def __init__(self,name):
        self.name = name 
        Account.total_account = Account.total_account +1  #클래스에서 토탈어카운트 변수 불러와야함 

    def show_count(self):
        print(f'가입한 고객이름{self.name}, 총계좌수{Account.total_account}')  # 고객이름은 p1 인스턴스의 변수에있음, 총계좌수는 어카운트 클래스의 변수에 있음 
        


p1 = Account('Jane')
p1.show_count()

p2 = Account('John')
p2.show_count()   # show_count 는 인스턴스 메서드, ()로 선언해야함 

Account.show_total_account()