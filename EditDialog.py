# -*- coding: utf-8 -*-
import wx
from AddDialog import AddDialog

class EditDialog(AddDialog):
    def __init__(self, *args, **kwds):
        AddDialog.__init__(self, *args, **kwds)
        self.SetTitle(u"修改寄养条目")
        self.labelDate = wx.StaticText(self, -1, u"寄养时间：")
        self.btnDel = wx.Button(self, -1, u"删除")
        self.btnOK.SetLabel(u"修改")
        self.__do_layout()

    def __do_layout(self):
        mainSizer = self.GetSizer()
        firstItem = self.formSizer.GetItem(0)
        firstItem.SetBorder(10)
        self.formSizer.Insert(0, self.labelDate, 0, wx.TOP, 20)
        self.buttonSizer.Insert(1, self.btnDel, 0)
        mainSizer.Fit(self)
        self.Layout()

    def setPlant(self, plant):
        self.labelDate.SetLabel(u"寄养时间：" + "%s" % plant.date)
        self.txtNumber.SetValue("%s" % plant.number)
        self.txtName.SetValue("%s" % plant.username)
        self.txtAddress.SetValue("%s" % plant.address)
        self.txtPhone.SetValue("%s" % plant.telephone)
        self.txtType.SetValue("%s" % plant.type)
        self.txtInfo.SetValue("%s" % plant.info)


