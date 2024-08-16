# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resources
import resources
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1241, 857)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.icoOnly_wg = QWidget(self.centralwidget)
        self.icoOnly_wg.setObjectName(u"icoOnly_wg")
        self.icoOnly_wg.setMinimumSize(QSize(91, 841))
        self.icoOnly_wg.setMaximumSize(QSize(91, 841))
        self.icoOnly_wg.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	border-radius:3px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.icoOnly_wg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.icoOnly_wg)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/icons/logo.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(17, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(28)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 12, -1, -1)
        self.tkIcon = QPushButton(self.icoOnly_wg)
        self.tkIcon.setObjectName(u"tkIcon")
        icon = QIcon()
        icon.addFile(u":/icons/institutionsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/institutionsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.tkIcon.setIcon(icon)
        self.tkIcon.setIconSize(QSize(100, 16))
        self.tkIcon.setCheckable(True)
        self.tkIcon.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.tkIcon)

        self.LCicon = QPushButton(self.icoOnly_wg)
        self.LCicon.setObjectName(u"LCicon")
        icon1 = QIcon()
        icon1.addFile(u":/icons/studentssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/studentssmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.LCicon.setIcon(icon1)
        self.LCicon.setIconSize(QSize(100, 20))
        self.LCicon.setCheckable(True)
        self.LCicon.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.LCicon)

        self.CGicon = QPushButton(self.icoOnly_wg)
        self.CGicon.setObjectName(u"CGicon")
        icon2 = QIcon()
        icon2.addFile(u":/icons/teacherssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/teacherssmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.CGicon.setIcon(icon2)
        self.CGicon.setIconSize(QSize(100, 20))
        self.CGicon.setCheckable(True)
        self.CGicon.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.CGicon)

        self.TDicon = QPushButton(self.icoOnly_wg)
        self.TDicon.setObjectName(u"TDicon")
        icon3 = QIcon()
        icon3.addFile(u":/icons/financessmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/financessmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.TDicon.setIcon(icon3)
        self.TDicon.setIconSize(QSize(100, 20))
        self.TDicon.setCheckable(True)
        self.TDicon.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.TDicon)


        self.verticalLayout.addLayout(self.verticalLayout_8)

        self.verticalSpacer_2 = QSpacerItem(20, 519, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.set1 = QPushButton(self.icoOnly_wg)
        self.set1.setObjectName(u"set1")
        icon4 = QIcon()
        icon4.addFile(u":/icons/settingssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icons/settingssmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.set1.setIcon(icon4)
        self.set1.setIconSize(QSize(100, 20))
        self.set1.setCheckable(True)
        self.set1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.set1)

        self.q1 = QPushButton(self.icoOnly_wg)
        self.q1.setObjectName(u"q1")
        icon5 = QIcon()
        icon5.addFile(u":/icons/signoutsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icons/signoutsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.q1.setIcon(icon5)
        self.q1.setIconSize(QSize(100, 16))
        self.q1.setCheckable(True)
        self.q1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.q1)


        self.verticalLayout.addLayout(self.verticalLayout_9)


        self.gridLayout.addWidget(self.icoOnly_wg, 0, 0, 1, 1)

        self.iconExpand_wg = QFrame(self.centralwidget)
        self.iconExpand_wg.setObjectName(u"iconExpand_wg")
        self.iconExpand_wg.setMinimumSize(QSize(246, 841))
        self.iconExpand_wg.setMaximumSize(QSize(246, 841))
        self.iconExpand_wg.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color:white;\n"
"}\n"
"QPushButton{\n"
"    border:none;\n"
"	height:30px;    \n"
"}")
        self.iconExpand_wg.setFrameShape(QFrame.StyledPanel)
        self.iconExpand_wg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.iconExpand_wg)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.iconExpand_wg)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icons/logo.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.iconExpand_wg)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalSpacer_4 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_21.addLayout(self.horizontalLayout_3)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.thongKe = QFrame(self.iconExpand_wg)
        self.thongKe.setObjectName(u"thongKe")
        self.thongKe.setFrameShape(QFrame.StyledPanel)
        self.thongKe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.thongKe)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.TKbut = QPushButton(self.thongKe)
        self.TKbut.setObjectName(u"TKbut")
        self.TKbut.setCheckable(True)

        self.verticalLayout_13.addWidget(self.TKbut)

        self.tkList = QFrame(self.thongKe)
        self.tkList.setObjectName(u"tkList")
        self.tkList.setFrameShape(QFrame.StyledPanel)
        self.tkList.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.tkList)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tkCapLanDau = QPushButton(self.tkList)
        self.tkCapLanDau.setObjectName(u"tkCapLanDau")
        self.tkCapLanDau.setMinimumSize(QSize(0, 18))
        self.tkCapLanDau.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.tkCapLanDau.setCheckable(True)

        self.verticalLayout_12.addWidget(self.tkCapLanDau)

        self.tkCapTungDonvi = QPushButton(self.tkList)
        self.tkCapTungDonvi.setObjectName(u"tkCapTungDonvi")
        self.tkCapTungDonvi.setMinimumSize(QSize(0, 18))
        self.tkCapTungDonvi.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.tkCapTungDonvi.setCheckable(True)

        self.verticalLayout_12.addWidget(self.tkCapTungDonvi)

        self.tkTheoNam = QPushButton(self.tkList)
        self.tkTheoNam.setObjectName(u"tkTheoNam")
        self.tkTheoNam.setMinimumSize(QSize(0, 18))
        self.tkTheoNam.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.tkTheoNam.setCheckable(True)

        self.verticalLayout_12.addWidget(self.tkTheoNam)

        self.tkTheoKhoangTime = QPushButton(self.tkList)
        self.tkTheoKhoangTime.setObjectName(u"tkTheoKhoangTime")
        self.tkTheoKhoangTime.setMinimumSize(QSize(0, 18))
        self.tkTheoKhoangTime.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.tkTheoKhoangTime.setCheckable(True)

        self.verticalLayout_12.addWidget(self.tkTheoKhoangTime)

        self.tkTheoNgayCN = QPushButton(self.tkList)
        self.tkTheoNgayCN.setObjectName(u"tkTheoNgayCN")
        self.tkTheoNgayCN.setMinimumSize(QSize(0, 18))
        self.tkTheoNgayCN.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.tkTheoNgayCN.setCheckable(True)

        self.verticalLayout_12.addWidget(self.tkTheoNgayCN)

        self.tkToanBo = QPushButton(self.tkList)
        self.tkToanBo.setObjectName(u"tkToanBo")
        self.tkToanBo.setMinimumSize(QSize(0, 18))
        self.tkToanBo.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.tkToanBo.setCheckable(True)

        self.verticalLayout_12.addWidget(self.tkToanBo)

        self.tkDanhSachDKV = QPushButton(self.tkList)
        self.tkDanhSachDKV.setObjectName(u"tkDanhSachDKV")
        self.tkDanhSachDKV.setMinimumSize(QSize(0, 18))
        self.tkDanhSachDKV.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.tkDanhSachDKV.setCheckable(True)

        self.verticalLayout_12.addWidget(self.tkDanhSachDKV)

        self.tkLuanChuyenSum = QPushButton(self.tkList)
        self.tkLuanChuyenSum.setObjectName(u"tkLuanChuyenSum")
        self.tkLuanChuyenSum.setMinimumSize(QSize(0, 18))
        self.tkLuanChuyenSum.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.tkLuanChuyenSum.setCheckable(True)

        self.verticalLayout_12.addWidget(self.tkLuanChuyenSum)


        self.verticalLayout_13.addWidget(self.tkList)


        self.verticalLayout_20.addWidget(self.thongKe)

        self.luanChuyen = QFrame(self.iconExpand_wg)
        self.luanChuyen.setObjectName(u"luanChuyen")
        self.luanChuyen.setFrameShape(QFrame.StyledPanel)
        self.luanChuyen.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.luanChuyen)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.luanChuyenBut = QPushButton(self.luanChuyen)
        self.luanChuyenBut.setObjectName(u"luanChuyenBut")
        self.luanChuyenBut.setCheckable(True)

        self.verticalLayout_14.addWidget(self.luanChuyenBut)

        self.lcList = QFrame(self.luanChuyen)
        self.lcList.setObjectName(u"lcList")
        self.lcList.setFrameShape(QFrame.StyledPanel)
        self.lcList.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.lcList)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.LCNhap = QPushButton(self.lcList)
        self.LCNhap.setObjectName(u"LCNhap")
        self.LCNhap.setMinimumSize(QSize(0, 18))
        self.LCNhap.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.LCNhap.setCheckable(True)

        self.verticalLayout_15.addWidget(self.LCNhap)

        self.LCKiemTraSuaChua = QPushButton(self.lcList)
        self.LCKiemTraSuaChua.setObjectName(u"LCKiemTraSuaChua")
        self.LCKiemTraSuaChua.setMinimumSize(QSize(0, 18))
        self.LCKiemTraSuaChua.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.LCKiemTraSuaChua.setCheckable(True)

        self.verticalLayout_15.addWidget(self.LCKiemTraSuaChua)

        self.LCKiemtraDKV = QPushButton(self.lcList)
        self.LCKiemtraDKV.setObjectName(u"LCKiemtraDKV")
        self.LCKiemtraDKV.setMinimumSize(QSize(0, 18))
        self.LCKiemtraDKV.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.LCKiemtraDKV.setCheckable(True)

        self.verticalLayout_15.addWidget(self.LCKiemtraDKV)


        self.verticalLayout_14.addWidget(self.lcList)


        self.verticalLayout_20.addWidget(self.luanChuyen)

        self.capGiayCn = QFrame(self.iconExpand_wg)
        self.capGiayCn.setObjectName(u"capGiayCn")
        self.capGiayCn.setFrameShape(QFrame.StyledPanel)
        self.capGiayCn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.capGiayCn)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.GCNbut = QPushButton(self.capGiayCn)
        self.GCNbut.setObjectName(u"GCNbut")
        self.GCNbut.setCheckable(True)

        self.verticalLayout_16.addWidget(self.GCNbut)

        self.GCNList = QFrame(self.capGiayCn)
        self.GCNList.setObjectName(u"GCNList")
        self.GCNList.setFrameShape(QFrame.StyledPanel)
        self.GCNList.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.GCNList)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.GCNcapLanDau = QPushButton(self.GCNList)
        self.GCNcapLanDau.setObjectName(u"GCNcapLanDau")
        self.GCNcapLanDau.setMinimumSize(QSize(0, 18))
        self.GCNcapLanDau.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.GCNcapLanDau.setCheckable(True)

        self.verticalLayout_17.addWidget(self.GCNcapLanDau)

        self.GCNtungDonvi = QPushButton(self.GCNList)
        self.GCNtungDonvi.setObjectName(u"GCNtungDonvi")
        self.GCNtungDonvi.setMinimumSize(QSize(0, 18))
        self.GCNtungDonvi.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.GCNtungDonvi.setCheckable(True)

        self.verticalLayout_17.addWidget(self.GCNtungDonvi)

        self.GCNtheoNam = QPushButton(self.GCNList)
        self.GCNtheoNam.setObjectName(u"GCNtheoNam")
        self.GCNtheoNam.setMinimumSize(QSize(0, 18))
        self.GCNtheoNam.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.GCNtheoNam.setCheckable(True)

        self.verticalLayout_17.addWidget(self.GCNtheoNam)

        self.GCNkhoangTime = QPushButton(self.GCNList)
        self.GCNkhoangTime.setObjectName(u"GCNkhoangTime")
        self.GCNkhoangTime.setMinimumSize(QSize(0, 18))
        self.GCNkhoangTime.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.GCNkhoangTime.setCheckable(True)

        self.verticalLayout_17.addWidget(self.GCNkhoangTime)

        self.GCNngayCapCN = QPushButton(self.GCNList)
        self.GCNngayCapCN.setObjectName(u"GCNngayCapCN")
        self.GCNngayCapCN.setMinimumSize(QSize(0, 18))
        self.GCNngayCapCN.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.GCNngayCapCN.setCheckable(True)

        self.verticalLayout_17.addWidget(self.GCNngayCapCN)

        self.GCNtoanBo = QPushButton(self.GCNList)
        self.GCNtoanBo.setObjectName(u"GCNtoanBo")
        self.GCNtoanBo.setMinimumSize(QSize(0, 18))
        self.GCNtoanBo.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.GCNtoanBo.setCheckable(True)

        self.verticalLayout_17.addWidget(self.GCNtoanBo)


        self.verticalLayout_16.addWidget(self.GCNList)


        self.verticalLayout_20.addWidget(self.capGiayCn)

        self.theoDoiKiLuat = QFrame(self.iconExpand_wg)
        self.theoDoiKiLuat.setObjectName(u"theoDoiKiLuat")
        self.theoDoiKiLuat.setFrameShape(QFrame.StyledPanel)
        self.theoDoiKiLuat.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.theoDoiKiLuat)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.KLbut = QPushButton(self.theoDoiKiLuat)
        self.KLbut.setObjectName(u"KLbut")
        self.KLbut.setCheckable(True)

        self.verticalLayout_18.addWidget(self.KLbut)

        self.KLlist = QFrame(self.theoDoiKiLuat)
        self.KLlist.setObjectName(u"KLlist")
        self.KLlist.setFrameShape(QFrame.StyledPanel)
        self.KLlist.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.KLlist)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.KLlanDau = QPushButton(self.KLlist)
        self.KLlanDau.setObjectName(u"KLlanDau")
        self.KLlanDau.setMinimumSize(QSize(0, 18))
        self.KLlanDau.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.KLlanDau.setCheckable(True)

        self.verticalLayout_19.addWidget(self.KLlanDau)

        self.KLtungDonvi = QPushButton(self.KLlist)
        self.KLtungDonvi.setObjectName(u"KLtungDonvi")
        self.KLtungDonvi.setMinimumSize(QSize(0, 18))
        self.KLtungDonvi.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.KLtungDonvi.setCheckable(True)

        self.verticalLayout_19.addWidget(self.KLtungDonvi)

        self.KLtheoNam = QPushButton(self.KLlist)
        self.KLtheoNam.setObjectName(u"KLtheoNam")
        self.KLtheoNam.setMinimumSize(QSize(0, 18))
        self.KLtheoNam.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.KLtheoNam.setCheckable(True)

        self.verticalLayout_19.addWidget(self.KLtheoNam)

        self.KLkhoangTime = QPushButton(self.KLlist)
        self.KLkhoangTime.setObjectName(u"KLkhoangTime")
        self.KLkhoangTime.setMinimumSize(QSize(0, 18))
        self.KLkhoangTime.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.KLkhoangTime.setCheckable(True)

        self.verticalLayout_19.addWidget(self.KLkhoangTime)

        self.KLngayCapCN = QPushButton(self.KLlist)
        self.KLngayCapCN.setObjectName(u"KLngayCapCN")
        self.KLngayCapCN.setMinimumSize(QSize(0, 18))
        self.KLngayCapCN.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.KLngayCapCN.setCheckable(True)

        self.verticalLayout_19.addWidget(self.KLngayCapCN)

        self.KLtoanBo = QPushButton(self.KLlist)
        self.KLtoanBo.setObjectName(u"KLtoanBo")
        self.KLtoanBo.setMinimumSize(QSize(0, 18))
        self.KLtoanBo.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"	font-size:11px;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298;\n"
