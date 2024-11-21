import sys
import random
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
from grafos_ui import Ui_MainWindow
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsTextItem, QGraphicsItem


class Nodo(QGraphicsEllipseItem):
    def __init__(self, x, y, radius, id, app):
        super().__init__(-radius, -radius, 2 * radius, 2 * radius)
        self.setBrush(QtGui.QBrush(QtGui.QColor("lightblue")))
        self.setPen(QtGui.QPen(QtCore.Qt.black))
        self.id = id
        self.setFlag(QGraphicsEllipseItem.ItemIsMovable)
        self.setFlag(QGraphicsEllipseItem.ItemSendsGeometryChanges)
        self.text_item = QGraphicsTextItem(f"Nodo {self.id}", self)
        self.text_item.setPos(-10, -10)
        self.app = app
        self.aristas = []

    def agregar_arista(self, arista):
        self.aristas.append(arista)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            for arista in self.aristas:
                arista.actualizar_posiciones()
        return super().itemChange(change, value)


class Arista(QGraphicsLineItem):
    def __init__(self, nodo1, nodo2, peso, scene):
        super().__init__()
        self.nodo1 = nodo1
        self.nodo2 = nodo2
        self.peso = peso
        self.scene = scene
        self.text_item = QGraphicsTextItem(str(self.peso))
        self.scene.addItem(self.text_item)
        self.actualizar_posiciones()
        self.setFlag(QGraphicsLineItem.ItemIsSelectable)
        self.setPen(QtGui.QPen(QtCore.Qt.black))

    def actualizar_posiciones(self):
        x1, y1 = self.nodo1.scenePos().x(), self.nodo1.scenePos().y()
        x2, y2 = self.nodo2.scenePos().x(), self.nodo2.scenePos().y()
        self.setLine(x1, y1, x2, y2)
        self.text_item.setPos((x1 + x2) / 2, (y1 + y2) / 2)


class GrafoApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(GrafoApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene()
        self.graphicsView = self.ui.graphicsView
        self.graphicsView.setScene(self.scene)
        self.nodos = []
        self.aristas = []

        # Conectar botones
        self.ui.btnPintarGrafo.clicked.connect(self.dibujar_grafo)
        self.ui.btnGenerarAdy.clicked.connect(self.generar_matriz_adyacencia)
        self.ui.btnGenerarK2.clicked.connect(lambda: self.calcular_k_trayectorias(2))
        self.ui.btnGenerarK3.clicked.connect(lambda: self.calcular_k_trayectorias(3))
        self.ui.tableWidget.horizontalHeader().sectionClicked.connect(self.llenar_matriz_aleatoria)

    def dibujar_grafo(self):
        self.scene.clear()
        self.nodos.clear()
        self.aristas.clear()
        matriz = self.obtener_matriz()
        self.dibujar_nodos_y_aristas(matriz)

    def obtener_matriz(self):
        """Obtiene la matriz de pesos desde la interfaz."""
        filas = self.ui.tableWidget.rowCount()
        columnas = self.ui.tableWidget.columnCount()
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                item = self.ui.tableWidget.item(i, j)
                valor = int(item.text()) if item and item.text().isdigit() else 0
                fila.append(valor)
            matriz.append(fila)
        return matriz

    def obtener_matriz_adyacencia(self):
        """Convierte la matriz de pesos en una matriz binaria de adyacencia."""
        matriz_pesos = self.obtener_matriz()
        num_nodos = len(matriz_pesos)
        matriz_adyacencia = [[1 if matriz_pesos[i][j] > 0 else 0 for j in range(num_nodos)] for i in range(num_nodos)]
        return np.array(matriz_adyacencia)

    def dibujar_nodos_y_aristas(self, matriz):
        num_nodos = len(matriz)
        radius = 20
        width = self.graphicsView.width() - 100
        height = self.graphicsView.height() - 100
        for i in range(num_nodos):
            x, y = random.randint(50, width), random.randint(50, height)
            nodo = Nodo(x, y, radius, i + 1, self)
            nodo.setPos(x, y)
            self.scene.addItem(nodo)
            self.nodos.append(nodo)
        for i in range(num_nodos):
            for j in range(num_nodos):
                peso = matriz[i][j]
                if peso > 0:
                    nodo1, nodo2 = self.nodos[i], self.nodos[j]
                    arista = Arista(nodo1, nodo2, peso, self.scene)
                    self.aristas.append(arista)
                    self.scene.addItem(arista)
                    nodo1.agregar_arista(arista)
                    nodo2.agregar_arista(arista)

    def llenar_matriz_aleatoria(self, index):
        filas = self.ui.tableWidget.rowCount()
        columnas = self.ui.tableWidget.columnCount()
        for i in range(filas):
            for j in range(columnas):
                if i == j:
                    self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem('0'))
                else:
                    valor_aleatorio = random.randint(1, 100)
                    self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(valor_aleatorio)))

    def generar_matriz_adyacencia(self):
        """Genera y muestra la matriz de adyacencia binaria."""
        matriz_adyacencia = self.obtener_matriz_adyacencia()
        num_nodos = len(matriz_adyacencia)

        self.ui.tableWidget_2.setRowCount(num_nodos)
        self.ui.tableWidget_2.setColumnCount(num_nodos)

        for i in range(num_nodos):
            for j in range(num_nodos):
                self.ui.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(matriz_adyacencia[i][j])))

    def calcular_k_trayectorias(self, k):
        """Calcula las trayectorias de longitud k usando la matriz de adyacencia binaria."""
        matriz_adyacencia = self.obtener_matriz_adyacencia()

        if k == 2:
            matriz_k = np.linalg.matrix_power(matriz_adyacencia, 2) 
            matriz_resultante = matriz_k - matriz_adyacencia  
        elif k == 3:
            matriz_k2 = np.linalg.matrix_power(matriz_adyacencia, 2) 
            matriz_k3 = np.dot(matriz_k2, matriz_adyacencia) 
            matriz_resultante = matriz_k3 - matriz_k2  
        else:
            return

        tabla = self.ui.tableWidget_3 if k == 2 else self.ui.tableWidget_4
        num_nodos = len(matriz_resultante)
        tabla.setRowCount(num_nodos)
        tabla.setColumnCount(num_nodos)

        for i in range(num_nodos):
            for j in range(num_nodos):
                tabla.setItem(i, j, QtWidgets.QTableWidgetItem(str(max(0, matriz_resultante[i][j]))))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GrafoApp()
    window.show()
    sys.exit(app.exec_())
