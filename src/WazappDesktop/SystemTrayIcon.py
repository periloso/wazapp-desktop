#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import pyqtSlot as Slot, pyqtSignal as Signal
from PyQt4.QtGui import QSystemTrayIcon, QIcon, QMenu

class SystemTrayIcon(QSystemTrayIcon):
    quit_signal = Signal()
    toggle_main_window_signal = Signal()

    def __init__(self):
        super(SystemTrayIcon, self).__init__()
        self.setIcon(QIcon.fromTheme('tray-offline'))
        menu = QMenu()
        menu.addAction(QIcon.fromTheme('view-minimize'), 'Show/Hide').triggered.connect(self.toggle_main_window_signal)
        menu.addSeparator()
        menu.addAction(QIcon.fromTheme('exit'), 'Quit').triggered.connect(self.quit_signal)
        self.setContextMenu(menu)
        self.show()

    @Slot(bool, bool)
    def statusChanged(self, online, unreadMessages):
        if unreadMessages:
            icon = QIcon.fromTheme('tray-message')
        elif online:
            icon = QIcon.fromTheme('tray-online')
        else:
            icon = QIcon.fromTheme('tray-offline')

        self.setIcon(icon)
