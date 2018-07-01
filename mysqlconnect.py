import mysql.connector

import time
from flask import Flask, request, render_template, jsonify
from flask import json


def connectSql():
    # conn = mysql.connector.connect(user='cdiotest', passwd='12345678', host='127.0.0.1', db='Weatherdata')
    conn = mysql.connector.connect(user='cdiotest', passwd='12345678', host='127.0.0.1', db='weatherdb')
    return conn


def close(conn, cur):
    cur.close()
    conn.close()

def indexsql(wendu, shidu,yuliang,fengsu,qiya,fengxiang):
    uptime = int(time.time())
    sqlhead = "INSERT INTO `wd` (`uptime`, `wendu`,`shidu`,`yuliang`,`fengsu`,`qiya`,`fengxiang`) VALUES ("
    sqlvalues = "'"+str(uptime) + "','" + str(wendu) + "','" + str(shidu)+ "','" + str(yuliang)+ "','" + str(fengsu)+"','" + str(qiya)+"','" + str(fengxiang)+"')"
    conn = connectSql()
    cursor = conn.cursor()
    indexsql = sqlhead + sqlvalues
    cursor.execute(indexsql)
    conn.commit()
    close(conn, cursor)

def selectsql():
    sql = "SELECT wd.uptime,wd.wendu,wd.shidu,wd.yuliang,wd.fengsu,wd.qiya,wd.fengxiang FROM wd ORDER BY wd.uptime DESC LIMIT 120"
    conn = connectSql()
    cursor = conn.cursor()
    cursor.execute(sql)
    values = cursor.fetchall()
    close(conn, cursor)
    return values


def wsjson():
    values = selectsql()
    values.sort()
    data=[]
    for x in values:
        value = {}
        time_local = time.localtime(x[0])
        value['hour'] = time.strftime("%H:%M", time_local)
        value['wendu']=int(x[1])*0.01
        value['shidu']=int(x[2])
        data.append(value)
    return json.dumps(data)

def qyjson():
    values = selectsql()
    values.sort()
    data=[]
    for x in values:
        value = {}
        time_local = time.localtime(x[0])
        value['hour'] = time.strftime("%H:%M", time_local)

        value['qiya']=int(x[5])*0.01
        value['yuliang']=int(x[3])

        data.append(value)
    return json.dumps(data)

def fsjson():
    values = selectsql()
    values.sort()
    data=[]
    for x in values:
        value = {}
        time_local = time.localtime(x[0])
        value['hour'] = time.strftime("%M:%S", time_local)
        value['fengsu']=int(x[4])*0.01
        value['fengxiang']=int(x[6])
        data.append(value)
    return json.dumps(data)
