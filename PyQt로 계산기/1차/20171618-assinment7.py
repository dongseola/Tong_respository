from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


# 버튼생성을 주로 하는 class를 새로 정의 하였다.
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
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # 입력받는 값이 보이게 하는 곳 만들기
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        #제일 위에(0번째) 2만큼 공간 차지하기
        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        # 9개의 버튼을 생성할 것이다
        self.digitButton = [x for x in range(0, 10)]

        # 숫자가 들어갈 layout 선언
        numLayout = QGridLayout()

        # 1부터 9까지 버튼 만들고 add하기
        for d in range(1, 10):
            self.digitButton[d] = Button('%d' % d, self.buttonClicked)
            numLayout.addWidget(self.digitButton[d], 2-int((d-1)/3), ((d-1)%3))

        # 0버튼 만들고 add하기
        self.digitButton[0] = Button('0', self.buttonClicked)
        numLayout.addWidget(self.digitButton[0], 3, 0)

        # . 과 = 버튼 만들고 add하기
        self.decButton = Button('.',self.buttonClicked)
        self.eqButton = Button('=',self.buttonClicked)
        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        # 제일큰 것에서 1번째 줄, 0번째에 숫자버튼 만든 grid 넣기
        mainLayout.addLayout(numLayout, 1, 0)

        # 사칙연산 기호 넣을 grid 만들기
        opLayout = QGridLayout()

        # 사칙연산 기호 버튼 만들고 add 하기
        list_ = ['*', '/', '+', '-', '(', ')', 'C']
        index = 0
        for s in list_:
            btn = Button(s, self.buttonClicked)
            opLayout.addWidget(btn, index/2, index%2)
            index += 1

        # 제일 큰 것에서 1번째 줄 1번째에 사칙연산버튼 만든 grid 넣기
        mainLayout.addLayout(opLayout, 1, 1)

        # 보이게 제일 큰것 실행 시키기
        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def buttonClicked(self):
        button = self.sender()

        key = button.text()
        if key == '=':
            result = str(eval(self.display.text()))
            self.display.setText(result)
        elif key == 'C':
            self.display.setText('')
        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())