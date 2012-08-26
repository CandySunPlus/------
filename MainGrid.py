# -*- coding: utf-8 -*-

import wx
import wx.grid
import sys
from EditDialog import EditDialog
from DataBase import Plants

reload(sys)
sys.setdefaultencoding('utf-8')

class MainGrid(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, id=-1)
        self.rowAttachmentData = []
        self.Bind(wx.EVT_SIZE, self.onResize, self)
        wx.grid.EVT_GRID_CELL_LEFT_DCLICK(self, self.onDClickGrid)

    def setColWidthProportions(self, proportions):
        self.colWidthProportions = proportions

    def fixWidth(self):
        mainWidth = self.GetParent().GetSize()[0] - self.GetRowLabelSize() - self.GetScrollLineY()
        for i in range(self.GetNumberCols()):
            cellWidth = self.colWidthProportions[i] * mainWidth
            #self.mainGrid.SetColMinimalWidth(i, cellWidth)
            self.SetColSize(i, cellWidth)
        self.Refresh()

    def setRowAttachmentData(self, row, data):
        self.rowAttachmentData.insert(row, data)

    def getRowAttachmentData(self, row):
        try:
            return self.rowAttachmentData[row]
        except Exception:
            return None

    def resetRowAttachmentData(self):
        self.rowAttachmentData = []

    def onResize(self, event):
        event.Skip()
        self.fixWidth()

    def onDClickGrid(self, event):
        event.Skip()
        index = self.getRowAttachmentData(event.GetRow())

        if index == None:
            return None
        else:
            plant = Plants.get(index)
            editDialog = EditDialog(self.GetParent())
            editDialog.setPlant(plant)
            editDialog.ShowModal()
            editDialog.Destroy()

