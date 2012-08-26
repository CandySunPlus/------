# -*- coding: utf-8 -*-
import sqlite3
import os
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

class DataBase():
    def __init__(self):
        self.db = sqlite3.connect(os.path.join('.', 'db.db3'))
        self.db.isolation_level = None
        self.createTable()

    def createTable(self):
        self.db.execute("CREATE TABLE IF NOT EXISTS main.Plants (id INTEGER PRIMARY KEY AUTOINCREMENT, num TEXT,username TEXT,address TEXT,telephone TEXT,adddate INTEGER,type TEXT,info TEXT)")

    def addNew(self, plants):
        sql = 'INSERT INTO main.Plants (num, username, address, telephone, adddate, type, info) VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (plants.number, plants.username, plants.address, plants.telephone, plants.date, plants.type, plants.info)
        self.db.execute(sql)

    def fetchOne(self, index):
        sql = 'SELECT * FROM main.Plants WHERE id=%s' % (index)
        cur = self.db.cursor()
        cur.execute(sql)
        return cur

    def fetch(self, page=1):
        pageNum = 40
        offset = (page - 1) * pageNum
        sql = 'SELECT * FROM main.Plants limit %s,40' % (offset)
        cur = self.db.cursor()
        cur.execute(sql)
        return cur

class Plants():
    def __init__(self):
        self.number = ''
        self.username = ''
        self.address = ''
        self.telephone = ''
        self.date = ''
        self.type = ''
        self.info = ''

    @staticmethod 
    def getByDialog(addDialog):
        plant = Plants()
        plant.number = addDialog.txtNumber.GetValue()
        plant.username = addDialog.txtName.GetValue()
        plant.address = addDialog.txtAddress.GetValue()
        plant.telephone = addDialog.txtPhone.GetValue()
        plant.date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) 
        plant.type = addDialog.txtType.GetValue()
        plant.info = addDialog.txtInfo.GetValue()
        return plant

    @staticmethod
    def get(index):
        dataBase = DataBase()
        cur = dataBase.fetchOne(index)
        data = cur.fetchall()
        plant = Plants()
        plant.number = data[0][1]
        plant.username = data[0][2]
        plant.address = data[0][3]
        plant.telephone = data[0][4]
        plant.date = data[0][5]
        plant.type = data[0][6]
        plant.info = data[0][7]
        return plant

