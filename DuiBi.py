from flask import Blueprint, jsonify
import pymysql

DuiBi_api = Blueprint('DuiBi_api', __name__)


MG_curedCount = []
MG_deadCount = []
MG_confirmedCount = []

YG_curedCount = []
YG_deadCount = []
YG_confirmedCount = []

FG_curedCount = []
FG_deadCount = []
FG_confirmedCount = []

ZG_curedCount = []
ZG_deadCount = []
ZG_confirmedCount = []

YDL_curedCount = []
YDL_deadCount = []
YDL_confirmedCount = []

ER_curedCount = []
ER_deadCount = []
ER_confirmedCount = []

SP_curedCount = []
SP_deadCount = []
SP_confirmedCount = []

time = []


conn = pymysql.connect(host='127.0.0.1', user='root', password='963270357', port=3306, db='yiqing',
                           charset='utf8mb4')
cursor = conn.cursor()
sql = "SELECT ROUND(AVG(province_confirmedCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '美国' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    MG_confirmedCount.append(field[0])

sql = "SELECT ROUND(AVG(province_confirmedCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '英国' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    YG_confirmedCount.append(field[0])

sql = "SELECT ROUND(AVG(province_confirmedCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '法国' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    FG_confirmedCount.append(field[0])

sql = "SELECT overall.confirmedCount,time from overall ORDER BY time"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    ZG_confirmedCount.append(field[0])
    time.append(field[1])
print(time)

sql = "SELECT ROUND(AVG(province_confirmedCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '意大利' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    YDL_confirmedCount.append(field[0])

sql = "SELECT ROUND(AVG(province_confirmedCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '西班牙' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    SP_confirmedCount.append(field[0])

sql = "SELECT ROUND(AVG(province_confirmedCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '俄罗斯' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    ER_confirmedCount.append(field[0])

sql = "SELECT ROUND(AVG(province_curedCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '美国' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    MG_curedCount.append(field[0])


sql = "SELECT ROUND(AVG(province_curedCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '英国' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    YG_curedCount.append(field[0])


sql = "SELECT ROUND(AVG(province_curedCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '法国' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    FG_curedCount.append(field[0])

sql = "SELECT overall.curedCount,time from overall ORDER BY time"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    ZG_curedCount.append(field[0])

sql = "SELECT ROUND(AVG(province_curedCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '意大利' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    YDL_curedCount.append(field[0])

sql = "SELECT ROUND(AVG(province_curedCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '西班牙' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    SP_curedCount.append(field[0])

sql = "SELECT ROUND(AVG(province_curedCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '俄罗斯' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    ER_curedCount.append(field[0])

sql = "SELECT ROUND(AVG(province_deadCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '美国' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    MG_deadCount.append(field[0])


sql = "SELECT ROUND(AVG(province_deadCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '英国' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    YG_deadCount.append(field[0])


sql = "SELECT ROUND(AVG(province_deadCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '法国' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    FG_deadCount.append(field[0])

sql = "SELECT overall.deadCount,time from overall ORDER BY time"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    ZG_deadCount.append(field[0])

sql = "SELECT ROUND(AVG(province_deadCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '意大利' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    YDL_deadCount.append(field[0])

sql = "SELECT ROUND(AVG(province_deadCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '西班牙' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    SP_deadCount.append(field[0])

sql = "SELECT ROUND(AVG(province_deadCount)) as count ,updateTime from abroad GROUP BY countryName,updateTime HAVING updateTime in (SELECT DISTINCT(updateTime) from abroad) AND countryName like '俄罗斯' ORDER BY updateTime"
cursor.execute(sql);
result = cursor.fetchall()
for field in result:
    ER_deadCount.append(field[0])
cursor.close()
conn.close()


@DuiBi_api.route('/duibi/confirm', methods=['GET'])
def confirm():
    result = {"time": time, "MG_confirmedCount": MG_confirmedCount, "FG_confirmedCount": FG_confirmedCount, "YG_confirmedCount": YG_confirmedCount, "ZG_confirmedCount": ZG_confirmedCount, "YDL_confirmedCount": YDL_confirmedCount, "SP_confirmedCount": SP_confirmedCount, "ER_confirmedCount": ER_confirmedCount}
    return jsonify(result)


@DuiBi_api.route('/duibi/cured', methods=['GET'])
def cured():
    result = {"time": time, "MG_curedCount": MG_curedCount, "FG_curedCount": FG_curedCount, "YG_curedCount": YG_curedCount, "ZG_curedCount": ZG_curedCount, "YDL_curedCount": YDL_curedCount, "SP_curedCount": SP_curedCount, "ER_curedCount": ER_curedCount}
    return jsonify(result)


@DuiBi_api.route('/duibi/death', methods=['GET'])
def death():
    result = {"time": time, "MG_deadCount": MG_deadCount, "FG_deadCount": FG_deadCount, "YG_deadCount": YG_deadCount, "ZG_deadCount": ZG_deadCount, "YDL_deadCount": YDL_deadCount, "SP_deadCount": SP_deadCount, "ER_deadCount": ER_deadCount}
    return jsonify(result)
