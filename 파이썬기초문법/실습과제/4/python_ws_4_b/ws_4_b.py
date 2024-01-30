food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.

for key in food_list:
    종류 = key['종류']
    이름 = key['이름']
    
    if 이름 == '토마토':
        key['종류'] = '과일'
        print(f'{이름} 은/는 {key["종류"]} (이)다.') # key['종류']

    elif 이름 == '자장면':
        print('자장면엔 고춧가루지')
        print(f'{이름} 은/는 {종류} (이)다.')
         
    else:
        print(f'{이름} 은/는 {종류} (이)다.')
print(food_list)


while True:
    for key in food_list:
        종류 = key['종류']
        이름 = key['이름']
    
        if 이름 == '토마토':
            key['종류'] = '과일'
            print(f'{이름} 은/는 {key["종류"]} (이)다.') # key['종류']

        elif 이름 == '자장면':
            print('자장면엔 고춧가루지')
            print(f'{이름} 은/는 {종류} (이)다.')
         
        else:
            print(f'{이름} 은/는 {종류} (이)다.')
    
    print(food_list)
    break