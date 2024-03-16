# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CupEditor_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 957)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_airport_name_cup = QtWidgets.QLabel(self.centralwidget)
        self.label_airport_name_cup.setGeometry(QtCore.QRect(20, 10, 159, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_airport_name_cup.setFont(font)
        self.label_airport_name_cup.setObjectName("label_airport_name_cup")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 70, 1081, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 870, 1081, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(30, 0, 30, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_previous = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_previous.setObjectName("pushButton_previous")
        self.horizontalLayout.addWidget(self.pushButton_previous)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_apply = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.horizontalLayout.addWidget(self.pushButton_apply)
        self.pushButton_write_changes = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_write_changes.setObjectName("pushButton_write_changes")
        self.horizontalLayout.addWidget(self.pushButton_write_changes)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_next = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout.addWidget(self.pushButton_next)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(100, 100, 310, 24))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_cup_latitude = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_cup_latitude.setObjectName("lineEdit_cup_latitude")
        self.horizontalLayout_2.addWidget(self.lineEdit_cup_latitude)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_cup_longitude = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_cup_longitude.setObjectName("lineEdit_cup_longitude")
        self.horizontalLayout_2.addWidget(self.lineEdit_cup_longitude)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 130, 291, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.lineEdit_cup_elevation = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_cup_elevation.setObjectName("lineEdit_cup_elevation")
        self.horizontalLayout_7.addWidget(self.lineEdit_cup_elevation)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.lineEdit_cup_frequency = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_cup_frequency.setObjectName("lineEdit_cup_frequency")
        self.horizontalLayout_6.addWidget(self.lineEdit_cup_frequency)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lineEdit_cup_runway = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_cup_runway.setObjectName("lineEdit_cup_runway")
        self.horizontalLayout_5.addWidget(self.lineEdit_cup_runway)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit_cup_length = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_cup_length.setObjectName("lineEdit_cup_length")
        self.horizontalLayout_4.addWidget(self.lineEdit_cup_length)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_cup_width = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_cup_width.setObjectName("lineEdit_cup_width")
        self.horizontalLayout_3.addWidget(self.lineEdit_cup_width)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.comboBox_cup_wayport_style = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_cup_wayport_style.setObjectName("comboBox_cup_wayport_style")
        self.horizontalLayout_8.addWidget(self.comboBox_cup_wayport_style)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(790, 100, 310, 24))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.lineEdit_file_latitude = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        self.lineEdit_file_latitude.setObjectName("lineEdit_file_latitude")
        self.horizontalLayout_9.addWidget(self.lineEdit_file_latitude)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.lineEdit_file_longitude = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        self.lineEdit_file_longitude.setObjectName("lineEdit_file_longitude")
        self.horizontalLayout_9.addWidget(self.lineEdit_file_longitude)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(670, 130, 431, 234))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_copy_elevation = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_copy_elevation.setObjectName("pushButton_copy_elevation")
        self.horizontalLayout_10.addWidget(self.pushButton_copy_elevation)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.lineEdit_file_elevation = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_file_elevation.setObjectName("lineEdit_file_elevation")
        self.horizontalLayout_10.addWidget(self.lineEdit_file_elevation)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_copy_frequency = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_copy_frequency.setObjectName("pushButton_copy_frequency")
        self.horizontalLayout_11.addWidget(self.pushButton_copy_frequency)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.lineEdit_file_frequency = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_file_frequency.setObjectName("lineEdit_file_frequency")
        self.horizontalLayout_11.addWidget(self.lineEdit_file_frequency)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_copy_runway = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_copy_runway.setObjectName("pushButton_copy_runway")
        self.horizontalLayout_12.addWidget(self.pushButton_copy_runway)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_12.addWidget(self.label_14)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem9)
        self.lineEdit_file_runway = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_file_runway.setObjectName("lineEdit_file_runway")
        self.horizontalLayout_12.addWidget(self.lineEdit_file_runway)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_copy_length = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_copy_length.setObjectName("pushButton_copy_length")
        self.horizontalLayout_13.addWidget(self.pushButton_copy_length)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem10)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_13.addWidget(self.label_15)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem11)
        self.lineEdit_file_length = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_file_length.setObjectName("lineEdit_file_length")
        self.horizontalLayout_13.addWidget(self.lineEdit_file_length)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_copy_width = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_copy_width.setObjectName("pushButton_copy_width")
        self.horizontalLayout_14.addWidget(self.pushButton_copy_width)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem12)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_14.addWidget(self.label_16)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem13)
        self.lineEdit_file_width = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_file_width.setObjectName("lineEdit_file_width")
        self.horizontalLayout_14.addWidget(self.lineEdit_file_width)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_15.addWidget(self.label_17)
        self.label_file_surface = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_file_surface.setObjectName("label_file_surface")
        self.horizontalLayout_15.addWidget(self.label_file_surface)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.label_airport_name_file = QtWidgets.QLabel(self.centralwidget)
        self.label_airport_name_file.setGeometry(QtCore.QRect(600, 10, 159, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_airport_name_file.setFont(font)
        self.label_airport_name_file.setObjectName("label_airport_name_file")
        self.cup_image = QtWidgets.QLabel(self.centralwidget)
        self.cup_image.setGeometry(QtCore.QRect(30, 400, 400, 400))
        self.cup_image.setObjectName("cup_image")
        self.file_image = QtWidgets.QLabel(self.centralwidget)
        self.file_image.setGeometry(QtCore.QRect(690, 400, 400, 400))
        self.file_image.setObjectName("file_image")
        self.pushButton_open_cup_image = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_cup_image.setGeometry(QtCore.QRect(160, 810, 121, 28))
        self.pushButton_open_cup_image.setObjectName("pushButton_open_cup_image")
        self.pushButton_open_file_image = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_file_image.setGeometry(QtCore.QRect(780, 810, 121, 28))
        self.pushButton_open_file_image.setObjectName("pushButton_open_file_image")
        self.label_airport_code_cup = QtWidgets.QLabel(self.centralwidget)
        self.label_airport_code_cup.setGeometry(QtCore.QRect(20, 40, 159, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_airport_code_cup.setFont(font)
        self.label_airport_code_cup.setObjectName("label_airport_code_cup")
        self.label_airport_code_file = QtWidgets.QLabel(self.centralwidget)
        self.label_airport_code_file.setGeometry(QtCore.QRect(600, 40, 159, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_airport_code_file.setFont(font)
        self.label_airport_code_file.setObjectName("label_airport_code_file")
        self.pushButton_discrepancies = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_discrepancies.setGeometry(QtCore.QRect(470, 800, 181, 61))
        self.pushButton_discrepancies.setObjectName("pushButton_discrepancies")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(480, 80, 151, 281))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 131, 261))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_location = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_location.setAutoExclusive(False)
        self.radioButton_location.setObjectName("radioButton_location")
        self.verticalLayout_3.addWidget(self.radioButton_location)
        self.radioButton_elevation = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_elevation.setAutoExclusive(False)
        self.radioButton_elevation.setObjectName("radioButton_elevation")
        self.verticalLayout_3.addWidget(self.radioButton_elevation)
        self.radioButton_frequency = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_frequency.setAutoExclusive(False)
        self.radioButton_frequency.setObjectName("radioButton_frequency")
        self.verticalLayout_3.addWidget(self.radioButton_frequency)
        self.radioButton_direction = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_direction.setAutoExclusive(False)
        self.radioButton_direction.setObjectName("radioButton_direction")
        self.verticalLayout_3.addWidget(self.radioButton_direction)
        self.radioButton_length = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_length.setAutoExclusive(False)
        self.radioButton_length.setObjectName("radioButton_length")
        self.verticalLayout_3.addWidget(self.radioButton_length)
        self.radioButton_width = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_width.setAutoExclusive(False)
        self.radioButton_width.setObjectName("radioButton_width")
        self.verticalLayout_3.addWidget(self.radioButton_width)
        self.radioButton_surface = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_surface.setAutoExclusive(False)
        self.radioButton_surface.setObjectName("radioButton_surface")
        self.verticalLayout_3.addWidget(self.radioButton_surface)
        self.pushButton_file_print_attributes = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_file_print_attributes.setGeometry(QtCore.QRect(780, 840, 121, 28))
        self.pushButton_file_print_attributes.setObjectName("pushButton_file_print_attributes")
        self.pushButton_cup_print_attributes = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cup_print_attributes.setGeometry(QtCore.QRect(160, 840, 121, 28))
        self.pushButton_cup_print_attributes.setObjectName("pushButton_cup_print_attributes")
        self.pushButton_copy_location = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_copy_location.setGeometry(QtCore.QRect(670, 98, 93, 28))
        self.pushButton_copy_location.setObjectName("pushButton_copy_location")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 350, 441, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.lineEdit_cup_waypoint_name = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_cup_waypoint_name.setObjectName("lineEdit_cup_waypoint_name")
        self.horizontalLayout_16.addWidget(self.lineEdit_cup_waypoint_name)
        self.lineEdit_cup_code = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_cup_code.setObjectName("lineEdit_cup_code")
        self.horizontalLayout_16.addWidget(self.lineEdit_cup_code)
        self.pushButton_copy_coordinates = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_copy_coordinates.setGeometry(QtCore.QRect(30, 100, 51, 28))
        self.pushButton_copy_coordinates.setObjectName("pushButton_copy_coordinates")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(490, 450, 139, 146))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem14)
        self.lineEdit_lookup = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_lookup.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_lookup.setObjectName("lineEdit_lookup")
        self.horizontalLayout_18.addWidget(self.lineEdit_lookup)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem15)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem16)
        self.pushButton_lookup = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_lookup.setObjectName("pushButton_lookup")
        self.horizontalLayout_19.addWidget(self.pushButton_lookup)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem17)
        self.verticalLayout_4.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem18)
        self.comboBox_filter_distance = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.comboBox_filter_distance.setObjectName("comboBox_filter_distance")
        self.comboBox_filter_distance.addItem("")
        self.comboBox_filter_distance.addItem("")
        self.comboBox_filter_distance.addItem("")
        self.comboBox_filter_distance.addItem("")
        self.comboBox_filter_distance.addItem("")
        self.comboBox_filter_distance.addItem("")
        self.comboBox_filter_distance.addItem("")
        self.comboBox_filter_distance.addItem("")
        self.comboBox_filter_distance.addItem("")
        self.comboBox_filter_distance.addItem("")
        self.horizontalLayout_17.addWidget(self.comboBox_filter_distance)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem19)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem20)
        self.checkBox_filter = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_filter.setObjectName("checkBox_filter")
        self.horizontalLayout_20.addWidget(self.checkBox_filter)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem21)
        self.verticalLayout_4.addLayout(self.horizontalLayout_20)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_airport_name_cup.setText(_translate("MainWindow", "Airport: CUP"))
        self.pushButton_previous.setText(_translate("MainWindow", "<- Previous"))
        self.pushButton_apply.setText(_translate("MainWindow", "Apply"))
        self.pushButton_write_changes.setText(_translate("MainWindow", "  Write Changes  "))
        self.pushButton_next.setText(_translate("MainWindow", "Next ->"))
        self.label_2.setText(_translate("MainWindow", "Latitude:"))
        self.lineEdit_cup_latitude.setText(_translate("MainWindow", "37.0000000"))
        self.label_3.setText(_translate("MainWindow", "Longitude:"))
        self.lineEdit_cup_longitude.setText(_translate("MainWindow", "37.0000000"))
        self.label_8.setText(_translate("MainWindow", "Elevation (ft):"))
        self.lineEdit_cup_elevation.setText(_translate("MainWindow", "37.0000000"))
        self.label_7.setText(_translate("MainWindow", "Frequency:"))
        self.lineEdit_cup_frequency.setText(_translate("MainWindow", "37.0000000"))
        self.label_6.setText(_translate("MainWindow", "Runway:"))
        self.lineEdit_cup_runway.setText(_translate("MainWindow", "37.0000000"))
        self.label_5.setText(_translate("MainWindow", "Length (ft):"))
        self.lineEdit_cup_length.setText(_translate("MainWindow", "37.0000000"))
        self.label_4.setText(_translate("MainWindow", "Width (ft):"))
        self.lineEdit_cup_width.setText(_translate("MainWindow", "37.0000000"))
        self.label_9.setText(_translate("MainWindow", "Type:"))
        self.label_10.setText(_translate("MainWindow", "Latitude:"))
        self.lineEdit_file_latitude.setText(_translate("MainWindow", "37.0000000"))
        self.label_11.setText(_translate("MainWindow", "Longitude:"))
        self.lineEdit_file_longitude.setText(_translate("MainWindow", "37.0000000"))
        self.pushButton_copy_elevation.setText(_translate("MainWindow", "<- Copy"))
        self.label_12.setText(_translate("MainWindow", "Elevation (ft):"))
        self.lineEdit_file_elevation.setText(_translate("MainWindow", "37.0000000"))
        self.pushButton_copy_frequency.setText(_translate("MainWindow", "<- Copy"))
        self.label_13.setText(_translate("MainWindow", "Frequency:"))
        self.lineEdit_file_frequency.setText(_translate("MainWindow", "37.0000000"))
        self.pushButton_copy_runway.setText(_translate("MainWindow", "<- Copy"))
        self.label_14.setText(_translate("MainWindow", "Runway:"))
        self.lineEdit_file_runway.setText(_translate("MainWindow", "37.0000000"))
        self.pushButton_copy_length.setText(_translate("MainWindow", "<- Copy"))
        self.label_15.setText(_translate("MainWindow", "Length (ft):"))
        self.lineEdit_file_length.setText(_translate("MainWindow", "37.0000000"))
        self.pushButton_copy_width.setText(_translate("MainWindow", "<- Copy"))
        self.label_16.setText(_translate("MainWindow", "Width (ft):"))
        self.lineEdit_file_width.setText(_translate("MainWindow", "37.0000000"))
        self.label_17.setText(_translate("MainWindow", "Surface:"))
        self.label_file_surface.setText(_translate("MainWindow", "<surface>"))
        self.label_airport_name_file.setText(_translate("MainWindow", "Airport: File"))
        self.cup_image.setText(_translate("MainWindow", "TextLabel"))
        self.file_image.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_open_cup_image.setText(_translate("MainWindow", "Open Image File"))
        self.pushButton_open_file_image.setText(_translate("MainWindow", "Open Image File"))
        self.label_airport_code_cup.setText(_translate("MainWindow", "Code: CUP"))
        self.label_airport_code_file.setText(_translate("MainWindow", "Code: CUP"))
        self.pushButton_discrepancies.setText(_translate("MainWindow", "Show Only Discrepancies"))
        self.groupBox.setTitle(_translate("MainWindow", "Faults"))
        self.radioButton_location.setText(_translate("MainWindow", "Location"))
        self.radioButton_elevation.setText(_translate("MainWindow", "Elevation"))
        self.radioButton_frequency.setText(_translate("MainWindow", "Frequency"))
        self.radioButton_direction.setText(_translate("MainWindow", "Runway Direction"))
        self.radioButton_length.setText(_translate("MainWindow", "Runway Length"))
        self.radioButton_width.setText(_translate("MainWindow", "Runway Width"))
        self.radioButton_surface.setText(_translate("MainWindow", "Runway Surface"))
        self.pushButton_file_print_attributes.setText(_translate("MainWindow", "Print Attributes"))
        self.pushButton_cup_print_attributes.setText(_translate("MainWindow", "Print Attributes"))
        self.pushButton_copy_location.setText(_translate("MainWindow", "<- Copy"))
        self.lineEdit_cup_waypoint_name.setText(_translate("MainWindow", "<Waypoint Name>"))
        self.lineEdit_cup_code.setText(_translate("MainWindow", "<Code>"))
        self.pushButton_copy_coordinates.setText(_translate("MainWindow", "Copy"))
        self.pushButton_lookup.setText(_translate("MainWindow", "Lookup"))
        self.comboBox_filter_distance.setItemText(0, _translate("MainWindow", "10"))
        self.comboBox_filter_distance.setItemText(1, _translate("MainWindow", "20"))
        self.comboBox_filter_distance.setItemText(2, _translate("MainWindow", "30"))
        self.comboBox_filter_distance.setItemText(3, _translate("MainWindow", "40"))
        self.comboBox_filter_distance.setItemText(4, _translate("MainWindow", "50"))
        self.comboBox_filter_distance.setItemText(5, _translate("MainWindow", "60"))
        self.comboBox_filter_distance.setItemText(6, _translate("MainWindow", "70"))
        self.comboBox_filter_distance.setItemText(7, _translate("MainWindow", "80"))
        self.comboBox_filter_distance.setItemText(8, _translate("MainWindow", "90"))
        self.comboBox_filter_distance.setItemText(9, _translate("MainWindow", "100"))
        self.label.setText(_translate("MainWindow", "Units: NM"))
        self.checkBox_filter.setText(_translate("MainWindow", "Filter Distance"))
