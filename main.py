import asyncio
import datetime
import json
import os
import shutil
import sys
import threading
import aiohttp
from PyQt6 import QtWidgets


class PyQtWindow(QtWidgets.QWidget):
    def __init__(self, window_title: str):
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)

        self.label_url = QtWidgets.QLabel("url")
        self.layout.addWidget(self.label_url, 0, 0)

        self.line_edit_url = QtWidgets.QLineEdit("https://jsonplaceholder.typicode.com/todos/")
        self.layout.addWidget(self.line_edit_url, 1, 0)

        self.label_status = QtWidgets.QLabel("...")
        self.layout.addWidget(self.label_status, 0, 1)

        self.button_start = QtWidgets.QPushButton("start download")
        self.button_start.clicked.connect(self.start)
        self.layout.addWidget(self.button_start, 1, 3)

        self.setWindowTitle(window_title)
        self.resize(640, 480)
        self.show()

    def start(self):
        self.label_status.setText("идёт загрузка")
        new_thread = threading.Thread(target=self.start_download)
        new_thread.start()

    def finish(self, message="загрузка завершена"):
        self.label_status.setText(f"{message} [{datetime.datetime.now().strftime('%H:%M:%S')}]")

    def start_download(self):
        try:
            try:
                shutil.rmtree("data")
            except Exception as error:
                pass
            os.mkdir("data")

            url = str(self.line_edit_url.text())
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/102.0.0.0 Safari/537.36'
            }

            async def download():
                async with aiohttp.ClientSession() as session:
                    async with session.get(url=url, headers=headers) as resp_object:
                        response = await resp_object.json()

                        if not isinstance(response, list):
                            response = [response]

                        for index, json_obj in enumerate(response, 1):
                            with open(f'data/data{json_obj["id"]}_{datetime.datetime.now().strftime("%H_%M")}.json',
                                      'w') as file:
                                json.dump(json_obj, file)

                        self.finish()

            asyncio.run(download())
        except Exception as error:
            self.finish(f"ошибка: {error}")


if __name__ == '__main__':
    pyqt_app = QtWidgets.QApplication([])
    pyqt_ui = PyQtWindow("загрузчик json")

    sys.exit(pyqt_app.exec())
