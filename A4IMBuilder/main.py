import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QListWidget, QTextEdit, 
                             QLabel, QStackedWidget, QListWidgetItem, QCheckBox,
                             QProgressBar, QMessageBox)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QTimer, Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QFont, QLinearGradient, QColor, QPalette, QIcon
from collections import OrderedDict

from mainmenu_widget import MainMenuWidget
from gitbuilding_widget import GitBuildingWindow
from gitbuilding_setup import GitBuildingSetup



class GitFileReaderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A4IM GitBuilding")
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        
        self.main_menu = MainMenuWidget(self)
        self.git_building = GitBuildingWindow(self)
        
        self.central_widget.addWidget(self.main_menu)
        self.central_widget.addWidget(self.git_building)
        
        # setup gitbuilding
        self.git_building_runner = GitBuildingSetup()
        self.git_building_runner.log.connect(self.on_git_building_log)

        self.run_git_building()

        self.show_main_menu()
        
        self.systems = {}
        self.system_order = []  # New attribute to track system order
        self.progress_bar = None  # Initialize progress_bar to None

   
    def run_git_building(self):
        # You might want to disable UI elements here
        self.git_building_runner.run()


    def on_git_building_log(self, message):
        # You can update a QTextEdit or similar widget to show the log
        print(message)  # For now, just print to console

    def show_main_menu(self):
        self.central_widget.setCurrentWidget(self.main_menu)


    def show_git_building(self, system):
        self.git_building.load_module(system)
        self.central_widget.setCurrentWidget(self.git_building)

 
    def update_progress(self, value):
        if self.progress_bar is not None:
            self.progress_bar.setValue(value)
        else:
            print(f"Progress update: {value}%")


if __name__ == "__main__":
    app = QApplication(sys.argv + ['--disable-seccomp-filter-sandbox'])
    window = GitFileReaderApp()
    window.show()
    sys.exit(app.exec_())