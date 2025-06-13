from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSpinBox, QComboBox
import sys

name_button = [
    "Button1", "Button2", "Button3", "Button4", "Button5",
    "Button6", "Button7", "Button8", "sophal",
    "Button10", "Button11", "Button12"
]

def my_b(self, max_per_row=5, Create_button=12):
    start_x = 50
    start_y = 100
    x_spacing = 120
    y_spacing = 50

    for i in range(Create_button):
        row = i // max_per_row
        col = i % max_per_row
        x = start_x + col * x_spacing
        y = start_y + row * y_spacing
        name = name_button[i]
        button_main(self, x, y, name)

def button(x, y):
    width = 110
    height = 35
    return (x, y, width, height)

def button_main(self, x, y, name):
    btn = QPushButton(name, self)
    btn.setGeometry(*button(x, y))
    method_name = f"{name}_{x}_{y}"
    if hasattr(self, method_name):
        btn.clicked.connect(getattr(self, method_name))
    else:
        print(f"Method {method_name} not found.")

def sin(self, name_sin="Threads", start_x=50, start_y=50):
    spinbox = QSpinBox(self)
    spinbox.setRange(1, 12)
    spinbox.setValue(5)
    spinbox.setGeometry(start_x, start_y, 110, 35)
    spinbox.setPrefix(f"{name_sin}: ")
    setattr(self, name_sin, spinbox)

def comb(self, name_com="ComboBox", start_x=50, start_y=400, Items=None):
    if Items is None:
        Items = ["Female_Male", "Female", "Male"]
    combo = QComboBox(self)
    combo.addItems(Items)
    combo.setGeometry(start_x, start_y, 110, 35)
    setattr(self, name_com, combo)

class CustomLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dynamic Buttons with Line Wrap")
        self.setGeometry(800, 100, 700, 600)

        # Create ComboBox
        comb(self, name_com="ComboBox", start_x=50, start_y=400)

        # Create Buttons
        my_b(self, max_per_row=5, Create_button=12)

        # Create SpinBoxes
        sin(self, "Threads", start_x=50, start_y=50)
        sin(self, "LOOP", start_x=180, start_y=50)

    def Button1_50_100(self):
        loop = self.LOOP.value()
        threads = self.Threads.value()
        gender = self.ComboBox.currentText()
        print(f"Button1 clicked → LOOP: {loop}, THREADS: {threads}, Gender: {gender}")

    def Button2_170_100(self): print("Button2 clicked")
    def Button3_290_100(self): print("Button3 clicked")
    def Button4_410_100(self): print("Button4 clicked")
    def Button5_530_100(self): print("Button5 clicked")
    def Button6_50_150(self): print("Button6 clicked")
    def Button7_170_150(self): print("Button7 clicked")
    def Button8_290_150(self): print("Button8 clicked")
    def sophal_410_150(self): print("Sophal clicked")
    def Button10_530_150(self): print("Button10 clicked")
    def Button11_50_200(self): print("Button11 clicked")
    def Button12_170_200(self): print("Button12 clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomLayout()
    window.show()
    sys.exit(app.exec_())
