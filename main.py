holidays = [
    {'id':1, 'country':"Lithuania", 'city':'Birštonas', 'price':60, 'accomodation':'hotel'},# 0
    {'id':2, 'country':"Lithuania", 'city':'Prienai', 'price':30, 'accomodation':'apartment'}, # 1
    {'id':3, 'country':"Lithuania", 'city':'Palanga', 'price':160, 'accomodation':'tent'},# 2
]
id_counter = 3
while True:
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti atostogu pasirinkimus")
    print("2. Įtraukti atostogas i sarasa")
    print("3. koreguoti atostogas")
    print("4. šalinti atostogas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")
    opt = input()

    match opt:
        case '1':
            for hol in holidays:
                print(f'{hol['id']}. Atostogos {hol['country']} {hol['city']}. Kaina gyvenant {hol['accomodation']}'
                      f' parai {hol['price']} ')
        case '2':
            print('Itraukti atostogas:')
            id_counter += 1
            id = id_counter
            print("iveskite šalį")
            country = input()
            print("Įvestike miestą")
            city = input()
            print("Įveskite apgyvendinimo tipą")
            accom = input()
            print("Įveskite kainą")
            price = input()
            holiday =  {'id':id, 'country':country, 'city':city, 'price':price, 'accomodation':accom}
            holidays.append(holiday)
        case '3':
            print('redaguoti atostogas')
            print("Pasirinkite ID atostogų kurias norite redaguoti")
            edit_id = input()
            for hol in holidays:
                if edit_id == str(hol['id']):
                    print(hol)
                    print("Įveskite šalį")
                    hol['country'] = input()
                    print("Įveskite miestą")
                    hol['city'] = input()
                    print("Įveskite apgyvendinimo tipą")
                    hol['accomodation'] = input()
                    print("Įveskite kainą")
                    hol['price'] = input()
        case '4':
            print('salinti atostogas')
            print("Pasirinkite ID atostogų kurias norite redaguoti")
            delete_id = input()
            for hol in holidays:
                if delete_id == str(hol['id']):
                    print(f'{hol['id']}. Šalinama: Atostogos {hol['country']} {hol['city']}. Kaina gyvenant'
                          f' {hol['accomodation']} parai {hol['price']} ')
                    holiday_index = holidays.index(hol)
                    del holidays[holiday_index]
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