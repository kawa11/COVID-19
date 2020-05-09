import pymysql
import csv

china = []
overall = []
abroad = []

def read_csv():
    with open('../csv/csv1/chinaArea_data.csv', encoding='utf-8') as f:
        f_csv = csv.reader(f)
        for i,row in enumerate(f_csv):
            if(i>=1):
                for index in range(0, len(row)):
                    if(row[index]==''):
                        row[index] = 0;
                china.append(row)
        insertChina(china)

    with open('../csv/csv1/abroadArea_data.csv', encoding='utf-8') as f:
        f_csv = csv.reader(f)
        for i,row in enumerate(f_csv):
            if(i>=1):
                for index in range(0, len(row)):
                    if(row[index]==''):
                        row[index] = 0;
                abroad.append(row[1:])
        insertAbroad(abroad)

def over():
    with open('../csv/csv1/overall.csv', encoding='utf-8') as f:
        f_csv = csv.reader(f)
        for i,row in enumerate(f_csv):
            if(i>=1):
                for index in range(0, len(row)):
                    if(row[index]==''):
                        row[index] = 0;
                overall.append(row[1:])
        insertOverall(overall)

def insertChina(data):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='963270357', port=3306, db='yiqing',
                           charset='utf8mb4')
    cursor = conn.cursor()
    sql = "insert into `china` values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.executemany(sql,data);
    conn.commit()
    cursor.close()
    conn.close()


def insertAbroad(data):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='963270357', port=3306, db='yiqing',
                           charset='utf8mb4')
    cursor = conn.cursor()
    sql = "insert into `abroad` values(null,%s,%s,%s,%s,%s,%s,%s)"
    cursor.executemany(sql,data);
    conn.commit()
    cursor.close()
    conn.close()

def insertOverall(data):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='963270357', port=3306, db='yiqing',
                           charset='utf8mb4')
    cursor = conn.cursor()
    sql = "insert into `overall` values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.executemany(sql,data);
    conn.commit()
    cursor.close()
    conn.close()


def delNone():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='963270357', port=3306, db='yiqing',
                           charset='utf8mb4')
    cursor = conn.cursor()
    sql = "DELETE FROM china WHERE updateTime < '01-24';"
    cursor.execute(sql);
    conn.commit()
    cursor.close()
    conn.close()

read_csv()
over()
delNone()