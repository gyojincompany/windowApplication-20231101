import sys

#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import * #위 버튼 다 불러올때 * 사용
from PyQt5.QtGui import QIcon #아이콘 불러오기

from PyQt5 import uic #Qt 다자인에서 만든 ui를 연결 시켜주는 라이브러리

form_class = uic.loadUiType("ui/mainUi.ui")[0]#첫번째 유아이 의례써줌 나중 경로파일만 변경해 주면됨

class MyWin(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)#제작해 놓은 유아이를 불러오기

        self.setWindowTitle('연습 프로그램')
        self.setWindowIcon(QIcon('img/google.png'))#윈도우 아이콘
        self.statusBar().showMessage('Test Program v0.5 2023-11-01')

        self.btn1.clicked.connect(self.btn1_clicked) # 버튼1이 클릭되면 메서드 btn1_clicked 호출
        self.btn2.clicked.connect(self.btn2_clicked) # 버튼2이 클릭되면 메서드 btn2_clicked 호출

    def btn1_clicked(self): # 버튼1번이 클릭되었을때 실행될 메서드
        print("버튼1번이 클릭되었습니다!!")

    def btn2_clicked(self): # 버튼2번이 클릭되었을때 실행될 메서드
        print("버튼2번이 클릭되었습니다!!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWin()

    ex.show()
    sys.exit(app.exec_())