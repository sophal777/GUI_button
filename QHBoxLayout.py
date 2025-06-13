from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QSpinBox, QComboBox,
    QVBoxLayout, QHBoxLayout, QGridLayout
)
import sys

BUTTON_NAMES = [
    "Button1", "Button2", "Button3", "Button4", "Button5",
    "Button6", "Button7", "Button8", "sophal",
    "Button10", "Button11", "Button12"
]

def create_buttons(self, layout, max_per_row=5):
    grid_layout = QGridLayout()
    for i, name in enumerate(BUTTON_NAMES):
        btn = QPushButton(name)
        row = i // max_per_row
        col = i % max_per_row
        grid_layout.addWidget(btn, row, col)
        method_name = f"{name}_{row}_{col}"
        if hasattr(self, method_name):
            btn.clicked.connect(getattr(self, method_name))
        else:
            print(f"Method {method_name} not found.")
    layout.addLayout(grid_layout)

def create_spinbox_row(self, layout, label_name="Threads"):
    box = QSpinBox()
    box.setRange(1, 12)
    box.setValue(5)
    box.setPrefix(f"{label_name}: ")
    setattr(self, label_name, box)

    row = QHBoxLayout()
    row.addWidget(box)
    layout.addLayout(row)

def create_combobox_row(self, layout, name="GenderBox", items=None):
    if items is None:
        items = ["Female_Male", "Female", "Male"]
    combo = QComboBox()
    combo.addItems(items)
    setattr(self, name, combo)

    row = QHBoxLayout()
    row.addWidget(combo)
    layout.addLayout(row)

class CustomLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout-Based UI")
        self.setGeometry(800, 100, 800, 600)

        main_layout = QVBoxLayout()

        create_spinbox_row(self, main_layout, "Threads")
        create_spinbox_row(self, main_layout, "LOOP")
        create_combobox_row(self, main_layout, "GenderBox")
        create_buttons(self, main_layout, max_per_row=5)

        self.setLayout(main_layout)

    def Button1_0_0(self):
        print("Button1 clicked")
        print(f"Threads: {self.Threads.value()}, LOOP: {self.LOOP.value()}, Gender: {self.GenderBox.currentText()}")

    def Button2_0_1(self): print("Button2 clicked")
    def Button3_0_2(self): print("Button3 clicked")
    def Button4_0_3(self): print("Button4 clicked")
    def Button5_0_4(self): print("Button5 clicked")
    def Button6_1_0(self): print("Button6 clicked")
    def Button7_1_1(self): print("Button7 clicked")
    def Button8_1_2(self): print("Button8 clicked")
    def sophal_1_3(self): print("sophal clicked")
    def Button10_1_4(self): print("Button10 clicked")
    def Button11_2_0(self): print("Button11 clicked")
    def Button12_2_1(self): print("Button12 clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CustomLayout()
    win.show()
    sys.exit(app.exec_())
