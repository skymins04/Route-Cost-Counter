import sys, os, re
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGroupBox, QGridLayout, QPushButton, QAction, QLabel, QSpinBox, QTextBrowser, QListWidget, QListWidgetItem, QMessageBox
from PyQt5.QtCore import QSize, Qt, QUrl
from PyQt5.QtGui import QIcon, QPixmap, QTextDocument

class RouteCostCounter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.resize(831, 528)   # init window
        self.setMinimumSize(QSize(831, 528))
        self.setMaximumSize(QSize(831, 528))
        self.setWindowTitle('임베디드 SW 챌린저 경로 분석기')
        icon = QIcon()
        icon.addFile('BetaMan.ico')
        self.setWindowIcon(icon)

        menu = self.menuBar()   # create menu

        menu_file = menu.addMenu('File')
        file_exit = QAction('종료', self)
        file_exit.triggered.connect(lambda:self.close())
        menu_file.addAction(file_exit)

        setRouteGroup = QGroupBox('경로 설정', self)    # create set Route grid Group
        setRouteGroup.setGeometry(20, 40, 651, 331)
        setRouteGridBox = QWidget(setRouteGroup)
        setRouteGridBox.setGeometry(10, 20, 631, 301)
        setRouteGridLayout = QGridLayout(setRouteGridBox)
        setRouteGridLayout.setContentsMargins(0, 0, 0, 0)
        setRouteGridLayout.setHorizontalSpacing(7)
        setRouteGridLayout.setVerticalSpacing(5)
        
        self.point00 = QPushButton('( 0, 0 )')  # create Points & matching grid\
        setRouteGridLayout.addWidget(self.point00,0,0,1,1)
        self.point01 = QPushButton('( 0, 1 )')
        setRouteGridLayout.addWidget(self.point01,0,1,1,1)
        self.point02 = QPushButton('( 0, 2 )')
        setRouteGridLayout.addWidget(self.point02,0,2,1,1)
        self.point03 = QPushButton('( 0, 3 )')
        setRouteGridLayout.addWidget(self.point03,0,3,1,1)
        self.point04 = QPushButton('( 0, 4 )')
        setRouteGridLayout.addWidget(self.point04,0,4,1,1)
        self.point05 = QPushButton('( 0, 5 )')
        setRouteGridLayout.addWidget(self.point05,0,5,1,1)
        self.point06 = QPushButton('( 0, 6 )')
        setRouteGridLayout.addWidget(self.point06,0,6,1,1)

        self.point10 = QPushButton('( 1, 0 )')
        setRouteGridLayout.addWidget(self.point10,1,0,1,1)
        self.point16 = QPushButton('( 1, 6 )')
        setRouteGridLayout.addWidget(self.point16,1,6,1,1)

        self.point20 = QPushButton('( 2, 0 )') 
        setRouteGridLayout.addWidget(self.point20,2,0,1,1)
        self.point26 = QPushButton('( 2, 6 )')
        setRouteGridLayout.addWidget(self.point26,2,6,1,1)

        self.point30 = QPushButton('( 3, 0 )')
        setRouteGridLayout.addWidget(self.point30,3,0,1,1)
        self.point31 = QPushButton('( 3, 1 )')
        setRouteGridLayout.addWidget(self.point31,3,1,1,1)
        self.point32 = QPushButton('( 3, 2 )')
        setRouteGridLayout.addWidget(self.point32,3,2,1,1)
        self.point33 = QPushButton('( 3, 3 )')
        setRouteGridLayout.addWidget(self.point33,3,3,1,1)
        self.point34 = QPushButton('( 3, 4 )')
        setRouteGridLayout.addWidget(self.point34,3,4,1,1)
        self.point35 = QPushButton('( 3, 5 )')
        setRouteGridLayout.addWidget(self.point35,3,5,1,1)
        self.point36 = QPushButton('( 3, 6 )')
        setRouteGridLayout.addWidget(self.point36,3,6,1,1)
        
        self.point40 = QPushButton('( 4, 0 )')
        setRouteGridLayout.addWidget(self.point40,4,0,1,1)
        self.point41 = QPushButton('( 4, 1 )')
        setRouteGridLayout.addWidget(self.point41,4,1,1,1)
        self.point42 = QPushButton('( 4, 2 )')
        setRouteGridLayout.addWidget(self.point42,4,2,1,1)
        self.point43 = QPushButton('( 4, 3 )')
        setRouteGridLayout.addWidget(self.point43,4,3,1,1)
        self.point44 = QPushButton('( 4, 4 )')
        setRouteGridLayout.addWidget(self.point44,4,4,1,1)
        self.point45 = QPushButton('( 4, 5 )')
        setRouteGridLayout.addWidget(self.point45,4,5,1,1)
        self.point46 = QPushButton('( 4, 6 )')
        setRouteGridLayout.addWidget(self.point46,4,6,1,1)

        setConditionGroup = QGroupBox('조건 설정', self)    # create set Condition Group
        setConditionGroup.setGeometry(20, 390, 211, 111)

        label = QLabel('포인트 이동 시간 (초)', setConditionGroup)
        label.setGeometry(20, 30, 131, 21)
        label_2 = QLabel('회전 시간 (초)', setConditionGroup)
        label_2.setGeometry(60, 60, 91, 16)
        self.pointMovetimeSpinbox = QSpinBox(setConditionGroup)
        self.pointMovetimeSpinbox.setGeometry(150, 30, 41, 21)
        self.pointMovetimeSpinbox.setValue(2)
        self.turningTimeSpinbox = QSpinBox(setConditionGroup)
        self.turningTimeSpinbox.setGeometry(150, 58, 42, 20)
        self.turningTimeSpinbox.setValue(1)

        resultGroup = QGroupBox('분석 결과', self)  # create drive result Group 
        resultGroup.setGeometry(250, 390, 421, 111)

        label_4 = QLabel('이동한 포인트 수', resultGroup)
        label_4.setGeometry(76, 17, 91, 16)
        self.pointsNumBrowser = QTextBrowser(resultGroup)
        self.pointsNumBrowser.setGeometry(180, 14, 41, 21)
        self.pointsNumBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pointsNumBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pointsNumBrowser.setOverwriteMode(False)
        self.pointsNumBrowser.setTabStopWidth(75)
        self.pointsNumBrowser.setAcceptRichText(True)
        self.pointsNumBrowser.setOpenExternalLinks(False)
        self.pointsNumBrowser.setHtml('0')

        label_5 = QLabel('포인트 이동 주행 시간 (초)', resultGroup)
        label_5.setGeometry(24, 40, 151, 16)
        self.pointsTimeBrowser = QTextBrowser(resultGroup)
        self.pointsTimeBrowser.setGeometry(180, 37, 41, 21)
        self.pointsTimeBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pointsTimeBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pointsTimeBrowser.setOverwriteMode(False)
        self.pointsTimeBrowser.setTabStopWidth(75)
        self.pointsTimeBrowser.setAcceptRichText(True)
        self.pointsTimeBrowser.setOpenExternalLinks(False)
        self.pointsTimeBrowser.setHtml('0')

        label_7 = QLabel('회전 수', resultGroup)
        label_7.setGeometry(128, 63, 41, 16)
        self.turningTimeBrowser = QTextBrowser(resultGroup)
        self.turningTimeBrowser.setGeometry(180, 83, 41, 21)
        self.turningTimeBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.turningTimeBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.turningTimeBrowser.setOverwriteMode(False)
        self.turningTimeBrowser.setTabStopWidth(75)
        self.turningTimeBrowser.setAcceptRichText(True)
        self.turningTimeBrowser.setOpenExternalLinks(False)
        self.turningTimeBrowser.setHtml('0')

        label_6 = QLabel('회전 주행 시간 (초)', resultGroup)
        label_6.setGeometry(64, 85, 111, 16)
        self.turningNumBrowser = QTextBrowser(resultGroup)
        self.turningNumBrowser.setGeometry(180, 60, 41, 21)
        self.turningNumBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.turningNumBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.turningNumBrowser.setOverwriteMode(False)
        self.turningNumBrowser.setTabStopWidth(75)
        self.turningNumBrowser.setAcceptRichText(True)
        self.turningNumBrowser.setOpenExternalLinks(False)
        self.turningNumBrowser.setHtml('0')

        label_8 = QLabel('총 주행 시간 (초)', resultGroup)
        label_8.setGeometry(240, 40, 91, 16)
        self.DriveTimeBrowser = QTextBrowser(resultGroup)
        self.DriveTimeBrowser.setGeometry(340, 37, 41, 21)
        self.DriveTimeBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DriveTimeBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DriveTimeBrowser.setOverwriteMode(False)
        self.DriveTimeBrowser.setTabStopWidth(75)
        self.DriveTimeBrowser.setAcceptRichText(True)
        self.DriveTimeBrowser.setOpenExternalLinks(False)
        self.DriveTimeBrowser.setHtml('0')

        RouteListGroup = QGroupBox('경로 리스트', self) # create Roupe List Group
        RouteListGroup.setGeometry(690, 40, 121, 461)

        self.routeList = QListWidget(RouteListGroup)
        self.routeList.setGeometry(10, 20, 101, 331)
        self.pointSave = []

        self.clearSelectionListBtn = QPushButton('선택 포인트 제거', RouteListGroup)
        self.clearSelectionListBtn.setGeometry(10, 360, 101, 31)

        self.clearListBtn = QPushButton('리스트 지우기', RouteListGroup)
        self.clearListBtn.setGeometry(10, 390, 101, 31)

        self.startAnalysisBtn = QPushButton('경로 분석', RouteListGroup)
        self.startAnalysisBtn.setEnabled(False)
        self.startAnalysisBtn.setGeometry(10, 420, 101, 31)

        self.point00.clicked.connect(lambda:self.addListItem(self.point00)) # define Event handling
        self.point01.clicked.connect(lambda:self.addListItem(self.point01))
        self.point02.clicked.connect(lambda:self.addListItem(self.point02))
        self.point03.clicked.connect(lambda:self.addListItem(self.point03))
        self.point04.clicked.connect(lambda:self.addListItem(self.point04))
        self.point05.clicked.connect(lambda:self.addListItem(self.point05))
        self.point06.clicked.connect(lambda:self.addListItem(self.point06))

        self.point10.clicked.connect(lambda:self.addListItem(self.point10))
        self.point16.clicked.connect(lambda:self.addListItem(self.point16))

        self.point20.clicked.connect(lambda:self.addListItem(self.point20))
        self.point26.clicked.connect(lambda:self.addListItem(self.point26))

        self.point30.clicked.connect(lambda:self.addListItem(self.point30))
        self.point31.clicked.connect(lambda:self.addListItem(self.point31))
        self.point32.clicked.connect(lambda:self.addListItem(self.point32))
        self.point33.clicked.connect(lambda:self.addListItem(self.point33))
        self.point34.clicked.connect(lambda:self.addListItem(self.point34))
        self.point35.clicked.connect(lambda:self.addListItem(self.point35))
        self.point36.clicked.connect(lambda:self.addListItem(self.point36))

        self.point40.clicked.connect(lambda:self.addListItem(self.point40))
        self.point41.clicked.connect(lambda:self.addListItem(self.point41))
        self.point42.clicked.connect(lambda:self.addListItem(self.point42))
        self.point43.clicked.connect(lambda:self.addListItem(self.point43))
        self.point44.clicked.connect(lambda:self.addListItem(self.point44))
        self.point45.clicked.connect(lambda:self.addListItem(self.point45))
        self.point46.clicked.connect(lambda:self.addListItem(self.point46))

        self.clearSelectionListBtn.clicked.connect(lambda:self.clearSelectionList(self.routeList.currentRow()))
        self.clearListBtn.clicked.connect(lambda:self.clearList())

        self.startAnalysisBtn.clicked.connect(lambda:self.startAnalysis())

        self.show()
    
    def addListItem(self, b):
        item = QListWidgetItem(b.text())
        
        if self.routeList.currentRow() == -1:
            self.routeList.addItem(item)
            self.pointSave.append((int(re.findall('\d+', b.text())[0]),int(re.findall('\d+', b.text())[1])))
        else :
            self.routeList.insertItem(self.routeList.currentRow()+1, item)
            self.routeList.setCurrentRow(self.routeList.currentRow()+1)
            self.pointSave.insert(self.routeList.currentRow(), (int(re.findall('\d+', b.text())[0]),int(re.findall('\d+', b.text())[1])))

        if self.routeList.count() >= 10:
            self.startAnalysisBtn.setEnabled(True)

    def clearList(self):
        self.routeList.clear()
        self.pointSave = []
        self.startAnalysisBtn.setEnabled(False)

    def clearSelectionList(self, index):
        self.routeList.takeItem(index);
        self.pointSave.pop(index)
        if self.routeList.count() < 10:
            self.startAnalysisBtn.setEnabled(False)

    def startAnalysis(self):
        if self.checkAvail()[0] == True:
            result = self.routeAnalysis()

            self.pointsNumBrowser.setHtml('{}'.format(result[0]))
            self.pointsTimeBrowser.setHtml('{}'.format(result[0]*self.pointMovetimeSpinbox.value()))
            self.turningNumBrowser.setHtml('{}'.format(result[1]))
            self.turningTimeBrowser.setHtml('{}'.format(result[1]*self.turningTimeSpinbox.value()))
            self.DriveTimeBrowser.setHtml('{}'.format(result[0]*self.pointMovetimeSpinbox.value()+result[1]*self.turningTimeSpinbox.value()))

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            
            msg.setWindowTitle("경로 유효성 검사")
            msg.setText("설정된 경로가 유효하지 않아 분석을 진행할 수 없습니다.")
            msg.setInformativeText("자세한 정보는 도움말을 참고하세요.")
            msg.exec()

    def checkAvail(self):
        errPck = []
        a = []
        for b in self.pointSave:
            if a == []:
                if b != (0,0):
                    errPck = []
                    errPck = (False,'err1',a,b)
                    return errPck; # err1
                a = b
            else:
                if (a[1] == 0 and b[1] == 0) or (a[1] == 6 and b[1] == 6):
                    if b[0]-1 != a[0] and b[0]+1 != a[0]:
                        errPck = []
                        errPck = (False,'err2',a,b)
                        return errPck # err2
                else:
                    if a[0] != 3 and b[0] != 3 and a[0] != 4 and b[0] != 4:
                        if b[1]-1 != a[1] and b[1]+1 != a[1]:
                            errPck = []
                            errPck = (False,'err3',a,b)
                            return errPck # err3
                    else:
                        if abs(b[0] - a[0]) >= 1 and abs(b[1] - a[1]) >= 1:
                            errPck = []
                            errPck = (False,'err4',a,b)
                            return errPck # err4
                        elif b[1] != a[1]:
                            if b[1]-1 != a[1] and b[1]+1 != a[1] :
                                errPck = []
                                errPck = (False,'err5',a,b)
                                return errPck # err5

                if a == b:
                    errPck = []
                    errPck = (False,'err6',a,b)
                    return errPck; # err6
                a = b
        if b != (4,6):
            errPck = []
            errPck = (False,'err7',a,b)
            return errPck; # err7
        errPck = []
        errPck = (True,'OK',a,b)
        return errPck;

    def routeAnalysis(self):
        a = []
        pointCount = 0
        turnCount = 0
        robotDir = 1 # 1: right, 2: top, 3: left, 4: bottom
        for b in self.pointSave:
            if a != []:
                if (a[0]-1, a[1]) == b: # top
                    if robotDir == 1: 
                        turnCount += 1
                    elif robotDir == 3: 
                        turnCount += 1
                    elif robotDir == 4: 
                        turnCount += 2
                    robotDir = 2
                elif (a[0]+1, a[1]) == b:   # bottom
                    if robotDir == 1: 
                        turnCount += 1
                    elif robotDir == 2:
                        turnCount += 1
                    elif robotDir == 3: 
                        turnCount += 2
                    robotDir = 4
                elif (a[0], a[1]-1) == b:   # left
                    if robotDir == 1: 
                        turnCount += 2
                    elif robotDir == 2: 
                        turnCount += 1
                    elif robotDir == 4: 
                        turnCount += 1
                    robotDir = 3    
                elif (a[0], a[1]+1) == b:   # right
                    if robotDir == 2: 
                        turnCount += 2
                    elif robotDir == 3: 
                        turnCount += 1
                    elif robotDir == 4: 
                        turnCount += 1
                    robotDir = 1
            a = b
            pointCount += 1
        pointCount += 1
        if robotDir == 2:
            turnCount += 1
        elif robotDir == 3:
            turnCount += 2
        elif robotDir == 4:
            turnCount += 1
        
        return (pointCount, turnCount)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RouteCostCounter()
    sys.exit(app.exec_()) # exec is main loop