"}")
        self.KLtoanBo.setCheckable(True)

        self.verticalLayout_19.addWidget(self.KLtoanBo)


        self.verticalLayout_18.addWidget(self.KLlist)


        self.verticalLayout_20.addWidget(self.theoDoiKiLuat)


        self.verticalLayout_21.addLayout(self.verticalLayout_20)

        self.verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.set2 = QPushButton(self.iconExpand_wg)
        self.set2.setObjectName(u"set2")
        self.set2.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	border-radius:3px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/settings2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icons/settings1.png", QSize(), QIcon.Normal, QIcon.On)
        self.set2.setIcon(icon6)
        self.set2.setIconSize(QSize(200, 20))
        self.set2.setCheckable(True)

        self.verticalLayout_2.addWidget(self.set2)

        self.q2 = QPushButton(self.iconExpand_wg)
        self.q2.setObjectName(u"q2")
        self.q2.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	border-radius:3px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/signout2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icons/signout1.png", QSize(), QIcon.Normal, QIcon.On)
        self.q2.setIcon(icon7)
        self.q2.setIconSize(QSize(200, 20))
        self.q2.setCheckable(True)

        self.verticalLayout_2.addWidget(self.q2)


        self.verticalLayout_21.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.iconExpand_wg, 0, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.headerWg = QWidget(self.centralwidget)
        self.headerWg.setObjectName(u"headerWg")
        self.horizontalLayout_7 = QHBoxLayout(self.headerWg)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.headerWg)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border:none;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon8)
        self.pushButton.setIconSize(QSize(39, 45))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label = QLabel(self.headerWg)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_22.addWidget(self.label)

        self.label_5 = QLabel(self.headerWg)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_22.addWidget(self.label_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_22)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_5 = QSpacerItem(198, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit = QLineEdit(self.headerWg)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 31))
        self.lineEdit.setMaximumSize(QSize(16777215, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	padding-left:20px;\n"
"    border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.lineEdit)

        self.label_6 = QLabel(self.headerWg)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/icons/profile.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_6)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.headerWg)

        self.MainWg = QWidget(self.centralwidget)
        self.MainWg.setObjectName(u"MainWg")
        self.MainWg.setMinimumSize(QSize(871, 751))
        self.MainWg.setMaximumSize(QSize(5000, 751))
        self.MainWg.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(131, 255, 189);\n"
