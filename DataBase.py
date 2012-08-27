# -*- coding: utf-8 -*-
import sqlite3
import os
import sys
import time
import wx

reload(sys)
sys.setdefaultencoding('utf-8')


class DataBase():
    def __init__(self):
        self.db = sqlite3.connect(os.path.join('.', 'db.db3'))
        self.db.isolation_level = None
        self.createTable()

    def createTable(self):
        self.db.execute("CREATE TABLE IF NOT EXISTS main.Plants (id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT,username TEXT,type TEXT,telephone TEXT,adddate INTEGER,address TEXT,info TEXT)")

    def addNew(self, plant):
        sql = 'INSERT INTO main.Plants '
        values = '", "'.join(plant.data.values())
        keys = ', '.join(plant.data.keys())
        sql = sql + '(' + keys + ') VALUES(' + '"' + values + '")'
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

    def update(self, plant, index):
        sql = 'UPDATE main.Plants SET number="%s", username="%s", address="%s", telephone="%s", type="%s", info="%s" WHERE id=%s' % (plant['number'], plant['username'], plant['address'], plant['telephone'], plant['type'], plant['info'], index)
        self.db.execute(sql)

    def delete(self, index):
        sql = 'DELETE FROM main.Plants WHERE id=%s' % (index)
        self.db.execute(sql)


class Plants():
    def __init__(self):
        self.data = {
            'number': '',
            'username': '',
            'type': '',
            'telephone': '',
            'adddate': '',
            'address': '',
            'info': ''
        }
        self.dataMeta = {
            'number': '寄养编号',
            'username': '客户名称',
            'address': '客户地址',
            'telephone': '电话号码',
            'adddate': '寄养日期',
            'type': '寄养品种',
            'info': '寄养时状况'
        }

    def __getitem__(self, key):
        value = self.data[key].strip()
        return value

    def __setitem__(self, key, value):
        value = value.strip()
        if len(value) > 0:
            self.data[key] = value
        else:
            alert = wx.MessageDialog(self.dialog, u"请你完整填写数据信息：" + self.dataMeta[key] + "！", u"数据不完整", wx.OK | wx.CENTER)
            alert.ShowModal()
            alert.Destroy()
            raise Exception()

    @staticmethod
    def getByDialog(dialog):
        plant = Plants()
        plant.dialog = dialog
        plant['number'] = dialog.txtNumber.GetValue()
        plant['username'] = dialog.txtName.GetValue()
        plant['type'] = dialog.txtType.GetValue()
        plant['telephone'] = dialog.txtPhone.GetValue()
        plant['adddate'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        plant['address'] = dialog.txtAddress.GetValue()
        plant['info'] = dialog.txtInfo.GetValue()
        return plant

    @staticmethod
    def get(index, dialog):
        dataBase = DataBase()
        cur = dataBase.fetchOne(index)
        data = cur.fetchall()
        plant = Plants()
        plant.dialog = dialog
        plant['number'] = data[0][1]
        plant['username'] = data[0][2]
        plant['type'] = data[0][3]
        plant['telephone'] = data[0][4]
        plant['adddate'] = data[0][5]
        plant['address'] = data[0][6]
        plant['info'] = data[0][7]
        return plant
