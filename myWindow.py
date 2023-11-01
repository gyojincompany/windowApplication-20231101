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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWin()
    ex.show()
    sys.exit(app.exec_())

