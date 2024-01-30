# def create_user(name, age, address):
#     user_info = {}
#     user_info['name'] = name
#     user_info['age'] = age
#     user_info['address'] = address
#     print(f'{name}님 환영합니다!')
#     return user_info


# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부']


# user_list = list(zip(name, age, address))

# Final_list = []

# for i in range(5):
#     result = user_list[i]
#     x, y, z = result
#     result_1 = create_user(x, y, z) 
#     Final_list.append(result_1)

# print(Final_list)

def create_user(data):
    name, age, address = data
    user_info = {'name': name, 'age': age, 'address': address}
    print(f'{name}님 환영합니다!')
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

user_list = list(zip(name, age, address))

Final_list = list(map(create_user, user_list))

print(Final_list)