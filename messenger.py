
import time
from datetime import datetime

import requests
from PyQt5 import QtCore, QtGui, QtWidgets

from clientui import Ui_MainWindow


class ExampleApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,url):
        super().__init__()
        self.setupUi(self)

        self.url = url

        self.pushButton.pressed.connect(self.send_messenge)

        self.after = time.time() - 24 * 60 * 60
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messeges)
        self.timer.start(1000)

    def add_text(self,text):
        self.textBrowser.append(text)
        self.textBrowser.repaint()

    def fromat_message(self,message):
        name = message['name']
        text = message['text']
        dt = datetime.fromtimestamp(message['time'])
        dt_beauty = dt.strftime('%Y/%m/%d %H:%M:%S')
        return f'{name} {dt_beauty}\n{text}\n'




    def update_messeges(self):

        try:
            response = requests.get(f'{self.url}messages?after=0', params={'after':self.after})
        except:
            return
        messages = response.json()['messages']
        for message in messages:
            self.add_text(self.fromat_message(message))
            after = message['time']





    def send_messenge(self):
        name = self.lineEditName.text()
        password = self.lineEditPassword.text()
        text =self.lineEditext.text()
        if not name or not password or not text:
            self.add_text("Write all boxes")
            return


        message = {'name': name,
                   'password': password,
                   'text': text}
        try:
            response = requests.post(f'{self.url}send', json=message)
        except:
            self.add_text('Server unreacheble')
            return

        if response.status_code == 200:
             self.lineEditext.setText('')
             self.lineEditext.repaint()
        elif response.status_code == 401:
            self.add_text('Name or password is not correct')
        else:
            self.add_text('Error')

            pass


app = QtWidgets.QApplication([])
window = ExampleApp('http://127.0.0.1:5000/')
window.show()
app.exec_()