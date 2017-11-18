from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad2 import numPadList, operatorList, constantList, functionList
import romkey

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()   # window속의 각 줄의 들어가는 것 만들기
        self.display.setReadOnly(True)  # True 일때만 display를 읽는다.
        self.display.setAlignment(Qt.AlignRight)   #
        self.display.setMaxLength(15)  # 결과를 도출하는 창이 최대 15개 까지 넣을 수 있게 한다.

        # Button Creation and Placement
        numLayout = QGridLayout()   #숫자 키패드
        opLayout = QGridLayout()    #연산자 키패드
        constLayout = QGridLayout()   # 특별한 숫자 예> 파이
        funcLayout = QGridLayout()    # 특혈한 연산자 예> 펙토리알

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }

        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]  # num op constants functions
            for btnText in buttonPad['buttons']:   # keypad2에 있는 리스트
                button = Button(btnText, self.buttonClicked) # 리스트 속에 들어있는 버튼을 눌렀을 때 buttonClicked에 연결

                # 작은 사이즈 각각 layout 완성하기
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1  #지정한 값보다 colom이 커지면 row를 늘리고 colom은 초기화

        # Layout(큰 사이즈인것들 5개)
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def buttonClicked(self):

        if self.display.text() == 'Error!':
            self.display.setText('')

        button = self.sender()
        key = button.text()

        if key == numPadList[11]:
            try:
                result = str(eval(self.display.text()))
            except:
                result = 'Error!'
            self.display.setText(result)

        elif key == operatorList[6]:
            self.display.clear()

        elif [True for x in constantList if key == x]:
            # eval 함수를 숫자로 계산 할 수 없는 경우 에러처리
            try :
                btTcon = constantList.index(key)
                text_list = ['3.141592', '3E+8', '340', '1.5E+8']
                self.display.setText(self.display.text() + text_list[btTcon])
            except :
                self.display.setText("eval Error")

        elif [True for x in functionList if key == x]:
            # eval을 숫자로 계산할 수 없는 경우 에러처리
            try :
                result_text = self.display.text()
                btTfun = functionList.index(key)
                func_list = [romkey.factorial,
                               romkey.decToBin,
                               romkey.binToDec,
                               romkey.decToRoman,
                               romkey.romanToDec]

                func = func_list[btTfun]
                value = func(result_text)
                self.display.setText(str(value))
            except :
                self.display.setText("eval Error")
        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
