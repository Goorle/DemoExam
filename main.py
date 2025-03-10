from PyQt5.QtWidgets import QApplication
from src.authorization import Authorization
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Authorization()
    window.show()
    app.exec()