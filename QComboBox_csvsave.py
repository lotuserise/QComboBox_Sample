import sys, csv,os
from PyQt4 import QtGui, QtCore
import string
import datetime
import traceback
import os.path
import sys
import logging

class Window(QtGui.QWidget):
    def __init__(self, rows, columns):
        QtGui.QWidget.__init__(self)
        self.table = QtGui.QTableWidget(rows, columns, self)

        '''
        for column in range(columns - 1):
            for row in range(rows - 1):
                self.MyCombo = QtGui.QComboBox()
                text = self.table.setCellWidget(row,column,self.MyCombo)
                combo1=self.MyCombo.addItem('test1')
                combo2=self.MyCombo.addItem('test2')
                combo3=self.MyCombo.addItem('test3')

                current1 = self.MyCombo.currentText()
                item = QtGui.QTableWidgetItem(str(current1))
                self.table.setItem(row, column,item)
                print(current1)
        '''
        self.MyCombo = QtGui.QComboBox()
        self.table.setCellWidget(0,0,self.MyCombo)
        self.MyCombo.addItem('test1')
        self.MyCombo.addItem('test2')
        current1=self.MyCombo.currentText()
        item = QtGui.QTableWidgetItem(str(current1))
        self.table.setItem(0, 0,item)
        print(current1)
        self.MyCombo.activated[str].connect(self.updatecombo)  


        self.buttonOpen = QtGui.QPushButton('Open', self)
        self.buttonSave = QtGui.QPushButton('Save', self)
        self.buttonOpen.clicked.connect(self.handleOpen)
        self.buttonSave.clicked.connect(self.handleSave)
        #self.buttonSave.clicked.connect(self.updatecombo)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.table)
        layout.addWidget(self.buttonOpen)
        layout.addWidget(self.buttonSave)

    def updatecombo(self,text):
        current2 = self.MyCombo.currentText()
        item = QtGui.QTableWidgetItem(str(current2))
        self.table.setItem(0, 0,item)
        print(current2)

    def handleSave(self):
        path = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV(*.csv)')

        writefile=open(path,'wb')
        with writefile:
            rowdata = []
            for row in range(self.table.rowCount()):
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)
                    #item = self.MyCombo.itemData(row,column)
                    if item is not None:
                        rowdata.append(item.text())
                    else:
                        rowdata.append('')
            writefile.write(str(rowdata).encode()+b'\n')

    def handleOpen(self):
        path = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '', 'CSV(*.csv)')
        #if not path.join():
        with open(str(path), 'rb') as stream:
            self.table.setRowCount(0)
            self.table.setColumnCount(0)
            for rowdata in csv.reader(stream):
                row = self.table.rowCount()
                self.table.insertRow(row)
                self.table.setColumnCount(len(rowdata))
                for column, data in enumerate(rowdata):
                    item = QtGui.QTableWidgetItem(data)
                    self.table.setItem(row, column, item)

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = Window(10, 5)
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())