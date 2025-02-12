# assignmentDay03
import random
drinks = ["위스키", "와인", "소주", "고량주","사케","위스키"]
foods = ["초콜릿","치즈","삼겹살","양꼬치","광어회","낙곱새"]

def print_menu(index):
    index -= 1
    print(f'{drinks[index]}에 어울리는 안주는 {foods[index]} 입니다')

while True:
    menu = int(input(f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]}   6) 아무거나   7) 종료 : '))
    if menu <= (len(drinks) - 1):
        print_menu(menu)
    elif menu == len(drinks):
        random_index = random.randint(0,len(drinks) - 1)
        print_menu(random_index)
    elif menu == len(drinks) + 1:
        print(f'다음에 또 오세요')
        break
