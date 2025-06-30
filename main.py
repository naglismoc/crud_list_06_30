from list_CRUD import *

holidays = load_holidays()
id_counter = 3
while True:
    print_info()
    opt = input()
    match opt:
        case '1':
           print_holidays(holidays)
        case '2':
           id_counter += 1
           create_holiday(id_counter, holidays)
        case '3':
           edit_holiday(holidays)
        case '4':
           delete_holiday(holidays)
        case '5':
            print('išeiti iš programos')
            break














# print(holidays)
# print(holidays[0])
# print(holidays[0]['city'])
#
# print("ivesk ką nors")
# tekstas = input()
# print(f"tu įvedei {tekstas}")