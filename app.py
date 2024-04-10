from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, \
    QMessageBox, QListWidget, QDialog, QLineEdit, QListWidgetItem, QFileDialog
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtCore import Qt
import pandas as pd
import sys


class TodoDialog(QDialog):
    """
    Dialog window to add or edit a todo item.
    """
    def __init__(self, parent=None):
        super(TodoDialog, self).__init__(parent)
        self.setWindowTitle('Add Todo')
        self.todo_edit = QLineEdit()  # Line edit widget to enter todo item
        font = QFont("arial", 11)
        self.todo_edit.setFont(font)
        self.todo_edit.setFixedHeight(25)
        self.ok_button = QPushButton('Ok')
        self.cancel_button = QPushButton('Cancel')

        layout = QVBoxLayout()
        layout.addWidget(self.todo_edit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        self.setLayout(layout)


class TodoListWidget(QWidget):
    """
    Main application window for the Todo List Application.
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Todo List Application")
        self.todo_list = QListWidget()  # List widget to display todo items
        font = QFont("Arial", 11)
        self.todo_list.setFont(font)
        self.add_button = QPushButton('Add')
        self.edit_button = QPushButton('Edit')
        self.delete_button = QPushButton('Delete')
        self.delete_all_button = QPushButton('Delete All')
        self.done_button = QPushButton('Done')
        self.in_progress_button = QPushButton('In Progress')
        self.not_done_button = QPushButton('Not Done')

        layout = QVBoxLayout()
        first_button_layout = QHBoxLayout()
        second_button_layout = QHBoxLayout()

        first_button_layout.addWidget(self.add_button)
        first_button_layout.addWidget(self.edit_button)
        first_button_layout.addWidget(self.delete_button)
        first_button_layout.addWidget(self.delete_all_button)

        second_button_layout.addWidget(self.done_button)
        second_button_layout.addWidget(self.in_progress_button)
        second_button_layout.addWidget(self.not_done_button)

        layout.addLayout(first_button_layout)
        layout.addWidget(self.todo_list)
        layout.addLayout(second_button_layout)

        self.add_button.clicked.connect(self.add_todo)
        self.edit_button.clicked.connect(self.edit_todo)
        self.delete_button.clicked.connect(self.delete_todo)
        self.delete_all_button.clicked.connect(self.delete_all)
        self.done_button.clicked.connect(self.done)
        self.in_progress_button.clicked.connect(self.in_progress)
        self.not_done_button.clicked.connect(self.not_done)

        self.setLayout(layout)

    def add_todo(self):
        """
        Function to add a new todo item.
        """
        dialog = TodoDialog()
        if dialog.exec_():
            todo_name = dialog.todo_edit.text()
            if todo_name:
                self.todo_list.addItem(todo_name)

    def edit_todo(self):
        """
        Function to edit an existing todo item.
        """
        if self.todo_list.currentItem() is None:
            QMessageBox.warning(self, "Error", "You haven't selected any todo to edit")
            return
        current_todo = self.todo_list.currentItem()
        if current_todo:
            dialog = TodoDialog()
            if dialog.exec_():
                edited_todo = dialog.todo_edit.text()
                if edited_todo:
                    current_todo.setText(edited_todo)

    def delete_todo(self):
        """
        Function to delete a selected todo item.
        """
        if self.todo_list.currentItem() is None:
            QMessageBox.warning(self, "Error", "You haven't selected any todo to delete")
            return
        current_todo = self.todo_list.currentItem()
        if current_todo:
            confirm = QMessageBox.question(self, 'Delete todo', 'Are You Sure You Want To Delete?',
                                           QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                self.todo_list.takeItem(self.todo_list.row(current_todo))

    def delete_all(self):
        """
        Function to delete all todo items.
        """
        if self.todo_list.count() == 0:
            QMessageBox.warning(self, "Error", "You don't have any todo to delete")
            return
        confirm = QMessageBox.question(self, 'Delete All', 'Are You Sure You Want To Delete All Todos? ',
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.todo_list.clear()

    def done(self):
        """
        Function to mark a todo item as 'Done'.
        """
        current_todo = self.todo_list.currentItem()
        if current_todo:
            current_todo.setBackground(QBrush(QColor("#8BC34A")))

    def in_progress(self):
        """
        Function to mark a todo item as 'In Progress'.
        """
        current_todo = self.todo_list.currentItem()
        if current_todo:
            current_todo.setBackground(QBrush(QColor("#303F9F")))

    def not_done(self):
        """
        Function to mark a todo item as 'Not Done'.
        """
        current_todo = self.todo_list.currentItem()
        if current_todo:
            current_todo.setBackground(QBrush(QColor("#D32F2F")))


def main():
    app = QApplication(sys.argv)
    todo_list = TodoListWidget()
    todo_list.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
