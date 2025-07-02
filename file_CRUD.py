import csv

headers = ['id','country','city','price','accomodation']
def load_holidays():
  with open("lithuania_accommodation.csv",mode='r',encoding='utf-8') as file:
      return list(csv.DictReader(file))

def save_holidays(holidays):
    with open("lithuania_accommodation.csv", mode='w',newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(holidays)

def create_holiday(holidays):
    print('Itraukti atostogas:')
    id = str(int(holidays[-1]['id']) + 1) if len(holidays) > 0 else 1
    print("iveskite šalį")
    country = input()
    print("Įvestike miestą")
    city = input()
    print("Įveskite apgyvendinimo tipą")
    accom = input()
    print("Įveskite kainą")
    price = input()
    holiday = {'id': id, 'country': country, 'city': city, 'price': price, 'accomodation': accom}
    holidays.append(holiday)
    save_holidays(holidays)

def edit_holiday(holidays):
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
            break
    save_holidays(holidays)

def delete_holiday(holidays):
    print('salinti atostogas')
    print("Pasirinkite ID atostogų kurias norite redaguoti")
    delete_id = input()
    for hol in holidays:
        if delete_id == str(hol['id']):
            print(f'{hol['id']}. Šalinama: Atostogos {hol['country']} {hol['city']}. Kaina gyvenant'
                  f' {hol['accomodation']} parai {hol['price']} ')
            holiday_index = holidays.index(hol)
            del holidays[holiday_index]
    save_holidays(holidays)



def print_holidays(holidays):
    for hol in holidays:
        print(f'{hol['id']}. Atostogos {hol['country']} {hol['city']}. Kaina gyvenant {hol['accomodation']}'
              f' parai {hol['price']} ')

def print_info():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti atostogu pasirinkimus")
    print("2. Įtraukti atostogas i sarasa")
    print("3. koreguoti atostogas")
    print("4. šalinti atostogas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")

