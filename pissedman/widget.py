# This Python file uses the following encoding: utf-8
import sys
import requests

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
        self.method = 'GET' # haven't added this drop down selection yet
        self.ui.sendBtn.clicked.connect(self.make_request)

    def make_request(self):
        #body = self.requestEdit.value
        #response = requests.request(method=self.method, url=self.ui.uriEdit.value,json=body)
        uri = self.ui.uriEdit.text()
        response = requests.get(url=uri,verify=False)
        self.ui.responseViewer.setText(response.text)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
