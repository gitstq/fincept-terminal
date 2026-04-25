#!/usr/bin/env python3
"""Test run script for Fincept Terminal"""

import sys
import logging

# Add project root to path
sys.path.insert(0, '/workspace/fincept-terminal')

# Test data fetcher
from data.data_fetcher import DataFetcher
from analysis.technical_analysis import TechnicalAnalysis

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_data_fetcher():
    """Test data fetcher module"""
    logger.info("Testing data fetcher...")
    fetcher = DataFetcher()
    
    # Test stock data
    stock_data = fetcher.get_stock_data('AAPL', period='1d', interval='1m')
    if stock_data is not None and not stock_data.empty:
        logger.info(f"✓ Stock data fetched successfully: {len(stock_data)} rows")
    else:
        logger.error("✗ Failed to fetch stock data")
    
    # Test market indices
    indices = fetcher.get_market_indices()
    if indices and len(indices) > 0:
        logger.info(f"✓ Market indices fetched successfully: {len(indices)} indices")
        for name, data in indices.items():
            logger.info(f"  - {name}: {data['price']:.2f} ({data['change']:.2f}%)")
    else:
        logger.error("✗ Failed to fetch market indices")
    
    # Test crypto data
    crypto_data = fetcher.get_crypto_data('BTC-USD', period='1d', interval='1m')
    if crypto_data is not None and not crypto_data.empty:
        logger.info(f"✓ Crypto data fetched successfully: {len(crypto_data)} rows")
    else:
        logger.error("✗ Failed to fetch crypto data")

def test_technical_analysis():
    """Test technical analysis module"""
    logger.info("Testing technical analysis...")
    fetcher = DataFetcher()
    ta = TechnicalAnalysis()
    
    # Get test data
    data = fetcher.get_stock_data('AAPL', period='1m', interval='1d')
    if data is None or data.empty:
        logger.error("✗ Failed to get test data for technical analysis")
        return
    
    # Test moving average
    ma = ta.calculate_moving_average(data, period=20)
    if ma is not None:
        logger.info("✓ Moving average calculated successfully")
    else:
        logger.error("✗ Failed to calculate moving average")
    
    # Test MACD
    macd = ta.calculate_macd(data)
    if macd is not None:
        logger.info("✓ MACD calculated successfully")
    else:
        logger.error("✗ Failed to calculate MACD")
    
    # Test RSI
    rsi = ta.calculate_rsi(data)
    if rsi is not None:
        logger.info("✓ RSI calculated successfully")
    else:
        logger.error("✗ Failed to calculate RSI")

def main():
    """Main test function"""
    try:
        logger.info("Starting Fincept Terminal test...")
        test_data_fetcher()
        test_technical_analysis()
        logger.info("Test completed successfully!")
    except Exception as e:
        logger.error(f"Test failed: {e}")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
