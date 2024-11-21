import sys
import numpy as np
from PyQt5 import QtWidgets, QtGui
from grafos import Ui_MainWindow
from PyQt5.QtWidgets import QGraphicsScene

class GrafoApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(GrafoApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Usar el graphicsView existente
        self.graphicsView = self.ui.graphicsView

        # Configurar la escena del QGraphicsView
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        # Conectar botones
        self.ui.btnPintarGrafo.clicked.connect(self.dibujar_grafo)
        self.ui.btnGenerarAdy.clicked.connect(self.generar_matriz_adyacencia)
        self.ui.btnGenerarK2.clicked.connect(lambda: self.encontrar_k_trayectorias(2))
        self.ui.btnGenerarK3.clicked.connect(lambda: self.encontrar_k_trayectorias(3))

    def dibujar_grafo(self):
        matriz = self.obtener_matriz()
        self.scene.clear()
        self.dibujar_nodos_y_aristas(matriz)

    def obtener_matriz(self):
        """Obtiene la matriz de pesos"""
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
        matriz_pesos = self.obtener_matriz()
        num_nodos = len(matriz_pesos)
        matriz_adyacencia = [[1 if matriz_pesos[i][j] > 0 else 0 for j in range(num_nodos)] for i in range(num_nodos)]
        return np.array(matriz_adyacencia)

    def dibujar_nodos_y_aristas(self, matriz):
        num_nodos = len(matriz)
        radius = 20
        spacing = 100
        posiciones = []

        # Dibujar nodos
        for i in range(num_nodos):
            x = i * spacing + 50
            y = 150
            posiciones.append((x, y))
            self.scene.addEllipse(x - radius, y - radius, 2 * radius, 2 * radius,
                                  pen=QtGui.QPen(), brush=QtGui.QBrush(QtGui.QColor("lightblue")))
            self.scene.addText(f"Nodo {i+1}").setPos(x - 10, y - 10)

        # Dibujar aristas
        for i in range(num_nodos):
            for j in range(num_nodos):
                peso = matriz[i][j]
                if peso > 0:
                    x1, y1 = posiciones[i]
                    x2, y2 = posiciones[j]
                    self.scene.addLine(x1, y1, x2, y2, pen=QtGui.QPen(QtGui.QColor("black")))
                    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
                    self.scene.addText(str(peso)).setPos(mid_x, mid_y)

    def generar_matriz_adyacencia(self):
        """Genera y muestra la matriz de adyacencia"""
        matriz_adyacencia = self.obtener_matriz_adyacencia()
        num_nodos = len(matriz_adyacencia)

        self.ui.tableWidget_2.setRowCount(num_nodos)
        self.ui.tableWidget_2.setColumnCount(num_nodos)

        for i in range(num_nodos):
            for j in range(num_nodos):
                item = QtWidgets.QTableWidgetItem(str(matriz_adyacencia[i][j]))
                self.ui.tableWidget_2.setItem(i, j, item)

    def encontrar_k_trayectorias(self, k):
        """Calcula la matriz de trayectorias de longitud k"""
        matriz_adyacencia = self.obtener_matriz_adyacencia()  # Usar matriz binaria de adyacencia

        if k == 2:
            matriz_k = np.linalg.matrix_power(matriz_adyacencia, 2)  # Trayectorias acumuladas de longitud 2
            matriz_resultante = matriz_k - matriz_adyacencia  # Diferencia para obtener trayectorias exactas
        elif k == 3:
            matriz_k2 = np.linalg.matrix_power(matriz_adyacencia, 2)  # Trayectorias acumuladas de longitud 2
            matriz_k3 = np.dot(matriz_k2, matriz_adyacencia)  # Calcula trayectorias acumuladas de longitud 3
            matriz_resultante = matriz_k3 - matriz_k2  # Diferencia para obtener trayectorias exactas
        else:
            return

        # Mostrar matriz en la tabla correspondiente
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
