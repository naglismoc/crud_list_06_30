import mysql.connector

DB_CONFIG = {
    'host':'localhost',
    'port':3312,
    'user':'root',
    'password':'root',
    'database':'holidays'
}

headers = ['id', 'country', 'city', 'accomodation', 'price']

def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

def load_holidays():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from holidays")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    # print(rows)
    holidays = []
    for row in rows:
        holiday = {}
        for i in range(len(row)):
            # print(i, row[i], headers[i])
            holiday[headers[i]] = row[i]
        holidays.append(holiday)
        # print(holiday)
    return holidays

def create_holiday(holidays):
    print('Itraukti atostogas:')
    print("iveskite šalį")
    country = input()
    print("Įvestike miestą")
    city = input()
    print("Įveskite apgyvendinimo tipą")
    accom = input()
    print("Įveskite kainą")
    price = input()

    conn = get_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO `holidays` (`country`,`city`,`accomodation`,`price`) VALUES (%s, %s, %s, %s);',
                (country, city, accom,price))
    conn.commit()

    cur.close()
    conn.close()

def edit_holiday(holidays):
    print('redaguoti atostogas')
    print("Pasirinkite ID atostogų kurias norite redaguoti")
    edit_id = input()
    #cia susirasti ka redaguosime
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from holidays where id = %s",(edit_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        print(f'{row[0]}. Atostogos {row[1]} {row[2]}. Kaina gyvenant {row[3]} parai {row[4]}')
        print("iveskite šalį")
        country = input()
        print("Įvestike miestą")
        city = input()
        print("Įveskite apgyvendinimo tipą")
        accom = input()
        print("Įveskite kainą")
        price = input()

        conn = get_conn()
        cur = conn.cursor()
        cur.execute('UPDATE `holidays` SET `country` = %s,`city` = %s,`accomodation` = %s, `price` = %s '
                    'WHERE `id` = %s;',
                (country, city, accom, price, int(edit_id)))
        conn.commit()
        cur.close()
        conn.close()
    else:
        print("Tokio pasirinkimo nera")

def delete_holiday(holidays):
    print('salinti atostogas')
    print("Pasirinkite ID atostogų kurias norite redaguoti")
    delete_id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM holidays WHERE id = %s",(delete_id,))
    conn.commit()
    cur.close()
    conn.close()

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

