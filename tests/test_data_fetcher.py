#!/usr/bin/env python3
"""Test data fetcher module"""

import pytest
from data.data_fetcher import DataFetcher

class TestDataFetcher:
    """Test DataFetcher class"""
    
    def setup_method(self):
        """Set up test environment"""
        self.fetcher = DataFetcher()
    
    def test_get_stock_data(self):
        """Test get_stock_data method"""
        data = self.fetcher.get_stock_data('AAPL', period='1d', interval='1m')
        assert data is not None
        assert 'Close' in data.columns
        assert not data.empty
    
    def test_get_market_indices(self):
        """Test get_market_indices method"""
        indices = self.fetcher.get_market_indices()
        assert isinstance(indices, dict)
        assert len(indices) > 0
    
    def test_get_crypto_data(self):
        """Test get_crypto_data method"""
        data = self.fetcher.get_crypto_data('BTC-USD', period='1d', interval='1m')
        assert data is not None
        assert 'Close' in data.columns
    
    def test_get_forex_data(self):
        """Test get_forex_data method"""
        data = self.fetcher.get_forex_data('EURUSD=X', period='1d', interval='1m')
        assert data is not None
        assert 'Close' in data.columns
