import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

from PyQt5 import uic # Qt Designer 에서 만든 ui를 연결시켜주는 라이브러리

form_class = uic.loadUiType("ui/mainUi.ui")[0]
# Qt Designer에서 만든 ui를 불러옴

class MyWin(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # 제작해 놓은 ui를 불러오기
        self.setWindowTitle('연습 프로그램') # 윈도우 타이틀
        self.setWindowIcon(QIcon('img/google.png')) # 윈도우 아이콘

        self.btn1.clicked.connect(self.btn1_clicked)  # 버튼1이 클릭되면 메서드 btn1_clicked 호출
        self.btn2.clicked.connect(self.btn2_clicked)  # 버튼2이 클릭되면 메서드 btn2_clicked 호출
        self.btn3.clicked.connect(self.btn3_clicked)  # 버튼3이 클릭되면 메서드 btn3_clicked 호출


    def btn1_clicked(self):  # 버튼1번이 클릭되었을때 실행될 메서드
        print("버튼1번이 클릭되었습니다!!")

    def btn2_clicked(self):  # 버튼2번이 클릭되었을때 실행될 메서드
        print("버튼2번이 클릭되었습니다!!")

    def btn3_clicked(self):
        user_text = self.lineEdit.text()  # 사용자가 입력한 텍스트 가져오기
        print(user_text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWin()
    ex.show()
    sys.exit(app.exec_())

