import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QAbstractItemView,
    QPushButton,
)
from PyQt5.QtCore import Qt, QMimeData


class DraggableListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setDefaultDropAction(Qt.CopyAction)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setStyleSheet("QListWidget { min-height: 200px; }")

    # Siapkan "paket" yang berlabel teks biasa saat drag dimulai
    def mimeData(self, items):
        mime = QMimeData()
        mime.setText("\n".join(item.text() for item in items))
        return mime

    def supportedDropActions(self):
        return Qt.CopyAction | Qt.MoveAction

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasText():
            for text in event.mimeData().text().splitlines():
                if text and not self.findItems(text, Qt.MatchExactly):
                    self.addItem(text)
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()


class DragDropDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drag and Drop Demo")
        self.setGeometry(300, 300, 600, 400)

        layout = QHBoxLayout()

        # Left list (source)
        left_container = QVBoxLayout()
        left_container.addWidget(QLabel("Source (drag from here):"))
        self.left_list = DraggableListWidget()
        for item in ["Apple", "Banana", "Cherry", "Date", "Elderberry"]:
            self.left_list.addItem(item)
        left_container.addWidget(self.left_list)

        # Right list (drop target)
        right_container = QVBoxLayout()
        right_container.addWidget(QLabel("Target (drop here):"))
        self.right_list = DraggableListWidget()
        right_container.addWidget(self.right_list)

        clear_btn = QPushButton("Clear Target")
        clear_btn.clicked.connect(self.right_list.clear)
        right_container.addWidget(clear_btn)

        layout.addLayout(left_container)
        layout.addLayout(right_container)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DragDropDemo()
    window.show()
    sys.exit(app.exec_())