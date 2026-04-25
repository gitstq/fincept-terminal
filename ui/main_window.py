#!/usr/bin/env python3
"""Main window for Fincept Terminal"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QTabWidget, QMenuBar, QMenu, QAction, QStatusBar
)
from PyQt6.QtCore import Qt
from ui.dashboard import Dashboard
from ui.chart_view import ChartView
from ui.settings import Settings
import logging

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    """Main window class for Fincept Terminal"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fincept Terminal")
        self.setGeometry(100, 100, 1200, 800)
        
        self.setup_ui()
        self.setup_menu()
        self.setup_status_bar()
        
        logger.info("Main window initialized")
    
    def setup_ui(self):
        """Set up the main UI"""
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        
        # Create tab widget
        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)
        
        # Add tabs
        self.dashboard = Dashboard()
        self.chart_view = ChartView()
        self.settings = Settings()
        
        self.tab_widget.addTab(self.dashboard, "Dashboard")
        self.tab_widget.addTab(self.chart_view, "Charts")
        self.tab_widget.addTab(self.settings, "Settings")
    
    def setup_menu(self):
        """Set up the menu bar"""
        menu_bar = QMenuBar()
        self.setMenuBar(menu_bar)
        
        # File menu
        file_menu = QMenu("File", self)
        menu_bar.addMenu(file_menu)
        
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # View menu
        view_menu = QMenu("View", self)
        menu_bar.addMenu(view_menu)
        
        # Help menu
        help_menu = QMenu("Help", self)
        menu_bar.addMenu(help_menu)
        
        about_action = QAction("About", self)
        help_menu.addAction(about_action)
    
    def setup_status_bar(self):
        """Set up the status bar"""
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_bar.showMessage("Ready")
