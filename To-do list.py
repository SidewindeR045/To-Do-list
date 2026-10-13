import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QListWidget, QLineEdit, QPushButton,
)
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 400, 500)
        self.tasks = []
        self.setWindowIcon(QIcon("lol.png"))

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.task_list = QListWidget()
        layout.addWidget(self.task_list)

        input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task...")
        input_layout.addWidget(self.task_input)

        add_button = QPushButton("Add")
        add_button.clicked.connect(self.add_task)
        input_layout.addWidget(add_button)

        layout.addLayout(input_layout)

        delete_button = QPushButton("Delete Selected")
        delete_button.clicked.connect(self.delete_task)
        layout.addWidget(delete_button)

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            self.task_list.addItem(task)
            self.task_input.clear()

    def delete_task(self):
        selected = self.task_list.currentRow()
        if selected >= 0:
            self.task_list.takeItem(selected)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()