import getpass

# ADD_INFO ----------------------------------------
# func Add new info
def add_new_info(list_custom_info):
    while(1):
        print()
        input_id = input('ID : ')

        is_same = False
        for info in list_custom_info:
            if info['name'] == input_id:
                is_same = True
                break
        if is_same == False:
            break
        else:
            print('Same id is exist try other id please.')

    input_password = getpass.getpass('Password :')

    input_cash = input('How much do you have : ')

    dic_input = {
        'name' : input_id,
        'password' : input_password,
        'cash' : input_cash
    }
    list_custom_info.append(dic_input)

    print('Tank you for join our company !')
    return input_id

# DISPLAY_INFOMATION

# func divide info -> list
def divide_info(list_custom_info, login_id):
    list_info_me = []
    list_info_others = []

    for info in list_custom_info:
        if info['name'] == login_id:
            list_info_me.append(info)
        else:
            list_info_others.append(info)
    return list_info_me, list_info_others


def render_info_keys(list_custom_info):
    if len(list_custom_info) > 0:
        dic_keys = list_custom_info[0].keys()
        for key in dic_keys:
            print(f'{key}\t\t', end='')
        print()
        print('-------------------------------------------------')

# func Render Value
def render_info_values(list_info, is_need_menu = False):
    for i, dic_info in enumerate(list_info):
        if is_need_menu == True:
            print(f'{i + 1}. ', end='')
            print(f"{dic_info['name']}\t\t", end='')
        else:
            for val in dic_info.values():
                print(f'{val}\t\t', end='')
        print()
        print('-------------------------------------------------')

def render_info_values_02(dic_info, is_need_menu = False):
    for val in dic_info.values():
        print(f'{val}\t\t\t', end='')
    print()


def render_others(list_others):
    while(1):
        print()
        render_info_keys(list_others)
        render_info_values(list_others, is_need_menu=True)

        try:
            select_menu = int(input('메뉴를 선택하세요 : '))
        except ValueError as val_error:
            print('Please enter exact menu number ~')
            continue

        if select_menu > 0 and select_menu <= len(list_others):
            render_info_values(list(list_others[select_menu - 1]))
            break













