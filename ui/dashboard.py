#!/usr/bin/env python3
"""Dashboard for Fincept Terminal"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QFrame, QGridLayout, QPushButton
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import logging

logger = logging.getLogger(__name__)

class Dashboard(QWidget):
    """Dashboard widget for market overview"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        logger.info("Dashboard initialized")
    
    def setup_ui(self):
        """Set up the dashboard UI"""
        main_layout = QVBoxLayout(self)
        
        # Header
        header = QLabel("Market Overview")
        header.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        main_layout.addWidget(header)
        
        # Market cards grid
        grid_layout = QGridLayout()
        main_layout.addLayout(grid_layout)
        
        # Market indices
        indices = [
            ("S&P 500", "4,567.89", "+0.23%"),
            ("NASDAQ", "14,234.56", "+0.45%"),
            ("Dow Jones", "35,123.45", "-0.12%"),
            ("Bitcoin", "$67,890.00", "+1.23%"),
        ]
        
        for i, (name, value, change) in enumerate(indices):
            card = self.create_market_card(name, value, change)
            grid_layout.addWidget(card, i // 2, i % 2)
        
        # Quick actions
        actions_layout = QHBoxLayout()
        main_layout.addLayout(actions_layout)
        
        quick_actions = ["Add Symbol", "Create Watchlist", "Run Analysis"]
        for action in quick_actions:
            btn = QPushButton(action)
            actions_layout.addWidget(btn)
    
    def create_market_card(self, name, value, change):
        """Create a market data card"""
        card = QFrame()
        card.setFrameShape(QFrame.Shape.Box)
        card.setStyleSheet("border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px;")
        
        layout = QVBoxLayout(card)
        
        name_label = QLabel(name)
        name_label.setFont(QFont("Arial", 12))
        layout.addWidget(name_label)
        
        value_label = QLabel(value)
        value_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        layout.addWidget(value_label)
        
        change_label = QLabel(change)
        if change.startswith("+"):
            change_label.setStyleSheet("color: green;")
        else:
            change_label.setStyleSheet("color: red;")
        layout.addWidget(change_label)
        
        return card
