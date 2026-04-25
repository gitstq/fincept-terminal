#!/usr/bin/env python3
"""Fincept Terminal - Main entry point"""

import sys
import logging
from ui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Main function to start the application"""
    try:
        logger.info("Starting Fincept Terminal...")
        
        # Create Qt application
        app = QApplication(sys.argv)
        
        # Create main window
        window = MainWindow()
        window.show()
        
        # Run application
        logger.info("Fincept Terminal started successfully")
        sys.exit(app.exec())
        
    except Exception as e:
        logger.error(f"Error starting Fincept Terminal: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
