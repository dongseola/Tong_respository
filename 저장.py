import pickle
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit, QGridLayout, QMessageBox)
from PyQt5.QtCore import Qt

class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'

        self.scdb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        # make button
        addButton = QPushButton("Add", self)
        belButton = QPushButton("Del", self)
        findButton = QPushButton("Find", self)
        incButton = QPushButton("Inc", self)
        showButton = QPushButton("show", self)

        addButton.clicked.connect(self.addAction)
        belButton.clicked.connect(self.delAction)
        findButton.clicked.connect(self.findAction)
        incButton.clicked.connect(self.incAction)
        showButton.clicked.connect(self.showScoreDB)

        # =======================================================
        # make label name
        name = QLabel('Name:')
        age = QLabel('Age:')
        score = QLabel('Score:')
        Amount = QLabel('Amount:')
        Result = QLabel('Result:')
        key = QLabel('Key:')

        # make label box
        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.AmountEdit = QLineEdit()
        self.ResultEdit = QTextEdit()

        self.keybox = QComboBox()
        # key정하는 박스 만들기
        self.keybox.addItem("Name")
        self.keybox.addItem("Age")
        self.keybox.addItem("Score")

        # ========================================================

        self.hbox1 = QHBoxLayout()
        # 1번째 줄
        self.hbox1.addWidget(name)
        self.hbox1.addWidget(self.nameEdit, 1)
        self.hbox1.addWidget(age)
        self.hbox1.addWidget(self.ageEdit, 1)
        self.hbox1.addWidget(score)
        self.hbox1.addWidget(self.scoreEdit, 1)

        self.hbox2 = QHBoxLayout()
        # 2번째 줄
        self.hbox2.addStretch(1)
        self.hbox2.addStretch(1)
        self.hbox2.addWidget(Amount)
        self.hbox2.addWidget(self.AmountEdit, 1)
        self.hbox2.addWidget(key)
        self.hbox2.addWidget(self.keybox)

        self.hbox3 = QHBoxLayout()
        # 3번째 줄
        self.hbox3.addStretch(1)
        self.hbox3.addWidget(addButton)
        self.hbox3.addWidget(belButton)
        self.hbox3.addWidget(findButton)
        self.hbox3.addWidget(incButton)
        self.hbox3.addWidget(showButton)

        self.hbox4 = QHBoxLayout()
        # 4번째 줄
        self.hbox4.addWidget(Result)
        self.hbox4.addStretch(1)

        self.hbox5 = QHBoxLayout()
        # 5번째 줄
        self.hbox5.addWidget(self.ResultEdit, 5)

        self.vbox = QVBoxLayout()
        # 쌓기
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)

        self.setLayout(self.vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()


        # ================================================================

    def closeEvent(self, event):

        self.writeScoreDB()

    def read_score_db(self):
        pass

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        keystand = self.keybox.currentText()
        print_ = ''
        for p in sorted(self.scoredb, key=lambda person: person[keystand]):
            for attr in sorted(p):
                print_ += (str(attr) + "=" + str(p[attr]) + '\t')
            print_ += '\n'

        self.ResultEdit.setPlainText(print_)

    def addAction(self):
        nametext = self.nameEdit.text()
        agetext = self.ageEdit.text()
        scoretext = self.scoreEdit.text()

        if nametext == "" :
            QMessageBox.question(self, 'title', "이름을 입력하십시오", QMessageBox.Yes)

        if agetext.isnumeric()==True and scoretext.isnumeric()==True:
            record = {'Name': nametext, 'Age': int(agetext), 'Score': int(scoretext)}
            self.scoredb += [record]
            self.showScoreDB()
        elif agetext.isnumeric()==False and scoretext.isnumeric()==True:
            QMessageBox.question(self, 'title', "Age에 숫자를 입력해주세요", QMessageBox.Yes)
        elif agetext.isnumeric()==True and scoretext.isnumeric()==False :
            QMessageBox.question(self, 'title', "Score에 숫자를 입력해주세요", QMessageBox.Yes)
        else :
            QMessageBox.question(self, 'title', "숫자를 입력해주세요", QMessageBox.Yes)

    def delAction(self):
        nametext = self.nameEdit.text()

        if nametext == "" :
            QMessageBox.question(self, 'title', "이름을 입력하십시오", QMessageBox.Yes)
        else :
            for k in range(0, len(self.scoredb)):
                for p in (self.scoredb):
                    if p['Name'] == nametext:
                        self.scoredb.remove(p)

            self.showScoreDB()

    def incAction(self):
        nametext = self.nameEdit.text()
        Amaunttext = self.AmountEdit.text()

        if nametext == "":
            QMessageBox.question(self, 'title', "이름을 입력하십시오", QMessageBox.Yes)

        if Amaunttext.isnumeric()==True :
            for p in self.scoredb:
                if p['Name'] == nametext:
                    p['Score'] = int(p['Score']) + int(Amaunttext)
            self.showScoreDB()
        else :
            QMessageBox.question(self, 'title', "Amaunt에 숫자를 입력해주세요", QMessageBox.Yes)


    def findAction(self):
        nametext = self.nameEdit.text()
        dic_find = []
        Print = ''
        for p in self.scoredb:
            if p['Name'] == nametext:
                dic_find += [p]

        for p in sorted(dic_find, key=lambda person: person['Name']):
            for attr in sorted(p):
                Print += str(attr) + "=" + str(p[attr]) + '\t'
            Print += '\n'

        self.ResultEdit.setPlainText(Print)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())