def my_multi(number_1, number_2):
    result_1 = int(number_1) * int(number_2)
    return result_1 

print(my_multi(2, 3))

# 결과 : 6
# 함수를 수정하고 호출 결과를 result_1 변수에 할당하여 출력하시오.


def is_negative(number):
    if number <= 0:
        result_2 = True
    else:
        result_2 = False
    
    return result_2

print(is_negative(3))

# is_negative(3) 결과 : False
# 함수를 수정하고 호출 결과를 result_2 변수에 할당하여 출력하시오.


def default_arg_func(default='기본값'):
    return default 

result_3 = default_arg_func()
result_4 = default_arg_func('다른 값')

print(result_3)
print(result_4)



