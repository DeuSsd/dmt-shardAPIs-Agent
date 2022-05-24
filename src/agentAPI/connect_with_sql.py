import sqlite3
conn = sqlite3.connect('web_api.db')
cur = conn.cursor()
import json

#cur.execute("""CREATE TABLE IF NOT EXISTS web_api(api_id INT PRIMARY KEY,name_api TEXT,website TEXT, title TEXT, description TEXT);""")
#cur.execute('DROP table if exists param_api')
#conn.commit()
#cur.execute('DROP table if exists param_api')
#cur.execute("""DELETE from web_api where api_id = 1""")
#conn.commit()
#conn.commit()

#cur.execute("""CREATE TABLE IF NOT EXISTS param_api(id INT PRIMARY KEY,api_id INT,parameters_api TEXT, title_param TEXT,type_parameters TEXT, description TEXT);""")
#conn.commit()
#api1 = ('1', 'weather_API', 'https://visual-crossing-weather.p.rapidapi.com/history', 'ПОГОДА','Позволяет собрать данные по погоде в разных городах')
#api_par_1=('1','1','start_time','Время начала','time','Параметр, отвечающий за начало выборки')
#api_par_2=('2','1','end_time','Время конца','time','Параметр, отвечающий за конец выборки')
#api_par_3=('3','1','location','Местность','string','Параметр, отвечающий за местность выборки')
#api2 = ('2', 'covid_API', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ','Статистика Ковид','Позволяет собрать данные по ковиду в разных городах')
#api2_par_1=('4','2','start_time','Время начала','time','Параметр, отвечающий за начало выборки')
#api2_par_2=('5','2','end_time','Время конца','time','Параметр, отвечающий за конец выборки')
#api2_par_3=('6','2','location','Местность','string','Параметр, отвечающий за местность выборки')
#cur.execute("INSERT INTO web_api VALUES(?, ?, ?,?,?);", api1)
#cur.execute("INSERT INTO param_api VALUES(?, ?, ?, ?,?,?);", api_par_1)
#cur.execute("INSERT INTO param_api VALUES(?, ?, ?, ?,?,?);", api_par_2)
#cur.execute("INSERT INTO param_api VALUES(?, ?, ?, ?,?,?);", api_par_3)
#cur.execute("INSERT INTO web_api VALUES(?, ?, ?,?,?);", api2)
#cur.execute("INSERT INTO param_api VALUES(?, ?, ?, ?,?,?);", api2_par_1)
#cur.execute("INSERT INTO param_api VALUES(?, ?, ?, ?,?,?);", api2_par_2)
#cur.execute("INSERT INTO param_api VALUES(?, ?, ?, ?,?,?);", api2_par_3)
#conn.commit()

#cur.execute('SELECT * FROM web_api')
#print(cur.fetchall())

cur.execute('SELECT * FROM param_api')
print(cur.fetchall())

def get_API():
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    list_api=[]
    cur.execute("SELECT name_api FROM backed_api_apiweb;")
    res=cur.fetchall()
    for i in range(len(res)):
        list_api.append(res[i][0])
    return list_api

def get_title(id):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute("""SELECT title_api, description FROM backed_api_apiweb
            WHERE id=?;""", (str(id)))
    res = cur.fetchall()
    #print(res)
    return res

def get_web(name_api):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    list_api = []
    cur.execute("SELECT name_api,web_api FROM backed_api_apiweb;")
    res = cur.fetchall()
    for i in range(len(res)):
        list_api.append(res[i])
    for i in range(len(list_api)):
        if list_api[i][0]==name_api:
            return list_api[i][1]
    return 'no data'

def from_web_to_api(name_web):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    list_api = []
    cur.execute("SELECT name_api,web_api FROM backed_api_apiweb;")
    res = cur.fetchall()
    for i in range(len(res)):
        list_api.append(res[i])
    for i in range(len(list_api)):
        if list_api[i][1]==name_web:
            return list_api[i][0]
    return 'no data'


def get_param(id_api):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute("""SELECT title_parameter, parameter_api, type_parameter, description_parameter FROM backed_api_parameters
        WHERE id_api_id=?;""", (str(id_api)))
    res = cur.fetchall()
    list_param=[]
    for i in range(len(res)):
        list_param.append({'title_parameter':res[i][0],'parameter': res[i][1], 'type':res[i][2],'description_parameters':res[i][3]})
        #print(res[i][0]+": "+res[i][1])

    return list_param


def get_xhost(name_api):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    list_api = []
    cur.execute("SELECT name_api,X_RapidAPI_Host FROM backed_api_apiweb;")
    res = cur.fetchall()
    for i in range(len(res)):
        list_api.append(res[i])
    for i in range(len(list_api)):
        if list_api[i][0]==name_api:
            return list_api[i][1]
    return 'no data'

def get_xkey(name_api):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    list_api = []
    cur.execute("SELECT name_api,X_RapidAPI_Key FROM backed_api_apiweb;")
    res = cur.fetchall()
    for i in range(len(res)):
        list_api.append(res[i])
    for i in range(len(list_api)):
        if list_api[i][0]==name_api:
            return list_api[i][1]
    return 'no data'

