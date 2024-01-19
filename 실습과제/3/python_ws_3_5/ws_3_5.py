
number_of_book = 100

def create_user(data):
    name, age, address = data
    user_info = {'name': name, 'age': age, 'address': address}
    print(f'{name}님 환영합니다!')
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

user_list = list(zip(name, age, address))
many_user = list(map(create_user, user_list))


info = list(map(lambda user: {'name': user['name'], 'age': user['age']}, many_user))

def rental_book(user_info):
    name = user_info['name']
    age = user_info['age']
    number = age//10 
    decrease_book(number)
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')

def decrease_book(num_books):
    global number_of_book
    number_of_book -= int(num_books)
    print(f'남은 책의 수 : {number_of_book}')

for user_info in info:
    rental_book(user_info)


