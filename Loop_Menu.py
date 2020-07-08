
import Info_Function

# RENDER_MANU ----------------------------------------
# func render login menu
def render_login_menu(list_custom_info):
    while (1):
        print('=========== 메 뉴 ===========')
        print('1. 회원가입')
        print('2. 로그인')

        try:
            select_menu_01 = int(input('메뉴를 선택하세요 : '))
        except ValueError as val_error:
            print('Please enter exact menu number ~')
            continue

        if select_menu_01 == 1:
            return Info_Function.add_new_info(list_custom_info)
        elif select_menu_01 == 2:
            # 로그인
            break
        else:
            print('잘못 입력하셨습니다. 다시입력하세요~')

# func render info
def render_info_menu(list_custom_info, login_id):
    list_info_me = []
    list_info_others = []
    list_info_me, list_info_others = Info_Function.divide_info(list_custom_info, login_id)

    while (1):
        print()
        print('=========== 정보보기 ===========')
        print('1. 내 정보')
        print('2. 다른사람 정보')
        print('3. 나가기')

        try:
            select_menu_02 = int(input('메뉴를 선택하세요 : '))
        except ValueError as val_error:
            print('Please enter exact menu number ~')
            continue

        if select_menu_02 == 1:
            Info_Function.render_info_keys(list_info_me)
            Info_Function.render_info_values(list_info_me)
        elif select_menu_02 == 2:
            Info_Function.render_others(list_info_others)
        elif select_menu_02 == 3:
            print('로그아웃 합니다 감사합니다.')
            break
        else:
            print('잘못 입력하셨습니다. 다시입력하세요~')
