# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'programa4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtCore import Qt
import random
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.Qt import Qt
import keyboard
from bcp import *
from PyQt5.QtCore import QTimer, Qt

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(1518, 713)
        widget.setStyleSheet("QWidget#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0.124, y1:0.153409, x2:1, y2:1, stop:0 rgba(29, 60, 195, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.label = QtWidgets.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(460, 10, 571, 40))
        self.label.setStyleSheet("font: 20pt \"Bahnschrift\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(widget)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 221, 31))
        self.label_2.setStyleSheet("font: 14pt \"Palatino Linotype\";")
        self.label_2.setObjectName("label_2")
        self.proces = QtWidgets.QLineEdit(widget)
        self.proces.setGeometry(QtCore.QRect(290, 110, 91, 31))
        self.proces.setStyleSheet("font: 14pt \"Palatino Linotype\";")
        self.proces.setText("")
        self.proces.setObjectName("proces")
        self.iniciar = QtWidgets.QPushButton(widget)
        self.iniciar.setGeometry(QtCore.QRect(60, 210, 321, 31))
        self.iniciar.setStyleSheet("font: 14pt \"Palatino Linotype\";")
        self.iniciar.setObjectName("iniciar")
        self.iniciar.clicked.connect(self.pedirProcesos)
        self.iniciar.clicked.connect(self.inicio)
        self.iniciar.clicked.connect(self.start_stop_func)
        
        
        self.label_3 = QtWidgets.QLabel(widget)
        self.label_3.setGeometry(QtCore.QRect(60, 340, 177, 31))
        self.label_3.setStyleSheet("font: 14pt \"Palatino Linotype\";")
        self.label_3.setObjectName("label_3")
        self.Nuevos = QtWidgets.QLabel(widget)
        self.Nuevos.setGeometry(QtCore.QRect(250, 340, 131, 31))
        self.Nuevos.setStyleSheet("font: 14pt \"Palatino Linotype\";\n"
"background-color: rgb(255, 255, 255);")
        self.Nuevos.setText("")
        self.Nuevos.setObjectName("Nuevos")
        self.label_4 = QtWidgets.QLabel(widget)
        self.label_4.setGeometry(QtCore.QRect(150, 420, 137, 31))
        self.label_4.setStyleSheet("font: 14pt \"Palatino Linotype\";")
        self.label_4.setObjectName("label_4")
        self.tablaListos = QtWidgets.QTableWidget(widget)
        self.tablaListos.setGeometry(QtCore.QRect(10, 460, 411, 231))
        self.tablaListos.setStyleSheet("font: 10pt \"Palatino Linotype\";")
        self.tablaListos.setObjectName("tablaListos")
        self.tablaListos.setColumnCount(3)
        self.tablaListos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaListos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaListos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaListos.setHorizontalHeaderItem(2, item)
        self.label_5 = QtWidgets.QLabel(widget)
        self.label_5.setGeometry(QtCore.QRect(650, 80, 215, 31))
        self.label_5.setStyleSheet("font: 14pt \"Palatino Linotype\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(widget)
        self.label_6.setGeometry(QtCore.QRect(560, 140, 244, 27))
        self.label_6.setStyleSheet("font: 12pt \"Palatino Linotype\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(widget)
        self.label_7.setGeometry(QtCore.QRect(620, 180, 187, 27))
        self.label_7.setStyleSheet("font: 12pt \"Palatino Linotype\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(widget)
        self.label_8.setGeometry(QtCore.QRect(570, 220, 239, 27))
        self.label_8.setStyleSheet("font: 12pt \"Palatino Linotype\";")
        self.label_8.setObjectName("label_8")
        self.ID = QtWidgets.QLabel(widget)
        self.ID.setGeometry(QtCore.QRect(820, 140, 121, 31))
        self.ID.setStyleSheet("font: 14pt \"Palatino Linotype\";\n"
"background-color: rgb(255, 255, 255);")
        self.ID.setText("")
        self.ID.setObjectName("ID")
        self.oper = QtWidgets.QLabel(widget)
        self.oper.setGeometry(QtCore.QRect(820, 180, 121, 31))
        self.oper.setStyleSheet("font: 14pt \"Palatino Linotype\";\n"
"background-color: rgb(255, 255, 255);")
        self.oper.setText("")
        self.oper.setObjectName("oper")
        self.label_9 = QtWidgets.QLabel(widget)
        self.label_9.setGeometry(QtCore.QRect(620, 260, 191, 27))
        self.label_9.setStyleSheet("font: 12pt \"Palatino Linotype\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(widget)
        self.label_10.setGeometry(QtCore.QRect(660, 300, 151, 27))
        self.label_10.setStyleSheet("font: 12pt \"Palatino Linotype\";")
        self.label_10.setObjectName("label_10")
        self.tme = QtWidgets.QLabel(widget)
        self.tme.setGeometry(QtCore.QRect(820, 220, 121, 31))
        self.tme.setStyleSheet("font: 14pt \"Palatino Linotype\";\n"
"background-color: rgb(255, 255, 255);")
        self.tme.setText("")
        self.tme.setObjectName("tme")
        self.tt = QtWidgets.QLabel(widget)
        self.tt.setGeometry(QtCore.QRect(820, 260, 121, 31))
        self.tt.setStyleSheet("font: 14pt \"Palatino Linotype\";\n"
"background-color: rgb(255, 255, 255);")
        self.tt.setText("")
        self.tt.setObjectName("tt")
        self.tr = QtWidgets.QLabel(widget)
        self.tr.setGeometry(QtCore.QRect(820, 300, 121, 31))
        self.tr.setStyleSheet("font: 14pt \"Palatino Linotype\";\n"
"background-color: rgb(255, 255, 255);")
        self.tr.setText("")
        self.tr.setObjectName("tr")
        self.label_11 = QtWidgets.QLabel(widget)
        self.label_11.setGeometry(QtCore.QRect(640, 420, 217, 31))
        self.label_11.setStyleSheet("font: 14pt \"Palatino Linotype\";")
        self.label_11.setObjectName("label_11")
        self.bloqueados = QtWidgets.QTableWidget(widget)
        self.bloqueados.setGeometry(QtCore.QRect(590, 460, 311, 231))
        self.bloqueados.setStyleSheet("font: 10pt \"Palatino Linotype\";")
        self.bloqueados.setObjectName("bloqueados")
        self.bloqueados.setColumnCount(2)
        self.bloqueados.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.bloqueados.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bloqueados.setHorizontalHeaderItem(1, item)
        self.label_12 = QtWidgets.QLabel(widget)
        self.label_12.setGeometry(QtCore.QRect(1170, 80, 215, 31))
        self.label_12.setStyleSheet("font: 14pt \"Palatino Linotype\";")
        self.label_12.setObjectName("label_12")
        self.Terminados = QtWidgets.QTableWidget(widget)
        self.Terminados.setGeometry(QtCore.QRect(1050, 140, 421, 441))
        self.Terminados.setStyleSheet("font: 10pt \"Palatino Linotype\";")
        self.Terminados.setObjectName("Terminados")
        self.Terminados.setColumnCount(3)
        self.Terminados.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Terminados.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Terminados.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Terminados.setHorizontalHeaderItem(2, item)
        self.label_13 = QtWidgets.QLabel(widget)
        self.label_13.setGeometry(QtCore.QRect(1180, 630, 57, 31))
        self.label_13.setStyleSheet("font: 14pt \"Palatino Linotype\";")
        self.label_13.setObjectName("label_13")
        self.reloj = QtWidgets.QLabel(widget)
        self.reloj.setGeometry(QtCore.QRect(1250, 630, 101, 31))
        self.reloj.setStyleSheet("font: 14pt \"Palatino Linotype\";\n"
"background-color: rgb(255, 255, 255);")
        self.reloj.setText("")
        self.reloj.setObjectName("reloj")
        self.quant = QtWidgets.QLineEdit(widget)
        self.quant.setGeometry(QtCore.QRect(290, 160, 91, 31))
        self.quant.setStyleSheet("font: 14pt \"Palatino Linotype\";")
        self.quant.setText("")
        self.quant.setObjectName("quant")
        self.label_14 = QtWidgets.QLabel(widget)
        self.label_14.setGeometry(QtCore.QRect(170, 160, 111, 31))
        self.label_14.setStyleSheet("font: 14pt \"Palatino Linotype\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(widget)
        self.label_15.setGeometry(QtCore.QRect(720, 340, 91, 27))
        self.label_15.setStyleSheet("font: 12pt \"Palatino Linotype\";")
        self.label_15.setObjectName("label_15")
        self.quantLab = QtWidgets.QLabel(widget)
        self.quantLab.setGeometry(QtCore.QRect(820, 340, 121, 31))
        self.quantLab.setStyleSheet("font: 14pt \"Palatino Linotype\";\n"
"background-color: rgb(255, 255, 255);")
        self.quantLab.setText("")
        self.quantLab.setObjectName("quantLab")
        self.valorQuant = QtWidgets.QLabel(widget)
        self.valorQuant.setGeometry(QtCore.QRect(250, 280, 131, 31))
        self.valorQuant.setStyleSheet("font: 14pt \"Palatino Linotype\";\n"
"background-color: rgb(255, 255, 255);")
        self.valorQuant.setText("")
        self.valorQuant.setObjectName("valorQuant")
        self.label_16 = QtWidgets.QLabel(widget)
        self.label_16.setGeometry(QtCore.QRect(36, 280, 201, 31))
        self.label_16.setStyleSheet("font: 14pt \"Palatino Linotype\";")
        self.label_16.setObjectName("label_16")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.label.setText(_translate("widget", "Algoritmo de Planificación RR (Round-Robin)"))
        self.label_2.setText(_translate("widget", "Número de procesos:"))
        self.iniciar.setText(_translate("widget", "Iniciar"))
        self.label_3.setText(_translate("widget", "Procesos nuevos:"))
        self.label_4.setText(_translate("widget", "Cola de listos"))
        item = self.tablaListos.horizontalHeaderItem(0)
        item.setText(_translate("widget", "ID"))
        item = self.tablaListos.horizontalHeaderItem(1)
        item.setText(_translate("widget", "TME"))
        item = self.tablaListos.horizontalHeaderItem(2)
        item.setText(_translate("widget", "TT"))
        self.label_5.setText(_translate("widget", "Proceso en ejecución"))
        self.label_6.setText(_translate("widget", "Número de programa (ID):"))
        self.label_7.setText(_translate("widget", "Operación a realizar:"))
        self.label_8.setText(_translate("widget", "Tiempo maximo estimado:"))
        self.label_9.setText(_translate("widget", "Tiempo transcurrido:"))
        self.label_10.setText(_translate("widget", "Tiempo restante:"))
        self.label_11.setText(_translate("widget", "Procesos Bloqueados"))
        item = self.bloqueados.horizontalHeaderItem(0)
        item.setText(_translate("widget", "ID"))
        item = self.bloqueados.horizontalHeaderItem(1)
        item.setText(_translate("widget", "TT"))
        self.label_12.setText(_translate("widget", "Procesos terminados"))
        item = self.Terminados.horizontalHeaderItem(0)
        item.setText(_translate("widget", "ID"))
        item = self.Terminados.horizontalHeaderItem(1)
        item.setText(_translate("widget", "Operación"))
        item = self.Terminados.horizontalHeaderItem(2)
        item.setText(_translate("widget", "Resultado"))
        self.label_13.setText(_translate("widget", "Reloj:"))
        self.label_14.setText(_translate("widget", "Quantum:"))
        self.label_15.setText(_translate("widget", "Quantum:"))
        self.label_16.setText(_translate("widget", "Valor del Quantum:"))

    def __init__(self):
        self.step = 0                                           # 2
 
        self.timer = QTimer(self)                               # 3
        self.timer.timeout.connect(self.ejecucion)
        
    
    def start_stop_func(self):                      
        if not self.timer.isActive():
            self.timer.start(1000)
        else:
            self.timer.stop()
    
    
    #Bandera para las entradas 1 = Interrupcion, 2 = Error, 3 = Pausa, 4=Continuar
    bandera = 0
    
    #Contador para el proceso que esta en ejecución
    contPros = 0
    
    #Contador para los procesos terminados
    contTerminados = 1
    terminados = []
    
    #Contador Global
    contadorGlobal = -1
    otraLista = []
    lisd = []
    cont = 1
    
    listaAux = []
    
    #Lista para procesos bloqueados
    prosBloq = []
    
    ids = 1
    
    terminador = 0
    
    #Lista que guardara los prosesos
    listaLotes = []
    
    quantum = 0
    quantum2 = 1
        
    def pedirProcesos(self):
        try:
            proses = int(self.proces.text())
            self.quantum = int(self.quant.text())
            _translate = QtCore.QCoreApplication.translate
            self.proces.setText(_translate("Dialog", ""))
            self.quant.setText(_translate("Dialog", ""))
            
        except ValueError:
            print("El valor ingresado no es un número, vuelva a ingresar")
        
        #contador para el while
        contador = 0
        
        #Variables necesarias para el ingreso de datos
        tme = 0
        oper = 0
        
        _translate = QtCore.QCoreApplication.translate
        self.valorQuant.setText(_translate("Dialog", str(self.quantum)))
        
        while contador < proses:
            lista = []    #[numero de cada proceso, tiempo maximo estimado, tiempo transcurrido, operacion, resultado, llegada, respuesta, banderalle, estado, fin, TRet, tEspera, tRestante]
                          #     0                             1                      2               3            4       5          6          7         8     9,    10     11        12
            
            #Numero de cada proceso
            lista.append(self.ids)
            self.ids += 1
            
            #Tiempo maximo estimado
            tme = random.randint(6, 16)
            lista.append(tme)
            
            #Tiempo transcurrido
            lista.append(0)
            
            #Operaciones y resultado
            oper = random.randint(1, 5)
            if oper == 1:
                num1 = random.randint(0, 1000)
                num2 = random.randint(0, 1000)
                operacion = str(num1) + "+" + str(num2)
                resultado = num1 + num2
            elif oper == 2:
                 num1 = random.randint(0, 1000)
                 num2 = random.randint(0, 1000)
                 operacion = str(num1) + "-" + str(num2)
                 resultado = num1 - num2
            elif oper == 3:
                num1 = random.randint(-1000, 1000)
                num2 = random.randint(-1000, 1000)
                operacion = str(num1) + "*" + str(num2)
                resultado = num1 * num2
            elif oper == 4:
                while True:
                    num1 = random.randint(-1000, 1000)
                    num2 = random.randint(-1000, 1000)
                    if num2 != 0:    
                        operacion = str(num1) + "/" + str(num2)
                        resultado = round(num1 / num2, 2)
                        break
            elif oper == 5:
                while True:
                    num1 = random.randint(-1000, 1000)
                    num2 = random.randint(-1000, 1000)
                    if num2 != 0:    
                        operacion = str(num1) + "%" + str(num2)
                        resultado = num1 % num2
                        break
                    
            lista.append(operacion)
            lista.append(resultado)
            
            lista.append(0)
            lista.append(0)
            lista.append(0)
            lista.append("Nuevo")
            lista.append(" ")
            lista.append(" ")
            lista.append(" ")
            lista.append(tme)
            
            #Agregar el trabajo a la lista de lotes
            self.listaLotes.append(lista)
            #print(self.listaLotes)
            
            contador += 1
        
        self.otraLista = self.listaLotes[0:]
        
        fin = 0
        try:
            while fin < 5:
                self.listaAux.append(self.otraLista.pop(0))
                fin += 1
        except IndexError:
            for x in range(len(self.otraLista)):
                self.listaAux.append(self.otraLista.pop(0))
            
        
    def terminadoProceso(self):
        #Terminado de un proceso
        if self.lisd == [] and len(self.listaAux) > 0:
            self.quantum2 = 1
            self.lisd = self.listaAux.pop(0)
            try:
                if self.lisd[7] == 0:
                    self.lisd[7] = 1
                    self.lisd[6] = self.contadorGlobal
                    print(self.lisd)
            except IndexError:
                pass
            
        try:
            if self.lisd[2] != 0:
                self.cont = self.lisd[2] + 1
            else:
                self.cont = 1
        except IndexError:
            pass
        self.terminador = 1
        
        if len(self.listaLotes) == self.contPros:
            self.bcp=QtWidgets.QDialog()
            self.ui=Ui_Form()
            self.ui.setupUi(self.bcp)
            self.bcp.show()
            cuenta = 0
            
            self.ui.BCP.setRowCount(len(self.terminados))
            for i in self.terminados:
                self.ui.BCP.setItem(cuenta, 0, QtWidgets.QTableWidgetItem(str(i[0])))
                self.ui.BCP.setItem(cuenta, 1, QtWidgets.QTableWidgetItem(str(i[1])))
                self.ui.BCP.setItem(cuenta, 2, QtWidgets.QTableWidgetItem(str(i[2])))
                self.ui.BCP.setItem(cuenta, 3, QtWidgets.QTableWidgetItem(str(i[3])))
                self.ui.BCP.setItem(cuenta, 4, QtWidgets.QTableWidgetItem(str(i[4])))
                self.ui.BCP.setItem(cuenta, 5, QtWidgets.QTableWidgetItem(str(i[5])))
                self.ui.BCP.setItem(cuenta, 6, QtWidgets.QTableWidgetItem(str(i[6])))
                self.ui.BCP.setItem(cuenta, 7, QtWidgets.QTableWidgetItem(str(i[7])))
                self.ui.BCP.setItem(cuenta, 8, QtWidgets.QTableWidgetItem(str(i[8])))
                self.ui.BCP.setItem(cuenta, 9, QtWidgets.QTableWidgetItem(str(i[9])))
                self.ui.BCP.setItem(cuenta, 10, QtWidgets.QTableWidgetItem(str(i[10])))
                self.ui.BCP.setItem(cuenta, 11, QtWidgets.QTableWidgetItem(str(i[11])))
                cuenta += 1
            self.start_stop_func()
    
    def inicio(self):
        #Terminado de un proceso
        try:
            if self.lisd[2] != 0:
                self.cont = self.lisd[2]
            else:
                self.cont = 1
        except IndexError:
            pass
        self.terminador = 1
        
    def ejecucion(self):
        _translate = QtCore.QCoreApplication.translate
        self.step += 1
        if self.bandera == 3:
            self.bandera = 0
            self.start_stop_func()
            
        for p in self.prosBloq:
            if p[12] == 8:
                p.pop(8)
                self.listaAux.append(p)
                for n in self.prosBloq:
                    if n[0] == p[0]:
                        self.prosBloq.remove(n)
                
        trabajos = len(self.otraLista)
        self.Nuevos.setText(_translate("widget", str(trabajos)))
        
        #Lote trabajando
        cuenta = 0
        self.tablaListos.setRowCount(len(self.listaAux))
        for i in self.listaAux:
            self.tablaListos.setItem(cuenta, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tablaListos.setItem(cuenta, 1, QtWidgets.QTableWidgetItem(str(i[1])))
            self.tablaListos.setItem(cuenta, 2, QtWidgets.QTableWidgetItem(str(i[2])))
            cuenta += 1
         
        try:
            self.terminador = self.lisd[1]
            self.ID.setText(_translate("widget", str(self.lisd[0])))
            self.oper.setText(_translate("widget", str(self.lisd[3])))
            self.tme.setText(_translate("widget", str(self.lisd[1])))
            self.tt.setText(_translate("widget", str(self.cont)))
            self.tr.setText(_translate("widget", str(self.lisd[1] - self.cont)))
            self.quantLab.setText(_translate("widget", str(self.quantum2)))
            
            self.contadorGlobal += 1
            if self.cont == self.lisd[1]:
                self.lisd[2] = self.cont
                self.contPros += 1
                #self.contadorGlobal -= 1
        except IndexError:
            self.ID.setText(_translate("widget", ""))
            self.oper.setText(_translate("widget", ""))
            self.tme.setText(_translate("widget", ""))
            self.tt.setText(_translate("widget", ""))
            self.tr.setText(_translate("widget", ""))
            self.quantLab.setText(_translate("widget", ""))
            self.contadorGlobal += 1
            
        #Prosesos terminados
        if self.contPros == self.contTerminados:
            self.quantum2 = 1
            lista = []
            lista.append(self.lisd[0])  #ID
            lista.append(self.lisd[3])  #oper
            lista.append(self.lisd[4])  #res
            lista.append('Terminado')  #estado
            lista.append(self.lisd[1])  #TME
            lista.append(self.lisd[5])  #llegada
            lista.append(self.contadorGlobal)  #Finalizado
            lista.append(lista[6] - lista[5]) #retorno
            lista.append(self.lisd[6] - lista[5])  #respuesta
            lista.append(self.cont) #servicio
            lista.append(lista[7]-lista[9]) #Espera
            lista.append(lista[4]-lista[9]) #restante
            
            self.terminados.append(lista)
            try:
                self.lisd = self.listaAux.pop(0)
                if self.lisd[7] == 0:
                    self.lisd[7] = 1
                    self.lisd[6] = self.contadorGlobal
                    #print(self.lisd)
            except IndexError:
                pass
            try:
                nuevalis = self.otraLista.pop(0)
                nuevalis[5] = self.contadorGlobal
                self.listaAux.append(nuevalis)
            except IndexError:
                pass
            
            self.contTerminados += 1
        elif self.quantum == self.quantum2:
            try:
                listaAgrega = []
                self.lisd[2] = self.cont
                self.quantum2 = 1
                listaAgrega.append(self.lisd[0])
                listaAgrega.append(self.lisd[1])
                listaAgrega.append(self.lisd[2])
                listaAgrega.append(self.lisd[3])
                listaAgrega.append(self.lisd[4])
                listaAgrega.append(self.lisd[5])
                listaAgrega.append(self.lisd[6])
                listaAgrega.append(self.lisd[7])
                listaAgrega.append(self.lisd[8])
                listaAgrega.append(self.lisd[9])
                listaAgrega.append(self.lisd[10])
                listaAgrega.append(self.lisd[11])
                self.listaAux.append(listaAgrega)  
                self.lisd = []
                self.terminadoProceso()
            except IndexError:
                pass
        else:
            self.quantum2 += 1
        
        
        if self.bandera == 4:
            self.bandera = 0
            lista = []    #[numero de cada proceso, tiempo maximo estimado, tiempo transcurrido, operacion, resultado, llegada, respuesta, banderalle]
                          #     0                             1                      2               3            4       5          6          7
            #Numero de cada proceso
            lista.append(self.ids)
            self.ids += 1
            
            #Tiempo maximo estimado
            tme = random.randint(6, 16)
            lista.append(tme)
            
            #Tiempo transcurrido
            lista.append(0)
            
            #Operaciones y resultado
            oper = random.randint(1, 5)
            if oper == 1:
                num1 = random.randint(0, 1000)
                num2 = random.randint(0, 1000)
                operacion = str(num1) + "+" + str(num2)
                resultado = num1 + num2
            elif oper == 2:
                 num1 = random.randint(0, 1000)
                 num2 = random.randint(0, 1000)
                 operacion = str(num1) + "-" + str(num2)
                 resultado = num1 - num2
            elif oper == 3:
                num1 = random.randint(-1000, 1000)
                num2 = random.randint(-1000, 1000)
                operacion = str(num1) + "*" + str(num2)
                resultado = num1 * num2
            elif oper == 4:
                while True:
                    num1 = random.randint(-1000, 1000)
                    num2 = random.randint(-1000, 1000)
                    if num2 != 0:    
                        operacion = str(num1) + "/" + str(num2)
                        resultado = round(num1 / num2, 2)
                        break
            elif oper == 5:
                while True:
                    num1 = random.randint(-1000, 1000)
                    num2 = random.randint(-1000, 1000)
                    if num2 != 0:    
                        operacion = str(num1) + "%" + str(num2)
                        resultado = num1 % num2
                        break
                    
            lista.append(operacion)
            lista.append(resultado)
            
            lista.append(0)
            lista.append(0)
            lista.append(0)
            lista.append("Nuevo")
            lista.append(" ")
            lista.append(" ")
            lista.append(" ")
            lista.append(tme)
        
            #Agregar el trabajo a la lista de lotes
            if self.lisd == []:
                var = len(self.listaAux) + len(self.prosBloq)
            else:
                var = len(self.listaAux) + len(self.prosBloq) + 1
            #print(var)
            if var < 5:
                lista[5] = self.contadorGlobal
                self.listaAux.append(lista)
                self.listaLotes.append(lista)
            else:
                self.otraLista.append(lista)
                self.listaLotes.append(lista)
        elif self.bandera == 5: #Tabla bcp
            self.bandera = 0
            self.bcp=QtWidgets.QDialog()
            self.ui=Ui_Form()
            self.ui.setupUi(self.bcp)
            self.bcp.show()
            cuenta = 0
            #Terminados en BCP
            listaBcp = self.terminados[0:]
            for i in self.otraLista:
                #Nuevos en BCP
                listo = []
                listo.append(i[0])
                listo.append(i[3])
                listo.append("Null")
                listo.append("Nuevo")
                listo.append(i[1])
                listo.append("Null")
                listo.append("Null")
                listo.append("Null")
                listo.append("Null")
                listo.append("Null")
                listo.append("Null")
                listo.append(i[12])
                listaBcp.append(listo)
            #Listos en bcp
            for i in self.listaAux:
                listo = []
                listo.append(i[0])
                listo.append(i[3])
                listo.append("Null")
                listo.append("Listo")
                listo.append(i[1])
                listo.append(i[5])
                listo.append("Null")
                listo.append("Null")
                if i[7] == 0:
                    listo.append("Null")
                elif i[7] == 1:
                    listo.append(i[6] - listo[5])
                listo.append(i[2])
                listo.append((self.contadorGlobal - i[5]) - i[2])
                listo.append(listo[4] - listo[9])
                listaBcp.append(listo)
            #Bloqueados en bcp
            for i in self.prosBloq:
                listo = []
                listo.append(i[0])
                listo.append(i[3])
                listo.append("Null")
                listo.append("Bloqueado, rest: " + str((8 - i[12]) - 1))
                listo.append(i[1])
                listo.append(i[5])
                listo.append("Null")
                listo.append("Null")
                listo.append(i[6] - listo[5])
                listo.append(i[2])
                listo.append((self.contadorGlobal - i[5]) - i[2])
                listo.append(listo[4] - listo[9])
                listaBcp.append(listo)
            #Ejecucion en bcp
            try:
                listo = []
                listo.append(self.lisd[0])
                listo.append(self.lisd[3])
                listo.append("Null")
                listo.append("Ejecución")
                listo.append(self.lisd[1])
                listo.append(self.lisd[5])
                listo.append("Null")
                listo.append("Null")
                listo.append(self.lisd[6] - listo[5])
                listo.append(self.cont)
                listo.append((self.contadorGlobal - self.lisd[5]) - self.cont)
                listo.append(listo[4] - listo[9])
                listaBcp.append(listo)
            except IndexError:
                pass
                
                
            self.ui.BCP.setRowCount(len(listaBcp))
            for i in listaBcp:
                self.ui.BCP.setItem(cuenta, 0, QtWidgets.QTableWidgetItem(str(i[0])))
                self.ui.BCP.setItem(cuenta, 1, QtWidgets.QTableWidgetItem(str(i[1])))
                self.ui.BCP.setItem(cuenta, 2, QtWidgets.QTableWidgetItem(str(i[2])))
                self.ui.BCP.setItem(cuenta, 3, QtWidgets.QTableWidgetItem(str(i[3])))
                self.ui.BCP.setItem(cuenta, 4, QtWidgets.QTableWidgetItem(str(i[4])))
                self.ui.BCP.setItem(cuenta, 5, QtWidgets.QTableWidgetItem(str(i[5])))
                self.ui.BCP.setItem(cuenta, 6, QtWidgets.QTableWidgetItem(str(i[6])))
                self.ui.BCP.setItem(cuenta, 7, QtWidgets.QTableWidgetItem(str(i[7])))
                self.ui.BCP.setItem(cuenta, 8, QtWidgets.QTableWidgetItem(str(i[8])))
                self.ui.BCP.setItem(cuenta, 9, QtWidgets.QTableWidgetItem(str(i[9])))
                self.ui.BCP.setItem(cuenta, 10, QtWidgets.QTableWidgetItem(str(i[10])))
                self.ui.BCP.setItem(cuenta, 11, QtWidgets.QTableWidgetItem(str(i[11])))
                cuenta += 1
                
            self.start_stop_func()
        
        if self.bandera == 2: #Error
            self.bandera = 0
            self.quantum2 = 1
            lista = []
            print(self.lisd)
            lista.append(self.lisd[0])  #ID
            lista.append(self.lisd[3])  #oper
            lista.append('ERROR')  #res
            lista.append('Terminado E')  #estado
            lista.append(self.lisd[1])  #TME
            lista.append(self.lisd[5])  #llegada
            lista.append(self.contadorGlobal)  #Finalizado
            lista.append(lista[6] - lista[5]) #retorno
            lista.append(self.lisd[6] - lista[5])  #respuesta
            lista.append(self.cont)  #servicio
            lista.append(lista[7]-lista[9]) #espera
            lista.append(lista[4]-lista[9]) #restante
            
            self.terminados.append(lista)
            self.contPros += 1
            self.contTerminados += 1
            
            #Imprimir procesos terminados
            cuenta = 0
            self.Terminados.setRowCount(len(self.terminados))
            for i in self.terminados:
                self.Terminados.setItem(cuenta, 0, QtWidgets.QTableWidgetItem(str(i[0])))
                self.Terminados.setItem(cuenta, 1, QtWidgets.QTableWidgetItem(str(i[1] + " =")))
                self.Terminados.setItem(cuenta, 2, QtWidgets.QTableWidgetItem(str(i[2])))
                cuenta += 1
            
            #self.contadorGlobal -= 1
            #Imprimir Contador Global
            self.reloj.setText(_translate("widget", str(self.contadorGlobal)))
            
            # try:
            #     self.lisd = self.listaAux.pop(0)
            #     if self.lisd[7] == 0:
            #         self.lisd[7] = 1
            #         self.lisd[6] = self.contadorGlobal
            #         print(self.lisd)
            # except IndexError:
            #     pass
            try:
                nuevalis = self.otraLista.pop(0)
                nuevalis[5] = self.contadorGlobal
                self.listaAux.append(nuevalis)
            except IndexError:
                pass
            self.lisd = []
            self.terminadoProceso()
        else:
            #Imprimir procesos terminados
            cuenta = 0
            self.Terminados.setRowCount(len(self.terminados))
            for i in self.terminados:
                self.Terminados.setItem(cuenta, 0, QtWidgets.QTableWidgetItem(str(i[0])))
                self.Terminados.setItem(cuenta, 1, QtWidgets.QTableWidgetItem(str(i[1] + "=")))
                self.Terminados.setItem(cuenta, 2, QtWidgets.QTableWidgetItem(str(i[2])))
                cuenta += 1
            
            #Imprimir Contador Global
            if self.contadorGlobal >= 0:
                self.reloj.setText(_translate("widget", str(self.contadorGlobal)))
                    
            for p in self.prosBloq:
                p[12] += 1
                
            #Imprimir procesos bloqueados
            cuenta = 0
            self.bloqueados.setRowCount(len(self.prosBloq))
            for i in self.prosBloq:
                self.bloqueados.setItem(cuenta, 0, QtWidgets.QTableWidgetItem(str(i[0])))
                self.bloqueados.setItem(cuenta, 1, QtWidgets.QTableWidgetItem(str(i[12])))
                cuenta += 1
            
            if self.bandera == 1: #Interrupcion
                try:
                    self.lisd[2] = self.cont
                    listaAgrega = []
                    listaAgrega.append(self.lisd[0])
                    listaAgrega.append(self.lisd[1])
                    listaAgrega.append(self.lisd[2])
                    listaAgrega.append(self.lisd[3])
                    listaAgrega.append(self.lisd[4])
                    listaAgrega.append(self.lisd[5])
                    listaAgrega.append(self.lisd[6])
                    listaAgrega.append(self.lisd[7])
                    listaAgrega.append(self.lisd[8])
                    listaAgrega.append(self.lisd[9])
                    listaAgrega.append(self.lisd[10])
                    listaAgrega.append(self.lisd[11])
                    listaAgrega.append(0)
                    self.prosBloq.append(listaAgrega)                    
                    try:
                        self.lisd = self.listaAux.pop(0)
                        self.quantum2 = 1
                        if self.lisd[7] == 0:
                            self.lisd[7] = 1
                            self.lisd[6] = self.contadorGlobal
                            #print(self.lisd)
                    except IndexError:
                        self.lisd = []
                    self.terminadoProceso()
                except IndexError:
                    pass
            if self.bandera == 1:
                self.bandera = 0
            else:
                self.cont += 1
                
                if self.cont > self.terminador:
                      self.terminadoProceso()  
        

class MainWindow(QtWidgets.QWidget, Ui_widget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_I:
            self.bandera = 1
            print("Se presiono la letra I")
        elif event.key() == Qt.Key_E:
            self.bandera = 2
            print("Se presiono la letra E")
        elif event.key() == Qt.Key_P:
            self.bandera = 3
            print("Se presiono la letra P")
        elif event.key() == Qt.Key_N:
            self.bandera = 4
            print("Se presiono la letra N")
        elif event.key() == Qt.Key_T:
            self.bandera = 5
            print("Se presiono la letra T")
        elif event.key() == Qt.Key_C:
            self.start_stop_func()
            print("Se presiono la letra C")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #widget = QtWidgets.QWidget()
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

