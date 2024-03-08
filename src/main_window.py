import sys
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction, QMenuBar, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def createActions(self):
        self.newAction = QAction("&New...", self)
        self.openAction = QAction("&Open...", self)
        self.saveAction = QAction("&Save", self)
        self.importAction = QAction("&Import", self)
        self.exportAction = QAction("&Export", self)
        self.exitAction = QAction("&Exit", self)

        self.undoAction = QAction("&Undo", self)
        self.redoAction = QAction("&Redo", self)
        self.cutAction = QAction("&Cut", self)
        self.copyAction = QAction("&Copy", self)
        self.pasteAction = QAction("&Paste", self)

        self.zoomInAction = QAction("&Zoom In", self)
        self.zoomOutAction = QAction("&Zoom Out", self)
        self.resetZoomAction = QAction("&Reset Zoom", self)
        self.gridViewAction = QAction("&Grid View", self)
        self.listViewAction = QAction("&List View", self)

        self.sampleEffectAction = QAction("&Nothing here", self)
        self.cleanUnusedMediaAction = QAction("&Clean Unused Media", self)
        self.propertiesAction = QAction("&Properties", self)

        self.helpGuideAction = QAction("&Help Guide", self)
        self.reportIssueAction = QAction("&Report Issue", self)
        self.aboutAction = QAction("&About", self)

    def createMenuBar(self):
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        menuBar.font()

        font = menuBar.font()
        font.setPointSize(14)
        menuBar.setFont(font)

        menuBar.setStyleSheet(
            """
            QMenuBar
            {
                background-color: #282828;
                color: #FFFFFF;
            }
            QMenuBar::item
            {
                color: #FFFFFF;
            }
            QMenu::item
            {
                color: #FFFFFF;
            }
            QMenu::item:selected
            {
                background-color: #535353;
            }
            QMenu::item:hover
            {
                background-color: #535353;
            }
            """
        )

        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.importAction)
        fileMenu.addAction(self.exportAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)

        editMenu = menuBar.addMenu("&Edit")
        editMenu.addAction(self.undoAction)
        editMenu.addAction(self.redoAction)
        editMenu.addSeparator()
        editMenu.addAction(self.cutAction)
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)

        viewMenu = menuBar.addMenu("&View")
        viewMenu.addAction(self.zoomInAction)
        viewMenu.addAction(self.zoomOutAction)
        viewMenu.addAction(self.resetZoomAction)
        viewMenu.addSeparator()
        viewMenu.addAction(self.gridViewAction)
        viewMenu.addAction(self.listViewAction)

        toolsMenu = menuBar.addMenu("&Tools")
        audioMenu = QMenu("Audio", self)
        audioMenu.addAction(self.sampleEffectAction)
        videoMenu = QMenu("Video", self)
        videoMenu.addAction(self.sampleEffectAction)
        toolsMenu.addMenu(audioMenu)
        toolsMenu.addMenu(videoMenu)
        toolsMenu.addSeparator()
        toolsMenu.addAction(self.cleanUnusedMediaAction)
        toolsMenu.addAction(self.propertiesAction)

        helpMenu = menuBar.addMenu("&Help")
        helpMenu.addAction(self.helpGuideAction)
        helpMenu.addAction(self.reportIssueAction)
        helpMenu.addSeparator()
        helpMenu.addAction(self.aboutAction)

    def initUI(self):
        self.setWindowTitle('Multimedia Editor v.0.1')
        self.setWindowIcon(QIcon(':/main_window_icon'))
        self.setStyleSheet("background-color: #404040;")
        self.setGeometry(50, 50, 800, 600)

        self.createActions()
        self.createMenuBar()

        self.showMaximized()
