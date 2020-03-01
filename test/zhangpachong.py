# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
#jupyter notebook一定运行这一行代码，在cell中显示图形
# -*- coding:utf-8 -*-
import baostock as bs
import pandas as pd
import tushare as ts
import datetime
import time
import sys
import pymysql

def get_name():
    ###登录系统###
    lg = bs.login()
    #显示登录返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond error_msg:' + lg.error_msg)
    ### 获取证券信息 ###
    nowdate = datetime.datetime.now()
    delta = datetime.timedelta(days=-2)
    today = nowdate + delta
    today = today.strftime('%Y-%m-%d')
    rs = bs.query_all_stock(day = today)
    print('query_all_stock respond error_code:' + rs.error_code)
    print('query_all_stock respond error_msg:' + rs.error_msg)
    ### 打印结果集 ###
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    ### 结果集输出到csv文件 ###
    #result.to_csv("E:\\all_stock.csv", encoding="gbk", index=False)
    ### 登出系统 ###
    bs.logout()
    conn = pymysql.connect("localhost", "root", "zjxtest", "stock",
                           use_unicode=True, charset="utf8")
    cursorl = conn.cursor()
    ls = []
    for i in range(len(result['code'])):
        ls.append([result['code'][i].split('.')[1], result['tradeStatus'][i],
                   result['code_name'][i]])
    #print(len(ls))
    for i in range(len(ls)):
        #sql = 'insert into stock_code_data values(%s,%s,%s,%s)'
        commit_data = [ls[i][0], ls[i][1].encode('utf8'), ls[i][2].encode('utf8'), today]
        #print(commit_data)
        cursorl.execute('insert into stock_code_data values(%s,%s,%s,%s)',commit_data)
        #cursorl.execute(sql, commit_data)
    conn.commit()
    conn.close()
    return ls
def get_today_stock(name_ls):
    for code in name_ls:
        a = ts.get_today_ticks(code)
        print(a)

def get_history_stock(last_date,now_date,name_ls):
    for code in name_ls:
        b = ts.get_hist_data(code, start=last_date, end=now_date)
        print(b)

if __name__ == '__main__':
    #nowdate = datetime.datetime.now() #现在
    #delta = datetime.timedelta(days=-1095)
    #lastdate = nowdate +delta
    #last_date = lastdate.strftime('%Y-%m-%d')
    #now_date = nowdate.strftime('%Y-%m-%d')
    name_ls = get_name()
    print (name_ls)