"	color:white;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.MainWg)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.MainWg)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(5000, 16777215))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.KL4P = QWidget()
        self.KL4P.setObjectName(u"KL4P")
        self.stackedWidget.addWidget(self.KL4P)
        self.TK3P = QWidget()
        self.TK3P.setObjectName(u"TK3P")
        self.stackedWidget.addWidget(self.TK3P)
        self.CN5P = QWidget()
        self.CN5P.setObjectName(u"CN5P")
        self.stackedWidget.addWidget(self.CN5P)
        self.CN4P = QWidget()
        self.CN4P.setObjectName(u"CN4P")
        self.stackedWidget.addWidget(self.CN4P)
        self.CN3P = QWidget()
        self.CN3P.setObjectName(u"CN3P")
        self.stackedWidget.addWidget(self.CN3P)
        self.CN2P = QWidget()
        self.CN2P.setObjectName(u"CN2P")
        self.stackedWidget.addWidget(self.CN2P)
        self.LC3P = QWidget()
        self.LC3P.setObjectName(u"LC3P")
        self.stackedWidget.addWidget(self.LC3P)
        self.LC2P = QWidget()
        self.LC2P.setObjectName(u"LC2P")
        self.stackedWidget.addWidget(self.LC2P)
        self.LC1P = QWidget()
        self.LC1P.setObjectName(u"LC1P")
        self.stackedWidget.addWidget(self.LC1P)
        self.TK8P = QWidget()
        self.TK8P.setObjectName(u"TK8P")
        self.stackedWidget.addWidget(self.TK8P)
        self.TK7P = QWidget()
        self.TK7P.setObjectName(u"TK7P")
        self.stackedWidget.addWidget(self.TK7P)
        self.TK6P = QWidget()
        self.TK6P.setObjectName(u"TK6P")
        self.stackedWidget.addWidget(self.TK6P)
        self.TK5P = QWidget()
        self.TK5P.setObjectName(u"TK5P")
        self.stackedWidget.addWidget(self.TK5P)
        self.TK4P = QWidget()
        self.TK4P.setObjectName(u"TK4P")
        self.stackedWidget.addWidget(self.TK4P)
        self.TK2P = QWidget()
        self.TK2P.setObjectName(u"TK2P")
        self.label_8 = QLabel(self.TK2P)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(228, 140, 111, 61))
        self.label_8.setStyleSheet(u"background-color: rgb(15, 15, 15);")
        self.stackedWidget.addWidget(self.TK2P)
        self.setP = QWidget()
        self.setP.setObjectName(u"setP")
        self.stackedWidget.addWidget(self.setP)
        self.KL6P = QWidget()
        self.KL6P.setObjectName(u"KL6P")
        self.stackedWidget.addWidget(self.KL6P)
        self.KL5P = QWidget()
        self.KL5P.setObjectName(u"KL5P")
        self.stackedWidget.addWidget(self.KL5P)
        self.KL3P = QWidget()
        self.KL3P.setObjectName(u"KL3P")
        self.stackedWidget.addWidget(self.KL3P)
        self.KL2P = QWidget()
        self.KL2P.setObjectName(u"KL2P")
        self.stackedWidget.addWidget(self.KL2P)
        self.KL1P = QWidget()
        self.KL1P.setObjectName(u"KL1P")
        self.stackedWidget.addWidget(self.KL1P)
        self.CN6P = QWidget()
        self.CN6P.setObjectName(u"CN6P")
        self.stackedWidget.addWidget(self.CN6P)
        self.Tk1P = QWidget()
        self.Tk1P.setObjectName(u"Tk1P")
        self.label_7 = QLabel(self.Tk1P)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(230, 170, 411, 161))
        self.label_7.setStyleSheet(u"background-color: rgb(9, 9, 9);")
        self.stackedWidget.addWidget(self.Tk1P)
        self.CN1P = QWidget()
        self.CN1P.setObjectName(u"CN1P")
        self.stackedWidget.addWidget(self.CN1P)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.MainWg)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.TKbut.toggled.connect(self.tkList.setHidden)
        self.luanChuyenBut.toggled.connect(self.lcList.setHidden)
        self.GCNbut.toggled.connect(self.GCNList.setHidden)
        self.KLbut.toggled.connect(self.KLlist.setHidden)
        self.TKbut.toggled.connect(self.tkIcon.setChecked)
        self.luanChuyenBut.toggled.connect(self.LCicon.setChecked)
        self.GCNbut.toggled.connect(self.CGicon.setChecked)
        self.KLbut.toggled.connect(self.TDicon.setChecked)
        self.set2.toggled.connect(self.set1.setChecked)
        self.q2.toggled.connect(self.q1.setChecked)
        self.q1.toggled.connect(MainWindow.close)
        self.q2.toggled.connect(MainWindow.close)
        self.pushButton.toggled.connect(self.iconExpand_wg.setHidden)
        self.pushButton.toggled.connect(self.icoOnly_wg.setVisible)

        self.stackedWidget.setCurrentIndex(13)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.tkIcon.setText("")
        self.LCicon.setText("")
        self.CGicon.setText("")
        self.TDicon.setText("")
        self.set1.setText("")
        self.q1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SQL QUERY TOOL FOR ACCESS", None))
        self.TKbut.setText(QCoreApplication.translate("MainWindow", u"TH\u1ed0NG K\u00ca", None))
        self.tkCapLanDau.setText(QCoreApplication.translate("MainWindow", u"1. C\u1ea5p L\u1ea7n \u0110\u1ea7u", None))
        self.tkCapTungDonvi.setText(QCoreApplication.translate("MainWindow", u"2. C\u1ea5p Gi\u1ea5y T\u1eebng \u0110\u01a1n V\u1ecb", None))
        self.tkTheoNam.setText(QCoreApplication.translate("MainWindow", u"3. C\u1ea5p Theo N\u0103m", None))
        self.tkTheoKhoangTime.setText(QCoreApplication.translate("MainWindow", u"4. C\u1ea5p Theo Kho\u1ea3ng Th\u1eddi Gian", None))
        self.tkTheoNgayCN.setText(QCoreApplication.translate("MainWindow", u"5. C\u1ea5p Theo Ng\u00e0y C\u1ea5p CN", None))
        self.tkToanBo.setText(QCoreApplication.translate("MainWindow", u"6. C\u1ea5p Gi\u1ea5y To\u00e0n B\u1ed9 C\u00e1c \u0110\u01a1n V\u1ecb", None))
        self.tkDanhSachDKV.setText(QCoreApplication.translate("MainWindow", u"7. Danh S\u00e1ch \u0110KV To\u00e0n B\u1ed9", None))
        self.tkLuanChuyenSum.setText(QCoreApplication.translate("MainWindow", u"8. Th\u1ed1ng K\u00ea Lu\u00e2n Chuy\u1ec3n", None))
        self.luanChuyenBut.setText(QCoreApplication.translate("MainWindow", u"LU\u00c2N CHUY\u1ec2N", None))
        self.LCNhap.setText(QCoreApplication.translate("MainWindow", u"1. Nh\u1eadp Lu\u00e2n Chuy\u1ec3n", None))
        self.LCKiemTraSuaChua.setText(QCoreApplication.translate("MainWindow", u"2. Ki\u1ec3m Tra S\u1eeda Ch\u1eefa", None))
        self.LCKiemtraDKV.setText(QCoreApplication.translate("MainWindow", u"3. Ki\u1ec3m Tra S\u1ed1 L\u01b0\u1ee3ng DC, \u0110KV", None))
        self.GCNbut.setText(QCoreApplication.translate("MainWindow", u"C\u1ea4P GI\u1ea4Y CN", None))
        self.GCNcapLanDau.setText(QCoreApplication.translate("MainWindow", u"1. H\u1ed3 S\u01a1 G\u1ed1c", None))
        self.GCNtungDonvi.setText(QCoreApplication.translate("MainWindow", u"2. Gi\u1ea5y Ch\u1ee9ng Nh\u1eadn \u0110KV", None))
        self.GCNtheoNam.setText(QCoreApplication.translate("MainWindow", u"3. Q\u0110CN : Nh\u1eadp, S\u1eeda Danh S\u00e1ch", None))
        self.GCNkhoangTime.setText(QCoreApplication.translate("MainWindow", u"4. Q\u0110CN : In \u1ea4n", None))
        self.GCNngayCapCN.setText(QCoreApplication.translate("MainWindow", u"5. Ki\u1ec3m Tra C\u1ea5p Gi\u1ea5y CN", None))
        self.GCNtoanBo.setText(QCoreApplication.translate("MainWindow", u"------------------------------------------", None))
        self.KLbut.setText(QCoreApplication.translate("MainWindow", u"THEO D\u00d5I K\u1ef6 LU\u1eacT", None))
        self.KLlanDau.setText(QCoreApplication.translate("MainWindow", u"1. Nh\u1eadp K\u1ef7 Lu\u1eadt \u0110KV", None))
        self.KLtungDonvi.setText(QCoreApplication.translate("MainWindow", u"2. Ki\u1ec3m Tra Theo S\u1ed1 Q\u0110", None))
        self.KLtheoNam.setText(QCoreApplication.translate("MainWindow", u"3. Ki\u1ec3m Tra Theo T\u00ean \u0110KV", None))
        self.KLkhoangTime.setText(QCoreApplication.translate("MainWindow", u"4. Nh\u1eadp K\u1ef7 Lu\u1eadt \u0110\u01a1n V\u1ecb \u0110K", None))
        self.KLngayCapCN.setText(QCoreApplication.translate("MainWindow", u"5. Ki\u1ec3m Tra K\u1ef7 Lu\u1eadt \u0110V Theo M\u00e3", None))
        self.KLtoanBo.setText(QCoreApplication.translate("MainWindow", u"6. Ki\u1ec3m Tra K\u1ef7 Lu\u1eadt \u0110V Theo S\u1ed1 Q\u0110", None))
        self.set2.setText("")
        self.q2.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello , Guys", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Welcome To Your Page", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type something ... ", None))
        self.label_6.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TK2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Cap lan dau", None))
    # retranslateUi

