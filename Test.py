import Jason_Func
#import Loop_Menu
import Info_Function


from sql_functions import sql_info

json_file_address = './test.json'


# add new member info
def add_new_member_info(list_dic_infos):
    input_id = None
    while(1):
        print()
        input_id = input('ID : ').lower()

        is_same = False
        for info in list_dic_infos:
            if input_id == info['name'].lower():
                is_same = True
                break
        if is_same == False:
            break
        print('Try other Id this Id is exsit! ')

    input_pass = input('PASSWORD : ')
    input_age = input('AGE : ')
    input_cash = input('CASH : ')

    dic_input = {
        'name': input_id,
        'password': input_pass,
        'age': input_age,
        'cash': input_cash
    }
    list_dic_infos.append(dic_input)

# sql class static value


def sql_open():
    # SQL --------------------------------------
    create_table = """CREATE TABLE students(
    name TEXT NOT NULL, 
    password TEXT NOT NULL, 
    age INT, 
    cash INT
    )
    """

    return sql_info('ai_school.db', create_table)

def sql_insert_data_to_table(list_custom_info, class_sql):
    sql_into_shape = "INSERT INTO students VALUES (?, ?, ?, ?);"
    class_sql.add_to_sql_table(list_custom_info, sql_into_shape)


# MAIN_FUNCTION ----------------------------------------
def main():
    # open sql
    class_sql = None
    class_sql = sql_open()

    # import json file
    dic_from_json_data = Jason_Func.file_open(json_file_address)
    if dic_from_json_data == -1:
        return
    list_custom_info = dic_from_json_data['students']

    # render only students name
    print('- student Name - ')
    for dic_info in list_custom_info:
        print(dic_info['name'])

    # render only name
    #add_new_member_info(list_custom_info)

    # render age is less then 20 age - render
    Info_Function.render_info_keys(list_custom_info)
    for dic_info in list_custom_info:
        if 20 > int(dic_info['age']):
            Info_Function.render_info_values_02(dic_info)

    Jason_Func.file_save(json_file_address, {'students' : list_custom_info})

    # sql insert data to table
    sql_insert_data_to_table(list_custom_info, class_sql)

    # sql close
    if class_sql != None:
        class_sql.exit_sql()

    return

    # First Menu
    #login_id = Loop_Menu.render_login_menu(list_custom_info)

    # Sec Menu (render Info)1
    #Loop_Menu.render_info_menu(list_custom_info, login_id)
    Loop_Menu.render_info_menu(list_custom_info, 'zozo')


    # save json file
    Jason_Func.file_save(json_file_address, {'students' : list_custom_info})

if __name__ == '__main__':
    main()
