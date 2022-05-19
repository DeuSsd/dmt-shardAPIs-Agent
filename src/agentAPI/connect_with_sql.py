import sqlite3
conn = sqlite3.connect('web_api.db')
cur = conn.cursor()
import json

#cur.execute("""CREATE TABLE IF NOT EXISTS web_api(api_id INT PRIMARY KEY,name_api TEXT,website TEXT);""")
#conn.commit()

#cur.execute("""CREATE TABLE IF NOT EXISTS param_api(id INT PRIMARY KEY,api_id INT,parameters_api TEXT,type_parameters TEXT);""")
#conn.commit()

#api1 = ('2', 'COVIDAPI', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
#api_par_1=('4','2','start_time','time')
#api_par_2=('5','2','end_time','time')
#api_par_3=('6','2','location','string')
#cur.execute("INSERT INTO web_api VALUES(?, ?, ?);", api1)
#cur.execute("INSERT INTO param_api VALUES(?, ?, ?, ?);", api_par_1)
#cur.execute("INSERT INTO param_api VALUES(?, ?, ?, ?);", api_par_2)
#cur.execute("INSERT INTO param_api VALUES(?, ?, ?, ?);", api_par_3)
#conn.commit()

def get_API():
    conn = sqlite3.connect('web_api.db')
    cur = conn.cursor()
    list_api=[]
    cur.execute("SELECT name_api FROM web_api;")
    res=cur.fetchall()
    for i in range(len(res)):
        list_api.append(res[i][0])
    return list_api

def get_web(name_api):
    conn = sqlite3.connect('web_api.db')
    cur = conn.cursor()
    list_api = []
    cur.execute("SELECT name_api,website FROM web_api;")
    res = cur.fetchall()
    for i in range(len(res)):
        list_api.append(res[i])
    for i in range(len(list_api)):
        if list_api[i][0]==name_api:
            return list_api[i][1]
    return 'no data'

def from_web_to_api(name_web):
    conn = sqlite3.connect('web_api.db')
    cur = conn.cursor()
    list_api = []
    cur.execute("SELECT name_api,website FROM web_api;")
    res = cur.fetchall()
    for i in range(len(res)):
        list_api.append(res[i])
    for i in range(len(list_api)):
        if list_api[i][1]==name_web:
            return list_api[i][0]
    return 'no data'


#print(get_web('weather_API'))


def get_param(id_api):
    conn = sqlite3.connect('web_api.db')
    cur = conn.cursor()
    cur.execute("""SELECT parameters_api, type_parameters FROM param_api
        WHERE api_id=?;""", (str(id_api)))
    res = cur.fetchall()
    list_param=[]
    for i in range(len(res)):
        list_param.append({'param': res[i][0], 'type':res[i][1]})
        #print(res[i][0]+": "+res[i][1])

    return list_param
#a=get_param(2)
#print(a)
