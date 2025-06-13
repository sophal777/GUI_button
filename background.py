import os
import random
import sys
from PyQt5.QtWidgets import (
    QApplication, QPushButton, QLabel, QVBoxLayout, QMainWindow,
    QWidget, QHBoxLayout, QFrame, QGraphicsDropShadowEffect
)
from PyQt5.QtGui import QFont, QColor, QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QGraphicsOpacityEffect
def apply_widget_style(widget, name_color="deepskyblue"):
    style = f"""
        QPushButton {{
            color: {name_color};
            border: 2px solid {name_color};
            border-radius: 20px;
            padding: 6px 12px;
            font-size: 14px;
        }}
        QPushButton:hover {{
            background-color: #222;
        }}
        QPushButton:pressed {{
            background-color: #444;
        }}
    """
    widget.setStyleSheet(style)

    if isinstance(widget, QPushButton):
        icon_dir = "icon"
        for ext in ["png", "ico", "svg"]:
            icon_path = os.path.join(icon_dir, f"{widget.text()}.{ext}")
            if os.path.exists(icon_path):
                widget.setIcon(QIcon(icon_path))
                widget.setIconSize(QSize(40, 40))
                widget.setText("")
                break

class TopFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(100)
        self.setStyleSheet("background-color: black;")

        self.title_label = QLabel("TOOLS AUTO \n DOWNLOAD", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Droid Serif", 26, QFont.Bold))
        font = self.title_label.font()
        font.setItalic(True)
        self.title_label.setFont(font)
        self.Style("#E0240B")

        title_layout = QVBoxLayout()
        title_layout.addWidget(self.title_label)
        self.setLayout(title_layout)

        # ប៊ូតុង
        self.btn1 = QPushButton("1", self)
        self.btn2 = QPushButton("2", self)
        self.btn3 = QPushButton("3", self)
        self.right_buttons = [self.btn1, self.btn2, self.btn3]

        self.btn4 = QPushButton("4", self)
        self.btn5 = QPushButton("5", self)
        self.btn6 = QPushButton("6", self)
        self.left_buttons = [self.btn4, self.btn5, self.btn6]

        for i, btn in enumerate(self.left_buttons + self.right_buttons):
            btn.setFixedSize(40, 40)
            color = "deepskyblue" if i < 3 else "orange"
            apply_widget_style(btn, color)
            btn.raise_()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        spacing = 10
        btn_size = 40

        for i, btn in enumerate(self.left_buttons):
            x = spacing + i * (btn_size + spacing)
            y = (self.height() - btn_size) // 2
            btn.move(x, y)

        x_start = self.width() - (btn_size + spacing) * len(self.right_buttons) - spacing
        y_pos = (self.height() - btn_size) // 2
        for i, btn in enumerate(self.right_buttons):
            x = x_start + i * (btn_size + spacing)
            btn.move(x, y_pos)

    def Style(self, color="#8D7907"):
        glow = QGraphicsDropShadowEffect(self)
        glow.setBlurRadius(25)
        glow.setOffset(0)
        glow.setColor(QColor(color))
        self.title_label.setGraphicsEffect(glow)
        self.title_label.setStyleSheet(f"color: {color};")

    def all_buttons(self):
        return self.left_buttons + self.right_buttons

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MainWindow with Floating Circle Buttons")
        self.setGeometry(800, 100, 700, 600)
        self.setWindowFlags(Qt.FramelessWindowHint)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)

        self.top_frame = TopFrame()
        self.main_layout.addWidget(self.top_frame)

        # 🧠 ឧទាហរណ៍ប្រើ all_buttons
        for i, btn in enumerate(self.top_frame.all_buttons(), 1):
            btn.setToolTip(f"Floating Button {i}")

        h_layout = QHBoxLayout()
        self.main_layout.addLayout(h_layout)

        self.widget1 = self.create_widget1()
        self.widget1.setFixedWidth(150)  # widget1 តូចជាងគេ
        h_layout.addWidget(self.widget1)

        h_layout.addWidget(self.create_widget2())

        self.widget3 = self.create_widget3()
        self.widget3.hide()  # បិទ widget3 តាំងពីដំបូង
        h_layout.addWidget(self.widget3)

    def create_widget1(self):
        widget = QWidget()
        widget.setStyleSheet("background-color: red;")
        layout = QVBoxLayout()
        self.zoom_in = QPushButton("Start")



        self.Another = QPushButton("HOME")
        layout.addWidget(self.zoom_in)
        layout.addWidget(self.Another)
        self.Another.clicked.connect(self.Start_Another)
        self.Another.setCheckable(True)

        self.apply_button_style(self.Another, "#182af2")
        self.zoom_in.clicked.connect(self.Start1)
        self.state = 0

        widget.setLayout(layout)
        return widget
    



    def apply_button_style(self, button, name_color="gold"):
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: black;
                color: {name_color};
                border: 2px solid {name_color};
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: bold;
                font-size: 14px;
            }}
            QPushButton:hover {{
                background-color: #111111;
            }}
            QPushButton:pressed {{
                background-color: #222222;
            }}
        """)


    def Start_Another(self):
        def fade_out_finished():
            self.widget3.hide()

        effect = QGraphicsOpacityEffect()
        self.widget3.setGraphicsEffect(effect)

        animation = QPropertyAnimation(effect, b"opacity")
        animation.setDuration(600)
        animation.setEasingCurve(QEasingCurve.InOutQuad)

        # Randomly choose animation type: 0 = fade only, 1 = fade + slide
        anim_type = random.choice([0, 1])

        if self.Another.isChecked():
            self.Another.setText("ON")
            self.apply_button_style(self.Another, "#f3b519")

            if anim_type == 0:
                # Fade in only
                self.widget3.show()
                effect.setOpacity(0)
                animation.setStartValue(0)
                animation.setEndValue(1)
                animation.start()
            else:
                # Fade + slide in from left
                self.widget3.show()
                effect.setOpacity(0)
                animation.setStartValue(0)
                animation.setEndValue(1)

                pos_anim = QPropertyAnimation(self.widget3, b"pos")
                pos_anim.setDuration(600)
                pos_anim.setEasingCurve(QEasingCurve.InOutQuad)

                start_pos = self.widget3.pos() - QPoint(100, 0)  # ចាប់ផ្តើមរុញចេញខាងឆ្វេង
                end_pos = self.widget3.pos()

                self.widget3.move(start_pos)
                pos_anim.setStartValue(start_pos)
                pos_anim.setEndValue(end_pos)

                animation.start()
                pos_anim.start()

                self.pos_anim = pos_anim  # កុំឲ្យ pos_anim លុប
        else:
            self.Another.setText("HOME")
            self.apply_button_style(self.Another, "#182af2")

            if anim_type == 0:
                # Fade out only
                effect.setOpacity(1)
                animation.setStartValue(1)
                animation.setEndValue(0)
                animation.finished.connect(fade_out_finished)
                animation.start()
            else:
                # Fade + slide out to left
                effect.setOpacity(1)
                animation.setStartValue(1)
                animation.setEndValue(0)

                pos_anim = QPropertyAnimation(self.widget3, b"pos")
                pos_anim.setDuration(600)
                pos_anim.setEasingCurve(QEasingCurve.InOutQuad)

                start_pos = self.widget3.pos()
                end_pos = self.widget3.pos() - QPoint(100, 0)

                pos_anim.setStartValue(start_pos)
                pos_anim.setEndValue(end_pos)

                animation.finished.connect(fade_out_finished)

                animation.start()
                pos_anim.start()

                self.pos_anim = pos_anim  # កុំឲ្យ pos_anim លុប

        self.fade_animation = animation  # កុំឲ្យ animation លុប

    def Start1(self):
        x = self.x()
        y = self.y()

        if self.state == 0:
            self.zoom_in.setText("zoom_in 70%")
            target_geometry = QRect(x, y, 1000, 800)
            self.state = 1
        elif self.state == 1:
            self.zoom_in.setText("Reset")
            target_geometry = QRect(x, y, 1200, 1000)
            self.state = 2
        else:
            self.zoom_in.setText("zoom_in 30%")
            target_geometry = QRect(x, y, 700, 600)
            self.state = 0
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(500)
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(target_geometry)
        self.animation.start()

    def apply_button_style(self, button, name_color="gold"):
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: black;
                color: {name_color};
                border: 2px solid {name_color};
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: bold;
                font-size: 14px;
            }}
            QPushButton:hover {{
                background-color: #111111;
            }}
            QPushButton:pressed {{
                background-color: #222222;
            }}
        """)

    def create_widget2(self):
        widget = QWidget()
        widget.setStyleSheet("background-color: green;")
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Green Button"))
        widget.setLayout(layout)
        return widget

    def create_widget3(self):
        widget = QWidget()
        widget.setStyleSheet("background-color: blue;")
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Blue Button"))
        widget.setLayout(layout)
        return widget
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if hasattr(self, "dragging") and self.dragging:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
