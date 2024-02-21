from PyQt5.QtWidgets import * 
import PyQt5
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from pathlib import Path
import sys
import random
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
points = 0
plus = 1
upgrade_cost = 20
pps_cost = 50
pps_ingame = 0
pps = 0
jackpot_pts1 = 50
jackpot_cost1 = 25
jackpot_pts2 = 35000
jackpot_cost2 = 15000
jackpot_pts3 = 1000000
jackpot_cost3 = 150000
chance1 = float(1/2) * 100
chance2 = float(1/8) * 100
chance3 = float(1/50) * 100
level = 0

class MainWindow(QWidget):
    def __init__(self) -> None:
        global points
        global pps
        super(MainWindow, self).__init__()
        # changing the background color to grey
        self.setStyleSheet("background-color: grey;") 
        self.setGeometry(0, 0, 1280, 720) 

        self.button_upgrade = QPushButton("Upgrade \nnext upgrade: " + f"{upgrade_cost:,}" + "\nmultiplier: " + f"{plus:,}", self)
        self.button_upgrade.setFont(QFont('Arial', 28))
        self.button_upgrade.clicked.connect(self.upgrade_pressed)

        self.button_pps = QPushButton("Passive Income! \nnext upgrade: " + f"{pps_cost:,}", self)
        self.button_pps.setFont(QFont('Arial', 24))
        self.button_pps.clicked.connect(self.pps_pressed)

        # this abomination is the text that displays the score
        self.points_label = QLabel("Points: \n" + f"{points:,}", self)
        self.points_label.setFont(QFont('Arial', 36))
        self.points_label.setAlignment(Qt.AlignCenter)
        self.points_label.setStyleSheet("color: white")
        self.points_label.resize(100,50)

        # the goofy ass button that increases the score
        self.button = QPushButton("Click me!", self)
        self.button.setFont(QFont('Arial', 28))
        self.button.clicked.connect(self.button_pressed)

        # this shit displays the points per second or something
        self.pps_label = QLabel("Points Per Second: " + f"{pps:,}", self)
        self.pps_label.setFont(QFont('Arial', 24))
        self.pps_label.setAlignment(Qt.AlignCenter)

        self.jackpot_button1 = QPushButton("Click to get " + f"{jackpot_pts1:,}" + " Points!\n" + str(chance1) + "% Chance\nCost: " + f"{jackpot_cost1:,}", self)
        self.jackpot_button1.setFont(QFont('Arial', 24))
        self.jackpot_button1.clicked.connect(jackpot_def1)

        self.jackpot_button2 = QPushButton ("Click to get " + f"{jackpot_pts2:,}" + " Points!\n"+ str(chance2) + "% Chance\nCost: " + f"{jackpot_cost2:,}", self)
        self.jackpot_button2.setFont(QFont('Arial', 24))
        self.jackpot_button2.clicked.connect(jackpot_def2)

        self.jackpot_button3 = QPushButton("Click to get " + f"{jackpot_pts3:,}" + " Points!\n" + str(chance3) + "% Chance\nCost: " + f"{jackpot_cost3:,}", self)
        self.jackpot_button3.setFont(QFont('Arial', 24))
        self.jackpot_button3.clicked.connect(jackpot_def3)

        self.level_label = QLabel("Level: " + str(level))
        self.level_label.setFont(QFont('Arial', 36))
        self.level_label.setAlignment(Qt.AlignCenter)

        # layout for all this crap
        self.layout = QGridLayout()
        self.layout.addWidget(self.button_upgrade, 0, 0)
        self.layout.addWidget(self.points_label, 1, 1)
        self.layout.addWidget(self.level_label, 0, 1)
        self.layout.addWidget(self.button, 2, 1)
        self.layout.addWidget(self.pps_label, 1, 2)
        self.layout.addWidget(self.button_pps, 1, 0)
        self.layout.addWidget(self.jackpot_button1, 0, 3)
        self.layout.addWidget(self.jackpot_button2, 1, 3)
        self.layout.addWidget(self.jackpot_button3, 2, 3)
        self.setLayout(self.layout)

        timer = QTimer(self)
        timer.timeout.connect(pps_func)
        timer.start(1000)

    def button_pressed(button_pressed):
        global points
        global pps
        points += plus
        print(f"{points:,}")
        mw.points_label.setText("Points: \n" + f"{points:,}")
    
    # why tf you no work?
    def upgrade_pressed(upgrade_pressed):
        global points
        global plus
        global upgrade_cost
        if points >= upgrade_cost:
            points -= upgrade_cost
            global level
            level += 1
            plus *= 6
            upgrade_cost *= 8
            print("current multiplicator: ", f"{plus:,}")
            print("current upgrade_cost: ", f"{upgrade_cost:,}")
            mw.button_upgrade.setText("Upgrade \nnext upgrade: " + f"{upgrade_cost:,}" + "\nmultiplier: " + f"{plus:,}")
            mw.level_label.setText("Level: " + str(level))
        else:
            print("Not enough Points!")
    upgrade_pressed(upgrade_pressed)

    def pps_pressed(pps_pressed):
        global points
        global pps_ingame
        global pps_cost
        if points >= pps_cost:
            points -= pps_cost
            pps_ingame += 1 + (pps_ingame*4)
            pps_cost *= 6
            
            print("current Points Per Second: " + f"{pps_ingame:,}")
            mw.button_pps.setText("Passive Income! \nnext upgrade: " + f"{pps_cost:,}")
            mw.pps_label.setText("Points Per Second: " + f"{pps_ingame:,}")
            pps_func()
        else:
            print("Not enough Points!")
        
