from signal import signal
import sys, os, configparser, log
from win10toast import ToastNotifier
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll
    appid = 'buggsoftware.supersearch.sub.1'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)
except ImportError:
    pass

def read_user_config():
    #Read Main Config File
    global defaultURL
    config = configparser.ConfigParser()
    config.read('MainConfig.ini')
    defaultURL = config['DEFAULT']['Default_URL']

def desktop_notification():
    n = ToastNotifier()
    


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(defaultURL))
        self.setCentralWidget(self.browser)
        self.showMaximized()


        #Status Bar Setup
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.bookmarkButton = QPushButton('Bookmarks')
        self.statusBar.addWidget(self.bookmarkButton)
        self.bookmarkButton.clicked.connect(self.bookmarksPage)


        #Navbar Stuff
        navbar = QToolBar()
        self.addToolBar(navbar)

        prevBtn = QAction('<', self)
        prevBtn.triggered.connect(self.browser.back)
        navbar.addAction(prevBtn)

        nextBtn = QAction('>', self)
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)

        refreshBtn = QAction('Refresh', self)
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)

        homeBtn = QAction('Home', self)
        homeBtn.triggered.connect(self.home)
        navbar.addAction(homeBtn)

        navbar.setMovable(False)

        self.searchBar = QLineEdit()
        self.searchBar.returnPressed.connect(self.loadUrl)
        navbar.addWidget(self.searchBar)
        self.browser.urlChanged.connect(self.updateUrl)

    def home(self):
        self.browser.setUrl(QUrl(defaultURL))

    def loadUrl(self):
        url = self.searchBar.text()
        self.browser.setUrl(QUrl(url))

    def updateUrl(self, url):
        self.searchBar.setText(url.toString())

    def bookmarksPage():
        pass

    def navigate(self, url):
        self.searchBar.setText(url.toString())


if __name__ == '__main__':
    read_user_config
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(basedir, 'icon.ico')))
    QApplication.setApplicationName('SuperSearch')
    MainWin = MainWindow()
    app.exec()