# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grafos.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2648, 1503)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(380, 100, 901, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(421, 151))
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.btnPintarGrafo = QtWidgets.QPushButton(self.centralwidget)
        self.btnPintarGrafo.setGeometry(QtCore.QRect(750, 410, 161, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPintarGrafo.sizePolicy().hasHeightForWidth())
        self.btnPintarGrafo.setSizePolicy(sizePolicy)
        self.btnPintarGrafo.setObjectName("btnPintarGrafo")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 500, 1241, 831))
        self.graphicsView.setObjectName("graphicsView")
        self.lblTtitulo = QtWidgets.QLabel(self.centralwidget)
        self.lblTtitulo.setGeometry(QtCore.QRect(590, 30, 661, 51))
        self.lblTtitulo.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 85, 255);")
        self.lblTtitulo.setObjectName("lblTtitulo")
        self.lblTtitulo_3 = QtWidgets.QLabel(self.centralwidget)
        self.lblTtitulo_3.setGeometry(QtCore.QRect(10, 220, 361, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTtitulo_3.sizePolicy().hasHeightForWidth())
        self.lblTtitulo_3.setSizePolicy(sizePolicy)
        self.lblTtitulo_3.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 85, 255);")
        self.lblTtitulo_3.setObjectName("lblTtitulo_3")
        self.lblTtitulo2 = QtWidgets.QLabel(self.centralwidget)
        self.lblTtitulo2.setGeometry(QtCore.QRect(20, 20, 181, 71))
        self.lblTtitulo2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 85, 255);")
        self.lblTtitulo2.setText("")
        self.lblTtitulo2.setPixmap(QtGui.QPixmap("logo_eafit_blanco.png"))
        self.lblTtitulo2.setObjectName("lblTtitulo2")
        self.lblTtitulo_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblTtitulo_2.setGeometry(QtCore.QRect(1490, 10, 881, 81))
        self.lblTtitulo_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 85, 255);")
        self.lblTtitulo_2.setObjectName("lblTtitulo_2")
        self.lblTtitulo_4 = QtWidgets.QLabel(self.centralwidget)
        self.lblTtitulo_4.setGeometry(QtCore.QRect(1500, 490, 891, 61))
        self.lblTtitulo_4.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 85, 255);")
        self.lblTtitulo_4.setObjectName("lblTtitulo_4")
        self.lblTtitulo_5 = QtWidgets.QLabel(self.centralwidget)
        self.lblTtitulo_5.setGeometry(QtCore.QRect(1500, 940, 881, 30))
        self.lblTtitulo_5.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 85, 255);")
        self.lblTtitulo_5.setObjectName("lblTtitulo_5")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(1490, 100, 861, 301))
        self.tableWidget_2.setRowCount(4)
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(1500, 560, 851, 300))
        self.tableWidget_3.setRowCount(4)
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_4.setGeometry(QtCore.QRect(1500, 1010, 851, 340))
        self.tableWidget_4.setRowCount(4)
        self.tableWidget_4.setColumnCount(4)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.btnGenerarAdy = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerarAdy.setGeometry(QtCore.QRect(1870, 420, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGenerarAdy.sizePolicy().hasHeightForWidth())
        self.btnGenerarAdy.setSizePolicy(sizePolicy)
        self.btnGenerarAdy.setObjectName("btnGenerarAdy")
        self.btnGenerarK2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerarK2.setGeometry(QtCore.QRect(1880, 870, 131, 40))
        self.btnGenerarK2.setObjectName("btnGenerarK2")
        self.btnGenerarK3 = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerarK3.setGeometry(QtCore.QRect(1890, 1360, 121, 50))
        self.btnGenerarK3.setObjectName("btnGenerarK3")
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(40, 1370, 131, 51))
        self.btnSalir.setObjectName("btnSalir")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2648, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnSalir.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setToolTip(_translate("MainWindow", "Haga doble clic en el cabaezado de un vértice para generar una matriz de pesos"))
        self.btnPintarGrafo.setText(_translate("MainWindow", "Dibujar Grafo"))
        self.lblTtitulo.setText(_translate("MainWindow", "Grafos por Juan Pablo Restrepo"))
        self.lblTtitulo_3.setText(_translate("MainWindow", "Matriz de Pesos>>"))
        self.lblTtitulo_2.setText(_translate("MainWindow", "Tabla de Adyacencia "))
        self.lblTtitulo_4.setText(_translate("MainWindow", "Tabla para K = 2"))
        self.lblTtitulo_5.setText(_translate("MainWindow", "Tabla para K = 3"))
        self.tableWidget_2.setToolTip(_translate("MainWindow", "Haga doble clic en el cabaezado de un vértice para generar una matriz de pesos"))
        self.tableWidget_3.setToolTip(_translate("MainWindow", "Haga doble clic en el cabaezado de un vértice para generar una matriz de pesos"))
        self.tableWidget_4.setToolTip(_translate("MainWindow", "Haga doble clic en el cabaezado de un vértice para generar una matriz de pesos"))
        self.btnGenerarAdy.setText(_translate("MainWindow", "Generar"))
        self.btnGenerarK2.setText(_translate("MainWindow", "Generar"))
        self.btnGenerarK3.setText(_translate("MainWindow", "Generar"))
        self.btnSalir.setText(_translate("MainWindow", "SALIR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