def pps_func():
    global points
    global pps_ingame
    points += pps_ingame
    mw.points_label.setText("Points: \n" + f"{points:,}")

def jackpot_def1():
    global points
    global jackpot_cost1
    global jackpot_pts1
    if mw.jackpot_button1.pressed:
        if points >= jackpot_cost1:
            choice = random.randint(1,2)
            print(choice)
            if choice == 1:
                print("You won!")
                points += jackpot_pts1
                jackpot_cost1 *= 2
                jackpot_pts1 *= 2
                mw.jackpot_button1.setText("Click to get " + f"{jackpot_pts1:,}" + " Points!\n" + str(chance1) + "% Chance\nCost: " + f"{jackpot_cost1:,}")
            else:
                points -= jackpot_cost1
                print("You lost!")
                print(jackpot_cost1)
                jackpot_cost1 *= 2
                jackpot_pts1 *= 2
                mw.jackpot_button1.setText("Click to get " + f"{jackpot_pts1:,}" + " Points!\n" + str(chance1) + "% Chance\nCost: " + f"{jackpot_cost1:,}")
    else:
        print("not pressed.")

def jackpot_def2():
    global points
    if mw.jackpot_button2.pressed:
        global jackpot_pts2
        global jackpot_cost2
        if points >= jackpot_cost2:
            choice2 = random.randint(1,8)
            print(choice2)
            if choice2 == 1:
                print("You won!")
                points += jackpot_pts2
                jackpot_cost2 *= 2
                jackpot_pts2 *= 2
                mw.jackpot_button2.setText("Click to get " + f"{jackpot_pts2:,}" + " Points!\n"+ str(chance2) + "% Chance\nCost: " + f"{jackpot_cost2:,}")
            else:
                print("You lost!")
                points -= jackpot_cost2
                jackpot_cost2 *= 2
                jackpot_pts2 *= 2
                mw.jackpot_button2.setText("Click to get " + f"{jackpot_pts2:,}" + " Points!\n"+ str(chance2) + "% Chance\nCost: " + f"{jackpot_cost2:,}")
    else:
        print("not pressed.")

def jackpot_def3():
    global points
    if mw.jackpot_button3.pressed:
        global jackpot_cost3
        global jackpot_pts3
        if points >= jackpot_cost3:
            choice3 = random.randint(1,50)
            print(choice3)
            if choice3 == 1:
                print("You won!")
                points += jackpot_pts3
                jackpot_cost3 *= 2
                jackpot_pts3 *= 2
                mw.jackpot_button3.setText("Click to get " + f"{jackpot_pts3:,}" + " Points!\n" + str(chance3) + "% Chance\nCost: " + f"{jackpot_cost3:,}")
            else:
                print("You lost!")
                points -= jackpot_cost3
                jackpot_cost3 *= 2
                jackpot_pts3 *= 2
                mw.jackpot_button3.setText("Click to get " + f"{jackpot_pts3:,}" + " Points!\n" + str(chance3) + "% Chance\nCost: " + f"{jackpot_cost3:,}")
    else:
        print("not pressed.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    print(PyQt5.QtWidgets.QStyleFactory.keys())
    app.setStyleSheet(Path('style.css').read_text())
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())