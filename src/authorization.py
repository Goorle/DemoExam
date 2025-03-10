from PyQt5.QtWidgets import QDialog
from .window.authorization_window import Ui_AuthorizationWindow

class Authorization(QDialog, Ui_AuthorizationWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

