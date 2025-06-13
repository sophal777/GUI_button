from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import QPropertyAnimation, QRect
import sys

class CustomLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom GUI Layout")
        self.setGeometry(100, 100, 500, 400)
        layout = QVBoxLayout()

        self.zoom_in = QPushButton("zoom_in 30%")
        layout.addWidget(self.zoom_in)
        self.setLayout(layout)

        self.state = 0
        self.zoom_in.clicked.connect(self.Start1)

    def Start1(self):
        x = self.x()
        y = self.y()

        if self.state == 0:
            self.zoom_in.setText("zoom_in 70%")
            target_geometry = QRect(x, y, 700, 600)
            self.state = 1
        elif self.state == 1:
            self.zoom_in.setText("Reset")
            target_geometry = QRect(x, y, 1200, 1000)
            self.state = 2
        else:
            self.zoom_in.setText("zoom_in 30%")
            target_geometry = QRect(x, y, 500, 400)
            self.state = 0

        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(500)
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(target_geometry)
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomLayout()
    window.show()
    sys.exit(app.exec_())
