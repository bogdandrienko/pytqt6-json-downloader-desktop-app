import datetime
import sys
import threading
import time
from PyQt6 import QtWidgets
from image_or_json_downloader import image_downloader, json_downloader
from weather_or_currency_monitoring import weather_monitoring, currency_monitoring
from image_or_video_scanner import image_scanner, video_scanner
from data_analyse import data_analyse

"""
Readme:
* Детальное описание проекта (стек технологий)
* Как использовать
* Как развернуть этот проект
* Gif

Доработка:
* Дизайн (средний) QtDesigner
* Функционал (многопоточность)

* Загрузчик картинок или json-файлов - вы указываете ссылку, он скачивает файл и записывает его в папку.

* Мониторинг погоды и курса валют - настольное приложение для вывода в реальном времени выбранных данных.

* Парсер цен в электронном магазине: вы указываете категорию и алгоритм сканирует все товары в этой категории и 
записывает в excel-файл в формате "товар-цена".

* Сканер папок с изображениями: есть одна папка, в ней надо найти только людей и вырезать эти файлы в другую папку.

* Анализатор видеофайлов или видео с веб-камеры и поиск жестов, вывод их на экран.

* Выведение суммы, среднего, моды..., а также их отображение pyplot, значений из файла, используя numpy
"""


class PyQtWindow(QtWidgets.QWidget):
    def __init__(self, window_title: str):
        super().__init__()

        global headers
        self.headers = headers

        self.play = True

        self.layout = QtWidgets.QGridLayout(self)

        self.label_url = QtWidgets.QLabel("url")
        self.layout.addWidget(self.label_url, 0, 0)

        self.line_edit_url = QtWidgets.QLineEdit("https://jsonplaceholder.typicode.com/todos/")
        self.layout.addWidget(self.line_edit_url, 1, 0)

        self.label_status = QtWidgets.QLabel("...")
        self.layout.addWidget(self.label_status, 0, 1)

        self.button_start = QtWidgets.QPushButton("start download")
        self.button_start.clicked.connect(self.start_weather_monitoring)
        self.layout.addWidget(self.button_start, 1, 3)

        self.setWindowTitle(window_title)
        self.resize(640, 480)
        self.show()

    def start(self):
        self.play = True

        self.label_status.setText("идёт загрузка")
        new_thread = threading.Thread(target=self.start_data_analyse)
        new_thread.start()

    def stop(self):
        self.play = False

    def finish(self, message="загрузка завершена"):
        self.label_status.setText(f"{message} [{datetime.datetime.now().strftime('%H:%M:%S')}]")

    def start_json_download(self):
        try:
            url = str(self.line_edit_url.text())
            json_downloader.start(url=url, headers=self.headers)
            self.finish()
        except Exception as error:
            self.finish(f"ошибка: {error}")

    def start_image_download(self):
        try:
            image_downloader.start(url="https://picsum.photos/370/250", headers=self.headers)
            self.finish()
        except Exception as error:
            self.finish(f"ошибка: {error}")

    def start_weather_monitoring(self):
        try:
            while self.play:
                time.sleep(2.0)
                weather_monitoring.start(url="https://www.gismeteo.kz/weather-astana-5164/", headers=self.headers)
                self.finish()
        except Exception as error:
            self.finish(f"ошибка: {error}")

    def start_currency_monitoring(self):
        try:
            while self.play:
                time.sleep(2.0)
                currency_monitoring.start(url="https://api.coincap.io/v2/assets/", headers=self.headers)
                self.finish()
        except Exception as error:
            self.finish(f"ошибка: {error}")

    def start_image_scanner(self):
        try:
            image_scanner.start()
            self.finish()
        except Exception as error:
            self.finish(f"ошибка: {error}")

    def start_video_scanner(self):
        try:
            video_scanner.start()
            self.finish()
        except Exception as error:
            self.finish(f"ошибка: {error}")

    def start_data_analyse(self):
        try:
            data_analyse.start()
            self.finish()
        except Exception as error:
            self.finish(f"ошибка: {error}")


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }

    pyqt_app = QtWidgets.QApplication([])
    pyqt_ui = PyQtWindow("пример приложений python")
    sys.exit(pyqt_app.exec())
