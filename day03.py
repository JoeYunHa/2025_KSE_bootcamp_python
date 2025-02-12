# assignmentDay03
import random
drinks = ["위스키", "와인", "소주", "고량주","사케","위스키"]
foods = ["초콜릿","치즈","삼겹살","양꼬치","광어회","낙곱새"]


def print_menu(index):
    index -= 1
    print(f'{drinks[index]}에 어울리는 안주는 {foods[index]} 입니다')

while True:
    menu_lists = '다음 술중에 고르세요.'
    for i in range(len(drinks)):
        menu_lists += f'\t{i + 1}) {drinks[i]}'
    menu_lists += f'\t{len(drinks)}) 아무거나\t{len(drinks)+1}) 종료\n'
    menu = int(input(menu_lists))
    if menu <= (len(drinks) - 1):
        print_menu(menu)
    elif menu == len(drinks):
        random_index = random.randint(0,len(drinks) - 1)
        print_menu(random_index)
    elif menu == len(drinks) + 1:
        print(f'다음에 또 오세요')
        break
