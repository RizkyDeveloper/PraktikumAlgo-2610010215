import sys
import os
from PyQt5 import QtWidgets, uic
from kelola_buku import KelolaBukuWindow
from pinjam_buku import PinjamBukuWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Ambil folder tempat main.py berada
        base_dir = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(base_dir, 'main.ui'), self)

        self.kelola_buku_win = None

        self.Push_Keluar.clicked.connect(self.close)
        self.Push_Data.clicked.connect(self.open_kelola_buku)
        self.pinjam_buku_win = None
        self.Push_Peminjaman.clicked.connect(self.open_pinjam_buku)

    def open_kelola_buku(self):
        if not self.kelola_buku_win:
            self.kelola_buku_win = KelolaBukuWindow()
        else:
            self.kelola_buku_win.load_books()  # Refresh data saat dibuka lagi
        self.kelola_buku_win.show()
        self.kelola_buku_win.raise_()
        self.kelola_buku_win.activateWindow()

    def open_pinjam_buku(self):
        if self.pinjam_buku_win is None:
            self.pinjam_buku_win = PinjamBukuWindow()
        else:
            self.pinjam_buku_win.load_books_combo()
            self.pinjam_buku_win.load_active_loans()

        self.pinjam_buku_win.show()
        self.pinjam_buku_win.raise_()
        self.pinjam_buku_win.activateWindow()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())