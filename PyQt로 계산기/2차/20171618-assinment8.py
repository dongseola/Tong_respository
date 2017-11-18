from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad2 import numPadList, operatorList, constantList, functionList
import calcFunctions

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
        # 만약 버튼이 눌었을 때 결과창에 나타나는값 구동 함수
        #num = eval(self.display.text()) #이거 왜 따로 객체를 못만들지???

        # 만약 결과창에 Error!가 뜨면 초기화 한다.
        if self.display.text() == 'Error!':
            self.display.setText('')

        # 버튼이 눌었을 때 날라오는 두 가지 이름 정하기
        button = self.sender()  # 날라오는 값???
        key = button.text()  # button 겉에 쓰여 있는 표시 / 숫자 누를때는 바로 사용가능

        if key == numPadList[11]:
            try:
                result = str(eval(self.display.text()))  # 결과값창의 것을 계산이 후 스트링변화 -> result
            except:
                result = 'Error!'
            self.display.setText(result)  # 결과 값을 창에 넣는다.

        elif key == operatorList[6]:
            self.display.clear()


#index(key)를 사용해서 한줄로 표현 하기
# elif  ==   (x for in) :
        elif [True for x in constantList if key == x]:
            btTcon = [x for x in range(0, 4) if key == constantList[x]]  # constantList이 눌렸을 때
            result_con = str(btTcon)[1]  # 리스트에서 스트링으로 바꾸기
            text_list = ['3.141592', '3E+8', '340', '1.5E+8']
            self.display.setText(self.display.text() + text_list[int(result_con)])

        elif [True for x in functionList if key == x]:
            result_text = eval(self.display.text())
            btTfun = [x for x in range(0, 4) if key == functionList[x]]  # functionList이 눌렸을 때
            result_fun = str(btTfun)[1]  # 리스트에서 스트링으로 바꾸기
            result_list = [calcFunctions.factorial(result_text), calcFunctions.decToBin(result_text),
                           calcFunctions.binToDec(str(result_text)),
                           calcFunctions.decToRoman(result_text)]
            # str bin-> int

            value = result_list[int(result_fun)]
            self.display.setText(str(value))

        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
