# This Python file uses the following encoding: utf-8
import sys
import requests
import json

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.methodCombo.currentTextChanged.connect(self.configure_request_body_input)
        self.ui.sendBtn.clicked.connect(self.make_request)

    @staticmethod
    def validate_body(body):
        return True

    def make_request(self):

        method=self.ui.methodCombo.currentText()             # has been checked

        if method in ["GET", "DELETE", "OPTIONS"]:
            body = None
        elif method in ["POST", "PUT"]:
            body = json.loads(self.ui.requestEdit.toPlainText()) # has been checked

        if validate_body(body):
            uri = self.ui.uriEdit.text()                         # has been checked
            response = requests.request(url=uri,method=method,json=body,verify=False)
            self.ui.responseViewer.setText(response.text)
        else:
            print('Error - invalid request body')


    def configure_request_body_input(self):

        method=self.ui.methodCombo.currentText()

        if method in ["GET", "DELETE", "OPTIONS"]: #then we shouldn't use request body
            self.ui.requestEdit.setReadOnly(True)

        else:
            self.ui.requestEdit.setReadOnly(False)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
