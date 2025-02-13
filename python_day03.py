import random

# (술, 안주) 리스트
drinks_foods = [
    ("위스키", "초콜릿"),
    ("와인", "치즈"),
    ("소주", "삼겹살"),
    ("고량주", "양꼬치"),
    ("사케", "광어회"),
    ("위스키", "낙곱새")  # 중복된 "위스키" 추가
]

# 술 목록 리스트
drinks_list = [drink[0] for drink in drinks_foods]

while True:
    menu = input(f'다음 술 중에 고르세요.\n'
                 f'1) {drinks_list[0]}   2) {drinks_list[1]}   3) {drinks_list[2]}   '
                 f'4) {drinks_list[3]}   5) {drinks_list[4]}   6) 아무거나   7) 종료 : ')

    if menu in ['1', '2', '3', '4', '5']:
        index = int(menu) - 1
        print(f'{drinks_list[index]}에 어울리는 안주는 {drinks_foods[index][1]} 입니다')

    elif menu == '6':
        random_index = random.randint(a: 0, len(drinks)-1)
        print(f'{random_drink}에 어울리는 안주는 {drinks_foods[random_drink]} 입니다')

        # random_drink = random.choice(drinks_foods_keys)
        # print(f'{random_drink}에 어울리는 안주는 {drinks_foods[random_drink]} 입니다')
    elif menu == '7':
        print(f'다음에 또 오세요')
        break