import tushare as ts
import datetime
import pymysql
db = pymysql.connect("localhost", "root", "zjxtest", "stock")
cursor = db.cursor()
sql = "select * from `stock_code_data` where date='2020-02-28';"
cursor.execute(sql)
data1 = cursor.fetchall()
data1 = list(data1)
data = []
for i in data1:
    data.append([str(i[0]), str(i[1]), str(i[2]), str(i[3])])

data1 = []
for i in data:
    data1.append([i[0], i[3]])
print(data1)
db = pymysql.connect("localhost", "root", "zjxtest", "stock")
cursor = db.cursor()

for j in data1:
    date = datetime.datetime.strptime(j[1], '%Y-%m-%d')
    deltal = datetime.timedelta(days=-247)
    lastdate = date + deltal
    end = '2020-01-02'
    start = lastdate.strftime('%Y-%m-%d')
    print(start, end)
    code = j[0]
    b = ts.get_hist_data(code, start=start, end=end)
    print(str(type(b)))
    if str(type(b)) == "<class 'NoneType'>":
        pass
    else:
        lenth = len(b['close'])
        if lenth > 1:
            for a in range(lenth):
                inputdata = [code, str(b.index[a]), str(b['open'][a]), str(b['high'][a]), str(b['close'][a]),
                             str(b['low'][a]), str(b['volume'][a]), str(b['price_change'][a]), str(b['p_change'][a]),
                             str(b['ma5'][a]), str(b['ma10'][a]), str(b['ma20'][a]), str(b['v_ma5'][a]),
                             str(b['v_ma10'][a]), str(b['v_ma20'][a]), '0']
                cursor.execute('insert into stock_day_data values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                               inputdata)
        db.commit()
db.close()
print('end haha')