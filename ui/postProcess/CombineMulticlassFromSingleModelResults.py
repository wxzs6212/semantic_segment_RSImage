# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CombineMulticlassFromSingleModelResults.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_combine_multiclas_fromsinglemodel(object):
    def setupUi(self, Dialog_combine_multiclas_fromsinglemodel):
        Dialog_combine_multiclas_fromsinglemodel.setObjectName("Dialog_combine_multiclas_fromsinglemodel")
        Dialog_combine_multiclas_fromsinglemodel.resize(436, 229)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_combine_multiclas_fromsinglemodel)
        self.buttonBox.setGeometry(QtCore.QRect(60, 180, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget_3 = QtWidgets.QWidget(Dialog_combine_multiclas_fromsinglemodel)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 10, 411, 27))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_6.setMinimumSize(QtCore.QSize(55, 23))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lineEdit_road_mask = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_road_mask.setMinimumSize(QtCore.QSize(201, 23))
        self.lineEdit_road_mask.setObjectName("lineEdit_road_mask")
        self.horizontalLayout_8.addWidget(self.lineEdit_road_mask)
        self.pushButton_road_mask = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_road_mask.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButton_road_mask.setObjectName("pushButton_road_mask")
        self.horizontalLayout_8.addWidget(self.pushButton_road_mask)
        self.layoutWidget = QtWidgets.QWidget(Dialog_combine_multiclas_fromsinglemodel)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 130, 401, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(55, 23))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.lineEdit_mask = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_mask.setMinimumSize(QtCore.QSize(201, 23))
        self.lineEdit_mask.setObjectName("lineEdit_mask")
        self.horizontalLayout.addWidget(self.lineEdit_mask)
        self.pushButton_mask = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_mask.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButton_mask.setObjectName("pushButton_mask")
        self.horizontalLayout.addWidget(self.pushButton_mask)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog_combine_multiclas_fromsinglemodel)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 80, 401, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.spinBox_forground = QtWidgets.QSpinBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(23)
        sizePolicy.setHeightForWidth(self.spinBox_forground.sizePolicy().hasHeightForWidth())
        self.spinBox_forground.setSizePolicy(sizePolicy)
        self.spinBox_forground.setMinimum(1)
        self.spinBox_forground.setMaximum(100000)
        self.spinBox_forground.setSingleStep(1)
        self.spinBox_forground.setProperty("value", 127)
        self.spinBox_forground.setObjectName("spinBox_forground")
        self.horizontalLayout_2.addWidget(self.spinBox_forground)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox_classes_um = QtWidgets.QSpinBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(23)
        sizePolicy.setHeightForWidth(self.spinBox_classes_um.sizePolicy().hasHeightForWidth())
        self.spinBox_classes_um.setSizePolicy(sizePolicy)
        self.spinBox_classes_um.setMinimum(1)
        self.spinBox_classes_um.setMaximum(1000)
        self.spinBox_classes_um.setSingleStep(1)
        self.spinBox_classes_um.setProperty("value", 2)
        self.spinBox_classes_um.setObjectName("spinBox_classes_um")
        self.horizontalLayout_2.addWidget(self.spinBox_classes_um)
        self.layoutWidget_4 = QtWidgets.QWidget(Dialog_combine_multiclas_fromsinglemodel)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 50, 411, 27))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_8.setMinimumSize(QtCore.QSize(55, 23))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.lineEdit_building_mask = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_building_mask.setMinimumSize(QtCore.QSize(201, 23))
        self.lineEdit_building_mask.setObjectName("lineEdit_building_mask")
        self.horizontalLayout_9.addWidget(self.lineEdit_building_mask)
        self.pushButton_building_mask = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_building_mask.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButton_building_mask.setObjectName("pushButton_building_mask")
        self.horizontalLayout_9.addWidget(self.pushButton_building_mask)

        self.retranslateUi(Dialog_combine_multiclas_fromsinglemodel)
        self.buttonBox.rejected.connect(Dialog_combine_multiclas_fromsinglemodel.reject)
        self.buttonBox.accepted.connect(Dialog_combine_multiclas_fromsinglemodel.slot_ok)
        self.pushButton_mask.clicked.connect(Dialog_combine_multiclas_fromsinglemodel.slot_get_save_mask)
        self.pushButton_road_mask.clicked.connect(Dialog_combine_multiclas_fromsinglemodel.slot_select_road_mask)
        self.pushButton_building_mask.clicked.connect(Dialog_combine_multiclas_fromsinglemodel.slot_select_building_mask)
        QtCore.QMetaObject.connectSlotsByName(Dialog_combine_multiclas_fromsinglemodel)

    def retranslateUi(self, Dialog_combine_multiclas_fromsinglemodel):
        _translate = QtCore.QCoreApplication.translate
        Dialog_combine_multiclas_fromsinglemodel.setWindowTitle(_translate("Dialog_combine_multiclas_fromsinglemodel", "Dialog"))
        self.label_6.setText(_translate("Dialog_combine_multiclas_fromsinglemodel", "Road  masks:"))
        self.pushButton_road_mask.setText(_translate("Dialog_combine_multiclas_fromsinglemodel", "Open"))
        self.label_7.setText(_translate("Dialog_combine_multiclas_fromsinglemodel", "Output Mask:"))
        self.pushButton_mask.setText(_translate("Dialog_combine_multiclas_fromsinglemodel", "Open"))
        self.label.setText(_translate("Dialog_combine_multiclas_fromsinglemodel", "Foreground value:"))
        self.label_2.setText(_translate("Dialog_combine_multiclas_fromsinglemodel", "Class Num:"))
        self.label_8.setText(_translate("Dialog_combine_multiclas_fromsinglemodel", "Building masks:"))
        self.pushButton_building_mask.setText(_translate("Dialog_combine_multiclas_fromsinglemodel", "Open"))

