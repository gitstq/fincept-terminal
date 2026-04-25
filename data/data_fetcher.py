#!/usr/bin/env python3
"""Data fetcher for Fincept Terminal"""

import yfinance as yf
import requests
import logging
import time

logger = logging.getLogger(__name__)

class DataFetcher:
    """Class to fetch financial data from various sources"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Fincept Terminal/1.0'
        })
    
    def get_stock_data(self, symbol, period='1d', interval='1m'):
        """Get stock data from Yahoo Finance"""
        try:
            logger.info(f"Fetching stock data for {symbol}, period={period}, interval={interval}")
            ticker = yf.Ticker(symbol)
            data = ticker.history(period=period, interval=interval)
            logger.info(f"Successfully fetched data for {symbol}")
            return data
        except Exception as e:
            logger.error(f"Error fetching stock data: {e}")
            return None
    
    def get_market_indices(self):
        """Get major market indices"""
        indices = {
            '^GSPC': 'S&P 500',
            '^IXIC': 'NASDAQ',
            '^DJI': 'Dow Jones',
            '^RUT': 'Russell 2000'
        }
        
        results = {}
        for symbol, name in indices.items():
            try:
                data = self.get_stock_data(symbol, period='1d', interval='1m')
                if data is not None and not data.empty:
                    latest = data.iloc[-1]
                    previous = data.iloc[-2] if len(data) > 1 else latest
                    close = latest['Close']
                    change = (close - previous['Close']) / previous['Close'] * 100
                    results[name] = {
                        'symbol': symbol,
                        'price': close,
                        'change': change
                    }
            except Exception as e:
                logger.error(f"Error fetching index {name}: {e}")
        
        return results
    
    def get_crypto_data(self, symbol='BTC-USD', period='1d', interval='1m'):
        """Get cryptocurrency data"""
        return self.get_stock_data(symbol, period, interval)
    
    def get_forex_data(self, pair='EURUSD=X', period='1d', interval='1m'):
        """Get forex data"""
        return self.get_stock_data(pair, period, interval)
    
    def get_news(self, query='finance', api_key=None):
        """Get financial news"""
        if not api_key:
            logger.warning("No News API key provided, skipping news fetch")
            return []
        
        try:
            url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
            response = self.session.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get('articles', [])
        except Exception as e:
            logger.error(f"Error fetching news: {e}")
            return []
