# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PredictMulticlassBatch.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_predict_multiclass_batch(object):
    def setupUi(self, Dialog_predict_multiclass_batch):
        Dialog_predict_multiclass_batch.setObjectName("Dialog_predict_multiclass_batch")
        Dialog_predict_multiclass_batch.resize(467, 300)
        self.layoutWidget_4 = QtWidgets.QWidget(Dialog_predict_multiclass_batch)
        self.layoutWidget_4.setGeometry(QtCore.QRect(0, 160, 441, 27))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_7.setMinimumSize(QtCore.QSize(55, 23))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.lineEdit_mask_dir = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_mask_dir.setMinimumSize(QtCore.QSize(201, 23))
        self.lineEdit_mask_dir.setObjectName("lineEdit_mask_dir")
        self.horizontalLayout_9.addWidget(self.lineEdit_mask_dir)
        self.pushButton_mask = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_mask.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButton_mask.setObjectName("pushButton_mask")
        self.horizontalLayout_9.addWidget(self.pushButton_mask)
        self.layoutWidget_3 = QtWidgets.QWidget(Dialog_predict_multiclass_batch)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 10, 441, 27))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_6.setMinimumSize(QtCore.QSize(55, 23))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lineEdit_images_dir = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_images_dir.setMinimumSize(QtCore.QSize(201, 23))
        self.lineEdit_images_dir.setObjectName("lineEdit_images_dir")
        self.horizontalLayout_8.addWidget(self.lineEdit_images_dir)
        self.pushButton_image = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_image.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButton_image.setObjectName("pushButton_image")
        self.horizontalLayout_8.addWidget(self.pushButton_image)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog_predict_multiclass_batch)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 80, 441, 27))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_5.setMinimumSize(QtCore.QSize(55, 23))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.lineEdit_model = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_model.setMinimumSize(QtCore.QSize(201, 23))
        self.lineEdit_model.setObjectName("lineEdit_model")
        self.horizontalLayout_7.addWidget(self.lineEdit_model)
        self.pushButton_model = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_model.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButton_model.setObjectName("pushButton_model")
        self.horizontalLayout_7.addWidget(self.pushButton_model)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_predict_multiclass_batch)
        self.buttonBox.setGeometry(QtCore.QRect(30, 220, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget_5 = QtWidgets.QWidget(Dialog_predict_multiclass_batch)
        self.layoutWidget_5.setGeometry(QtCore.QRect(0, 120, 439, 24))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.comboBox_gupid = QtWidgets.QComboBox(self.layoutWidget_5)
        self.comboBox_gupid.setMinimumSize(QtCore.QSize(0, 22))
        self.comboBox_gupid.setObjectName("comboBox_gupid")
        self.comboBox_gupid.addItem("")
        self.comboBox_gupid.addItem("")
        self.comboBox_gupid.addItem("")
        self.comboBox_gupid.addItem("")
        self.comboBox_gupid.addItem("")
        self.comboBox_gupid.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_gupid)
        spacerItem = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.layoutWidget_5)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.spinBox_classes = QtWidgets.QSpinBox(self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_classes.sizePolicy().hasHeightForWidth())
        self.spinBox_classes.setSizePolicy(sizePolicy)
        self.spinBox_classes.setMinimumSize(QtCore.QSize(47, 22))
        self.spinBox_classes.setMinimum(1)
        self.spinBox_classes.setMaximum(100)
        self.spinBox_classes.setSingleStep(1)
        self.spinBox_classes.setProperty("value", 2)
        self.spinBox_classes.setObjectName("spinBox_classes")
        self.horizontalLayout_2.addWidget(self.spinBox_classes)
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.comboBox_strategy = QtWidgets.QComboBox(self.layoutWidget_5)
        self.comboBox_strategy.setMinimumSize(QtCore.QSize(0, 22))
        self.comboBox_strategy.setObjectName("comboBox_strategy")
        self.comboBox_strategy.addItem("")
        self.comboBox_strategy.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_strategy)
        self.layoutWidget_6 = QtWidgets.QWidget(Dialog_predict_multiclass_batch)
        self.layoutWidget_6.setGeometry(QtCore.QRect(10, 50, 444, 25))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.spinBox_bands = QtWidgets.QSpinBox(self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_bands.sizePolicy().hasHeightForWidth())
        self.spinBox_bands.setSizePolicy(sizePolicy)
        self.spinBox_bands.setMinimumSize(QtCore.QSize(47, 22))
        self.spinBox_bands.setMinimum(1)
        self.spinBox_bands.setMaximum(1000)
        self.spinBox_bands.setProperty("value", 3)
        self.spinBox_bands.setObjectName("spinBox_bands")
        self.horizontalLayout_4.addWidget(self.spinBox_bands)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.comboBox_dtype = QtWidgets.QComboBox(self.layoutWidget_6)
        self.comboBox_dtype.setObjectName("comboBox_dtype")
        self.comboBox_dtype.addItem("")
        self.comboBox_dtype.addItem("")
        self.comboBox_dtype.addItem("")
        self.comboBox_dtype.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_dtype)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_3.setMinimumSize(QtCore.QSize(33, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.spinBox_windsize = QtWidgets.QSpinBox(self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(23)
        sizePolicy.setHeightForWidth(self.spinBox_windsize.sizePolicy().hasHeightForWidth())
        self.spinBox_windsize.setSizePolicy(sizePolicy)
        self.spinBox_windsize.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_windsize.setMaximumSize(QtCore.QSize(50, 23))
        self.spinBox_windsize.setMaximum(1000)
        self.spinBox_windsize.setSingleStep(2)
        self.spinBox_windsize.setProperty("value", 256)
        self.spinBox_windsize.setObjectName("spinBox_windsize")
        self.horizontalLayout_4.addWidget(self.spinBox_windsize)

        self.retranslateUi(Dialog_predict_multiclass_batch)
        self.pushButton_image.clicked.connect(Dialog_predict_multiclass_batch.slot_select_img_dir)
        self.pushButton_model.clicked.connect(Dialog_predict_multiclass_batch.slot_select_model_file)
        self.pushButton_mask.clicked.connect(Dialog_predict_multiclass_batch.slot_save_mask_dir)
        self.buttonBox.accepted.connect(Dialog_predict_multiclass_batch.slot_ok)
        self.buttonBox.rejected.connect(Dialog_predict_multiclass_batch.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_predict_multiclass_batch)

    def retranslateUi(self, Dialog_predict_multiclass_batch):
        _translate = QtCore.QCoreApplication.translate
        Dialog_predict_multiclass_batch.setWindowTitle(_translate("Dialog_predict_multiclass_batch", "Dialog"))
        self.label_7.setText(_translate("Dialog_predict_multiclass_batch", "Output dir:"))
        self.pushButton_mask.setText(_translate("Dialog_predict_multiclass_batch", "Open"))
        self.label_6.setText(_translate("Dialog_predict_multiclass_batch", "Image dir:"))
        self.pushButton_image.setText(_translate("Dialog_predict_multiclass_batch", "Open"))
        self.label_5.setText(_translate("Dialog_predict_multiclass_batch", "Model:"))
        self.pushButton_model.setText(_translate("Dialog_predict_multiclass_batch", "Open"))
        self.label_12.setText(_translate("Dialog_predict_multiclass_batch", "GPU ID:"))
        self.comboBox_gupid.setItemText(0, _translate("Dialog_predict_multiclass_batch", "0"))
        self.comboBox_gupid.setItemText(1, _translate("Dialog_predict_multiclass_batch", "1"))
        self.comboBox_gupid.setItemText(2, _translate("Dialog_predict_multiclass_batch", "2"))
        self.comboBox_gupid.setItemText(3, _translate("Dialog_predict_multiclass_batch", "3"))
        self.comboBox_gupid.setItemText(4, _translate("Dialog_predict_multiclass_batch", "4"))
        self.comboBox_gupid.setItemText(5, _translate("Dialog_predict_multiclass_batch", "5"))
        self.label.setText(_translate("Dialog_predict_multiclass_batch", "Target classes:"))
        self.label_13.setText(_translate("Dialog_predict_multiclass_batch", "Predict strategy:"))
        self.comboBox_strategy.setItemText(0, _translate("Dialog_predict_multiclass_batch", "original"))
        self.comboBox_strategy.setItemText(1, _translate("Dialog_predict_multiclass_batch", "smooth"))
        self.label_8.setText(_translate("Dialog_predict_multiclass_batch", "bands:"))
        self.label_9.setText(_translate("Dialog_predict_multiclass_batch", "dtype:"))
        self.comboBox_dtype.setItemText(0, _translate("Dialog_predict_multiclass_batch", "uint8"))
        self.comboBox_dtype.setItemText(1, _translate("Dialog_predict_multiclass_batch", "uint10"))
        self.comboBox_dtype.setItemText(2, _translate("Dialog_predict_multiclass_batch", "uint16"))
        self.comboBox_dtype.setItemText(3, _translate("Dialog_predict_multiclass_batch", "float"))
        self.label_3.setText(_translate("Dialog_predict_multiclass_batch", "windsize :"))

