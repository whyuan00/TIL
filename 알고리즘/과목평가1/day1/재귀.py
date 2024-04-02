def 재귀함수(number):
    if number <2:
        return number

    else:
        k, v = divmod(number, 2)
        remain = str(v)
        result = str(재귀함수(k)) + remain

    return result


print(재귀함수(55))