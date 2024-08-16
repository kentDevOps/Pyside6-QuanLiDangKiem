from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow,QMenu, QWidget
from PySide6.QtGui import QAction
from PySide6.QtCore import QPoint
from ui_index import Ui_MainWindow

class MySideBar(QMainWindow,Ui_MainWindow):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle ("SQL Access Tool")

    #Hide Widget menu
        self.icoOnly_wg.setHidden(True)
    #Hide Dropdown
        self.tkList.setHidden(True)
        self.lcList.setHidden(True)
        self.GCNList.setHidden(True)
        self.KLlist.setHidden(True)
    #conect button to chuyen Page
        # Phần Thống Kê 
        self.tkCapLanDau.clicked.connect(self.chuyenPageTK1)
        self.tkCapTungDonvi.clicked.connect(self.chuyenPageTk2)
        self.tkTheoNam.clicked.connect(self.chuyenPageTk3)
        self.tkTheoKhoangTime.clicked.connect(self.chuyenPageTk4)
        self.tkTheoNgayCN.clicked.connect(self.chuyenPageTk5)
        self.tkToanBo.clicked.connect(self.chuyenPageTk6)
        self.tkDanhSachDKV.clicked.connect(self.chuyenPageTk7)
        self.tkLuanChuyenSum.clicked.connect(self.chuyenPageTk8)     
        # Phần Luân Chuyển
        self.LCNhap.clicked.connect(self.chuyenPageLC1)
        self.LCKiemTraSuaChua.clicked.connect(self.chuyenPageLC2)
        self.LCKiemtraDKV.clicked.connect(self.chuyenPageLC3)     
        # Phần Cấp Giấy CHứng Nhận
        self.GCNcapLanDau.clicked.connect(self.chuyenPageCN1)
        self.GCNtungDonvi.clicked.connect(self.chuyenPageCN2)
        self.GCNtheoNam.clicked.connect(self.chuyenPageCN3)   
        self.GCNkhoangTime.clicked.connect(self.chuyenPageCN4)
        self.GCNngayCapCN.clicked.connect(self.chuyenPageCN5)
        #self.GCNtoanBo.clicked.connect(self.chuyenPageCN6)     
        # Phần Kỉ Luật
        self.KLlanDau.clicked.connect(self.chuyenPageKl1)
        self.KLtungDonvi.clicked.connect(self.chuyenPageKl2)
        self.KLtheoNam.clicked.connect(self.chuyenPageKl3)   
        self.KLkhoangTime.clicked.connect(self.chuyenPageKl4)
        self.KLngayCapCN.clicked.connect(self.chuyenPageKl5)
        self.KLtoanBo.clicked.connect(self.chuyenPageKl6)                                        
    #conect button to respective context menu
        self.tkIcon.clicked.connect(self.thongke_context)
        self.LCicon.clicked.connect(self.luanChuyen_context)   
        self.CGicon.clicked.connect(self.capGiay_context) 
        self.TDicon.clicked.connect(self.kiLuat_context)
    # Conect page of stack
        ##----> Phần Thống Kê
    def chuyenPageTK1(self):
        self.stackedWidget.setCurrentWidget(self.Tk1P)
    def chuyenPageTk2(self):      
        self.stackedWidget.setCurrentWidget(self.TK2P)
    def chuyenPageTk3(self):      
        self.stackedWidget.setCurrentWidget(self.TK3P)
    def chuyenPageTk4(self):       
        self.stackedWidget.setCurrentWidget(self.TK4P)
    def chuyenPageTk5(self):     
        self.stackedWidget.setCurrentWidget(self.TK5P)
    def chuyenPageTk6(self):      
        self.stackedWidget.setCurrentWidget(self.TK6P)
    def chuyenPageTk7(self):       
        self.stackedWidget.setCurrentWidget(self.TK7P)
    def chuyenPageTk8(self):      
        self.stackedWidget.setCurrentWidget(self.TK8P)  
        # Phần Luân Chuyển
    def chuyenPageLC1(self):
        self.stackedWidget.setCurrentWidget(self.LC1P)
    def chuyenPageLC2(self):       
        self.stackedWidget.setCurrentWidget(self.LC2P)
    def chuyenPageLC3(self): 
        self.stackedWidget.setCurrentWidget(self.LC3P)  
        # Phần Cấp Giấy CN
    def chuyenPageCN1(self):
        self.stackedWidget.setCurrentWidget(self.CN1P)
    def chuyenPageCN2(self):       
        self.stackedWidget.setCurrentWidget(self.CN2P)
    def chuyenPageCN3(self): 
        self.stackedWidget.setCurrentWidget(self.CN3P)                                                
    def chuyenPageCN4(self):
        self.stackedWidget.setCurrentWidget(self.CN4P)
    def chuyenPageCN5(self):       
        self.stackedWidget.setCurrentWidget(self.CN5P)
    '''def chuyenPageCN6(self): 
        self.stackedWidget.setCurrentWidget(self.CN6P)'''     
        # Phần Theo Dõi Kỉ Luật
    def chuyenPageKl1(self):
        self.stackedWidget.setCurrentWidget(self.KL1P)
    def chuyenPageKl2(self):       
        self.stackedWidget.setCurrentWidget(self.KL2P)
    def chuyenPageKl3(self): 
        self.stackedWidget.setCurrentWidget(self.KL3P)                                                
    def chuyenPageKl4(self):
        self.stackedWidget.setCurrentWidget(self.KL4P)
    def chuyenPageKl5(self):       
        self.stackedWidget.setCurrentWidget(self.KL5P)
    def chuyenPageKl6(self): 
        self.stackedWidget.setCurrentWidget(self.KL6P)              
    # Show context menu from IconOnly Widget
    def thongke_context(self):
        self.show_custom_menu(self.tkIcon,["1. Cấp Lần Đầu","2. Cấp Giấy Từng Đơn Vị","3. Cấp Theo Năm",
                                                "4. Cấp Theo Khoảng Thời Gian","5. Cấp Theo Ngày Cấp CN",
                                                "6. Cấp Giấy Toàn Bộ Các Đơn Vị","7. Danh Sách ĐKV Toàn Bộ",
                                                "8. Thống Kê Luân Chuyển"],100,75)
    def luanChuyen_context(self):
        self.show_custom_menu(self.LCicon,["1. Nhập Luân Chuyển","2. Kiểm Tra Sửa Chữa","3. Kiểm Tra Số Lượng DC, ĐKV"],100,125)
    def capGiay_context(self):
        self.show_custom_menu(self.CGicon,["1. Hồ Sơ Gốc","2. Giấy Chứng Nhận ĐKV","3. QĐCN : Nhập, Sửa Danh Sách",
                                           "4. QĐCN : In Ấn","5. Kiểm Tra Cấp Giấy CN"],100,180)
    def kiLuat_context(self):
        self.show_custom_menu(self.TDicon,["1. Nhập Kỷ Luật ĐKV","2. Kiểm Tra Theo Số QĐ","3. Kiểm Tra Theo Tên ĐKV",
                                           "4. Nhập Kỷ Luật Đơn Vị ĐK","5. Kiểm Tra Kỷ Luật ĐV Theo Mã",
                                           "6. Kiểm Tra Kỷ Luật ĐV Theo Số QĐ"],100,240)           
    def show_custom_menu(self,button,menu_item,Xpos,Ypos):
        menu = QMenu(self)
        # Set style Sheet
        menu.setStyleSheet("""
                           QMenu{
                           background-color: black;
                           color:white;
                           }
                           QMenu:selected{
                           background-color: White;
                           color:#12B298;
                           }                           
                           """)
        # Add action to menu
        for item in menu_item:
            Action = QAction(item,self)
            Action.triggered.connect(self.handle_click)
            menu.addAction(Action)
        #show menu
        #menu.move(button.mapToGlobal(button.rect().topRight()- QPoint(30, -11)))
        '''left_margin = 30  # Khoảng cách từ lề trái
        top_margin = 5   # Khoảng cách từ lề trên

        # Tính toán vị trí mới
        new_position = button.mapToGlobal(button.rect().topLeft()) + QPoint(left_margin, top_margin)
        menu.move(new_position)    '''   
        # Tính toán tọa độ toàn cục của giao diện chính
        main_window_pos = self.mapToGlobal(QPoint(0, 0))
        # Tính toán tọa độ của menu
        menu_pos = main_window_pos + QPoint(Xpos, Ypos)

        # Di chuyển menu tới vị trí tính toán được
        menu.move(menu_pos) 
        menu.exec()
    def handle_click(self):
        text = self.sender().text()
        if text == "1. Cấp Lần Đầu":
            self.chuyenPageTK1()
        elif text == "2. Cấp Giấy Từng Đơn Vị":
            self.chuyenPageTk2()
        elif text == "3. Cấp Theo Năm":
            self.chuyenPageTk3()
        elif text == "4. Cấp Theo Khoảng Thời Gian":
            self.chuyenPageTk4()
        elif text == "5. Cấp Theo Ngày Cấp CN":
            self.chuyenPageTk5()
        elif text == "6. Cấp Giấy Toàn Bộ Các Đơn Vị":
            self.chuyenPageTk6()
        elif text == "7. Danh Sách ĐKV Toàn Bộ":
            self.chuyenPageTk7()
        elif text == "8. Thống Kê Luân Chuyển":
            self.chuyenPageTk8()  

        elif text == "1. Nhập Luân Chuyển":
            self.chuyenPageLC1()
        elif text == "2. Kiểm Tra Sửa Chữa":
            self.chuyenPageLC2()
        elif text == "3. Kiểm Tra Số Lượng DC, ĐKV":
            self.chuyenPageLC3()  

        elif text == "1. Hồ Sơ Gốc":
            self.chuyenPageCN1()
        elif text == "2. Giấy Chứng Nhận ĐKV":
            self.chuyenPageCN2()
        elif text == "3. QĐCN : Nhập, Sửa Danh Sách":
            self.chuyenPageCN3() 
        elif text == "4. QĐCN : In Ấn":
            self.chuyenPageCN4()
        elif text == "5. Kiểm Tra Cấp Giấy CN":
            self.chuyenPageCN5() 

        elif text == "1. Nhập Kỷ Luật ĐKV":
            self.chuyenPageKl1()
        elif text == "2. Kiểm Tra Theo Số QĐ":
            self.chuyenPageKl2()
        elif text == "3. Kiểm Tra Theo Tên ĐKV":
            self.chuyenPageKl3() 
        elif text == "4. Nhập Kỷ Luật Đơn Vị ĐK":
            self.chuyenPageKl4()
        elif text == "5. Kiểm Tra Kỷ Luật ĐV Theo Mã":
            self.chuyenPageKl5()
        elif text == "6. Kiểm Tra Kỷ Luật ĐV Theo Số QĐ":
            self.chuyenPageKl6()              