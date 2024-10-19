import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
import subprocess

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Person Reidentification System'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label = QLabel(self)
        self.label.move(10, 10)
        self.label.resize(400, 400)

        self.btn = QPushButton('Select Videos', self)
        self.btn.move(420, 10)
        self.btn.clicked.connect(self.selectVideos)

        self.version_label = QLabel('Version:', self)
        self.version_label.move(420, 100)
        self.version_label.resize(60, 20)

        self.version = QLabel('v3', self)
        self.version.move(480, 100)
        self.version.resize(60, 20)

        self.run_btn = QPushButton('Run', self)
        self.run_btn.move(420, 150)
        self.run_btn.resize(100, 40)
        self.run_btn.clicked.connect(self.runSystem)

        self.show()

    def selectVideos(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        videos, _ = QFileDialog.getOpenFileNames(self,"Select Videos", "","Video Files (*.mp4 *.avi)", options=options)
        if videos:
            self.videos = videos
            pixmap = QPixmap(videos[0]).scaledToWidth(400)
            self.label.setPixmap(pixmap)

    def runSystem(self):
        # Activate py37 environment
        activate_path = os.path.join(os.environ['CONDA_PREFIX'], 'Scripts', 'activate.bat')
        env_path = os.path.join(os.environ['CONDA_PREFIX'], 'envs', 'py37')
        command = f"python demo.py --videos {' '.join(self.videos)} --version {self.version.text()}"
        print("command= ",command)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(output.decode('utf-8'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
