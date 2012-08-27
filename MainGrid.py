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
        self.colWidthProportions = [0.06, 0.08, 0.1, 0.12, 0.17, 0.27, 0.2]
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

    def deleteRowAttachmentData(self, row):
        del self.rowAttachmentData[row]

    def resetRowAttachmentData(self):
        self.rowAttachmentData = []

    def ClearGrid(self):
        wx.grid.Grid.ClearGrid(self)
        self.resetRowAttachmentData()

    def onResize(self, event):
        event.Skip()
        self.fixWidth()

    def onDClickGrid(self, event):
        event.Skip()
        index = self.getRowAttachmentData(event.GetRow())

        if index != None:
            editDialog = EditDialog(self.GetParent())
            plant = Plants.get(index, editDialog)
            editDialog.row = event.GetRow()
            editDialog.setPlant(plant)
            editDialog.id = index
            editDialog.ShowModal()
            editDialog.Destroy()
        else:
            return None
