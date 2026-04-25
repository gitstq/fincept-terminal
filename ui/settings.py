#!/usr/bin/env python3
"""Settings for Fincept Terminal"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QCheckBox, QComboBox, QPushButton
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import logging

logger = logging.getLogger(__name__)

class Settings(QWidget):
    """Settings widget for Fincept Terminal"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        logger.info("Settings initialized")
    
    def setup_ui(self):
        """Set up the settings UI"""
        main_layout = QVBoxLayout(self)
        
        # Header
        header = QLabel("Settings")
        header.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        main_layout.addWidget(header)
        
        # API Settings
        api_section = QWidget()
        api_layout = QVBoxLayout(api_section)
        api_layout.setContentsMargins(20, 10, 20, 10)
        api_section.setStyleSheet("background-color: #f9f9f9; border-radius: 8px;")
        
        api_header = QLabel("API Settings")
        api_header.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        api_layout.addWidget(api_header)
        
        # Alpha Vantage API Key
        alpha_layout = QHBoxLayout()
        api_layout.addLayout(alpha_layout)
        
        alpha_label = QLabel("Alpha Vantage API Key:")
        alpha_layout.addWidget(alpha_label)
        
        self.alpha_input = QLineEdit()
        self.alpha_input.setPlaceholderText("Enter your API key")
        alpha_layout.addWidget(self.alpha_input)
        
        # News API Key
        news_layout = QHBoxLayout()
        api_layout.addLayout(news_layout)
        
        news_label = QLabel("News API Key:")
        news_layout.addWidget(news_label)
        
        self.news_input = QLineEdit()
        self.news_input.setPlaceholderText("Enter your API key")
        news_layout.addWidget(self.news_input)
        
        main_layout.addWidget(api_section)
        
        # Display Settings
        display_section = QWidget()
        display_layout = QVBoxLayout(display_section)
        display_layout.setContentsMargins(20, 10, 20, 10)
        display_section.setStyleSheet("background-color: #f9f9f9; border-radius: 8px; margin-top: 10px;")
        
        display_header = QLabel("Display Settings")
        display_header.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        display_layout.addWidget(display_header)
        
        # Theme
        theme_layout = QHBoxLayout()
        display_layout.addLayout(theme_layout)
        
        theme_label = QLabel("Theme:")
        theme_layout.addWidget(theme_label)
        
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Light", "Dark", "System"])
        theme_layout.addWidget(self.theme_combo)
        
        # Language
        language_layout = QHBoxLayout()
        display_layout.addLayout(language_layout)
        
        language_label = QLabel("Language:")
        language_layout.addWidget(language_label)
        
        self.language_combo = QComboBox()
        self.language_combo.addItems(["English", "中文", "Español"])
        language_layout.addWidget(self.language_combo)
        
        main_layout.addWidget(display_section)
        
        # Data Settings
        data_section = QWidget()
        data_layout = QVBoxLayout(data_section)
        data_layout.setContentsMargins(20, 10, 20, 10)
        data_section.setStyleSheet("background-color: #f9f9f9; border-radius: 8px; margin-top: 10px;")
        
        data_header = QLabel("Data Settings")
        data_header.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        data_layout.addWidget(data_header)
        
        # Auto-refresh
        refresh_layout = QHBoxLayout()
        data_layout.addLayout(refresh_layout)
        
        self.refresh_check = QCheckBox("Enable auto-refresh")
        refresh_layout.addWidget(self.refresh_check)
        
        self.refresh_combo = QComboBox()
        self.refresh_combo.addItems(["1 minute", "5 minutes", "15 minutes", "30 minutes"])
        refresh_layout.addWidget(self.refresh_combo)
        
        main_layout.addWidget(data_section)
        
        # Save button
        save_btn = QPushButton("Save Settings")
        main_layout.addWidget(save_btn)
