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

    @staticmethod
    def handle_response(response, indent=4):
        content_type = response.headers['content-type']
        if content_type == 'text/html':
            return response.text
        elif 'application/json' in content_type:
            return json.dumps(response.json(),indent=indent)
        else:
            return f'Content type of {content_type} not implemented.'

    def make_request(self):

        method=self.ui.methodCombo.currentText()             # has been checked

        if method in ["GET", "DELETE", "OPTIONS"]:
            body = None
        elif method in ["POST", "PUT"]:
            try:
                body = json.loads(self.ui.requestEdit.toPlainText()) # has been checked
            except ValueError:
                self.ui.responseViewer.setText('Invalid request body: please enter valid json.')
                return

        uri = self.ui.uriEdit.text()                         # has been checked
        verify = self.ui.verifySsl.isChecked()
        
        try:
            output = self.handle_response(requests.request(url=uri,method=method,json=body,verify=verify))
        except requests.exceptions.SSLError:
            output = "SSL validation failed, are you behind a MITM proxy? De-select 'SSL Verify' if you are confident in the security and privacy of your conneciton (do so at your own risk!)"
        
        self.ui.responseViewer.setText(output)
            


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
